name: str = "Corey"
age: int = 38

def create_user(first_name: str, last_name: str, age:int | None = None) -> dict[str, str|int|None]:
    email: str = f"{first_name}.{last_name}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,}

user1: dict = create_user("John", "Smith", age=21)
user2: dict = create_user("John", "Cena")

print(user1)
print(user2)
