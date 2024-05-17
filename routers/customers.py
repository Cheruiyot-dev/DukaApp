from fastapi import APIRouter,  Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import CreateCustomerRequest, CreateCustomerResponse, User
from database import get_db
from models import Customer
from sqlalchemy import or_
from utility import pwd_context

router = APIRouter(
    prefix='/customers',
    tags=['Customers'] 
)


@router.post("/register_customer", response_model=CreateCustomerResponse)
async def register_customer(customer: CreateCustomerRequest,
                            db: Session = Depends(get_db)) -> \
                                CreateCustomerResponse:
    existing_customer = db.query(Customer).filter(or_(Customer.email == customer.email, Customer.username == customer.username)).first()
    if existing_customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )

    # Hash password before storing it

    hashed_password = pwd_context.hash(customer.password)

    new_customer = Customer(
        username=customer.username,
        email=customer.email,
        password=hashed_password
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    # Response
    response = CreateCustomerResponse(
        id=new_customer.id,
        username=new_customer.username,
        email=new_customer.email)

    return response


@router.get("/{customer_id}", status_code=status.HTTP_200_OK,
            response_model=User)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{customer_id} does not exist")

    return customer
