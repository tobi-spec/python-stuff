from typing import Callable

# Decorator - A function that extends the behavior of another function without modifying it

def add_sprinkles(function) -> Callable:
    def wrapper(*args, **kwargs):
        print("adding sprinkles")
        function(*args, **kwargs)
    return wrapper

def add_fudge(function) -> Callable:
    def wrapper(*args, **kwargs):
        print("adding fudge")
        function(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor: str) -> None:
    print(f"Here's your {flavor} ice cream!")

get_ice_cream("Vanilla")
