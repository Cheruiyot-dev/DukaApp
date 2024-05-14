from pydantic import BaseModel


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
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class ProductRequest(BaseModel):
    product_name: str
    product_price: float
    product_quantity: int


class ProductResponse(BaseModel):
    id: int
    product_name: str
    product_price: float
    product_quantity: int


class CustomerCreate(BaseModel):
    user_name: str
    user_password: str
    user_email: str
    user_contact: str


class CustomerResponse(BaseModel):
    id: int
    user_name: str
    user_email: str
    user_contact: str
