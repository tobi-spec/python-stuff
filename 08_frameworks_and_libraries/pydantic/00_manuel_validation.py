def create_user(username, email, age):
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if not isinstance(email, str):
        raise TypeError("email must be a string")
    if not isinstance(age, int):
        raise TypeError("age must be a integer")

    return {"username": username, "email": email, "age": age}

user1 = create_user(username="john", email="john@gmx.com", age=24)
print(user1)

user2 = create_user(username="john", email=None, age="24")
print(user2)


from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

user3 = User(username="john", email="john@gmx.com", age=24)
print(user1)

user4 = User(username="john", email=None, age="24")
print(user2)