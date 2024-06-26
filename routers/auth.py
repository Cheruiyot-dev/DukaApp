from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import Token
from database import get_db
from models import SalesAgent
from oauth2 import create_access_token

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    sale_agent = db.query(SalesAgent).filter(SalesAgent.username == user_credentials.username).first()

    if not sale_agent:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"username": sale_agent.username})

    return {"access_token": access_token, "token_type": "bearer"}
