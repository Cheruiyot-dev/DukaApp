from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    id: Optional[str] = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class CreateCustomerRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class CreateCustomerResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    username: str


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


class MakeSaleRequest(BaseModel):
    buyer_first_name: str
    buyer_last_name: str
    product_name: str
    quantity_bought: int
    created_at: datetime


class SaleResponse(BaseModel):
    sale_id: int
    pid: int
    buyer_first_name: str
    buyer_last_name: str
    product_name: str
    seller_name: str
    quantity_bought: int
    created_at: datetime
    total_price: float
 

class UpdateSaleRequest(BaseModel):
    quantity_bought: Optional[int] = None
    buyer_first_name: Optional[str] = None
    buyer_last_name: Optional[str] = None
    seller: Optional[str] = None
    total_price: Optional[float] = None


class UpdateSaleResponse(BaseModel):
    sale_id: int
    pid: int
    buyer_first_name: Optional[str] = None
    buyer_last_name: Optional[str] = None
    product_name: Optional[str] = None
    seller_name: str
    quantity_bought: Optional[str] = None
    created_at: datetime
    total_price: Optional[float] = None
