from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl, validator, SecretStr, ConfigDict
from datetime import datetime
from typing import Literal, Annotated

class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uid: UUID = Field(alias="id", default_factory=uuid4) # takes id value from user_data instead of creating new uid
    username: str
    email: EmailStr
    age: int
    password: SecretStr

user_data = {
    "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": "39",
    "password": "secret123",
}
user = User.model_validate(user_data)

print(user.model_dump_json(indent=2,
                           by_alias=True, # set attribute name uid to id
                           exclude={"password"})
      )