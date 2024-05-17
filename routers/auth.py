from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import Token
from database import get_db
from models import Customer
from oauth2 import create_access_token

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.username == user_credentials.username).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"user_id": customer.id})

    return {"access_token": access_token, "token_type": "bearer"}
