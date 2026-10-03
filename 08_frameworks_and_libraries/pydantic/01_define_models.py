from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    # required
    uid: int
    username: str
    email: str

    # not required
    bio: str = "just a test"
    is_active: bool = True
    full_name: str | None = None
    verified_at: datetime | None = None

user = User(uid=123, username="John", email="john@gmx.com")
print(user)
print(user.uid)
print(user.username)

# override does not trigger revalidation
print(user.bio)
user.bio=123
print(user.bio)

# to dict
print(user.model_dump())

# to json
print(user.model_dump_json(indent=2))