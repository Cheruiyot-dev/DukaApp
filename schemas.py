from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class CreateCustomerRequest(BaseModel):
    username: str
    email: str
    password: str


class CreateCustomerResponse(BaseModel):
    id: int
    username: str
    email: str


class LoginRequest(BaseModel):
    username: str
    password: str


class ProductRequest(BaseModel):
    name: str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None



