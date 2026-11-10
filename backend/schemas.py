
from pydantic import BaseModel, EmailStr, Field


# User Registration Schema
class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


# User Response Schema
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool

    model_config = {"from_attributes": True}


# User Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str
