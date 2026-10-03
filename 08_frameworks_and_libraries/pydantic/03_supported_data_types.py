from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl, validator, SecretStr
from datetime import datetime
from typing import Literal, Annotated


class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr

    website: HttpUrl = None
    password: SecretStr = None

    bio: str = "just a test"
    is_active: bool = True
    full_name: str | None = None
    verified_at: datetime | None = None
try:
    user = User(
        username="username",
        email="user@gmx.de",
        password="password1223",
    )
except ValidationError as e:
    print(e)

print(user)



class BlogPost(BaseModel):
    uid: Annotated[int, Field(gt=0)]
    author_id: str | int
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list) # creates empty list for each instance, otherwise class wide
    created_at: datetime =  Field(default_factory= lambda: datetime.now()) # creates now() for each instance not class of class init
    status: Literal["draft", "published", "unpublished"] = "draft"

    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

post = BlogPost(
    uid=1,
    title="Getting started with Python",
    content="How it begins",
    author_id="12345",
    slug="this-is-a-url-part"
)
print(post)

try:
    BlogPost(
        uid=0,
        author_id=None,
        title="Hi",
        content="Nothing.."
    )
except ValidationError as e:
    print(e)