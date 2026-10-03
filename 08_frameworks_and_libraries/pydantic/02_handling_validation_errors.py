from pydantic import BaseModel, ValidationError
from datetime import datetime


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

try:
    # type conversion of uid
    user = User(uid="123", username=None, email=None)
except ValidationError as e:
    print(e)