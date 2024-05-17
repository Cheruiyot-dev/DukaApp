from datetime import timedelta
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas import CreateCustomerRequest, CreateCustomerResponse

from database import engine, Base, get_db
from models import Customer
from routers import auth, customers, products, sales

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(sales.router)


@app.get("/")
async def index():
    return {"Duka": "Sales API"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
