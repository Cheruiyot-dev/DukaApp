from datetime import timedelta
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import schemas
from schemas import CreateCustomerRequest
from auth import authenticate_user, create_access_token, \
      get_current_active_user, pwd_context
from database import engine, Base, get_db
from models import Customer, Product, Order, OrderItem
from routers import customers, products, sales

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(customers.router)
app.include_router(products.router)
app.include_router(sales.router)


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=schemas.
                                     ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@app.post("/register_customer")
async def register_customer(customer: CreateCustomerRequest,
                            db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(customer.password)

    # Check if the email already exists
    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()
    if existing_customer:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    # create a new customer
    new_customer = Customer(username=customer.username,
                            email=customer.email,
                            password=hashed_password)
    print(new_customer)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer

# Product routes



@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# Add more routes for handling customers, products, orders, etc.


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
