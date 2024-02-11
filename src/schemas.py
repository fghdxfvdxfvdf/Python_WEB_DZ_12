from datetime import date

from pydantic import BaseModel, EmailStr, Field

from src.database.models import Role


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str = None


class ContactUpdatedModel(BaseModel):
    updated: bool = False


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str = None


class UserModel(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=1, max_length=100)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    avatar: str
    roles: Role

    class Config:
        orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
