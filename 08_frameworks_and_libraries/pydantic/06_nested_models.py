from pydantic import BaseModel, Field, EmailStr, ValidationError, SecretStr
from uuid import UUID, uuid4
from typing import Annotated

class SocialMediaUser(BaseModel):
    username: str
    email: EmailStr
    age: int
    password: SecretStr

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPost(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    author_id: str | int
    author: SocialMediaUser
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    comments: list[Comment] = Field(default_factory=list)


post_data = {
    "author_id": 1,
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "author": {
        "username": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

try:
    post = BlogPost(**post_data)
    print(post.model_dump_json(indent=2))
except ValidationError as e:
    print(e)