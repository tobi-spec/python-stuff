from pydantic import BaseModel, Field, field_validator, ValidationError, HttpUrl, EmailStr, model_validator
from typing import Annotated


class User(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=20)]
    website: HttpUrl = None

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric, underscores are allowed")
        return v.lower()

    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http", "https")):
            return f'https://{v}'
        return v

try:
    user = User(
        username="!!CoreySchafer!!",
        website="mysite.com"
    )
except ValidationError as e:
    print(e)


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_password(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords don't match")
        return self

try:
    registration = UserRegistration(
        email="test@gmx.com",
        password="admin123",
        confirm_password="user1234"
    )
except ValidationError as e:
    print(e)