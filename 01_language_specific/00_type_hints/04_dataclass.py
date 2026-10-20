from typing import NewType
from dataclasses import dataclass

name: str = "Corey"
age: int = 38

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | HSL | None = None

def create_user(first_name: str, last_name: str, age:int | None = None, fav_color: RGB | HSL | None = None) -> User:
    email: str = f"{first_name}.{last_name}@example.com"
    return User (
        first_name= first_name,
        last_name= last_name,
        email= email,
        age= age,
        fav_color= fav_color
    )

user1: User = create_user("John", "Smith", age=21, fav_color=RGB((123, 124, 255)))
user2: User = create_user("John", "Cena", fav_color=HSL((206, 124, 255)))

print(user1)
print(user2)