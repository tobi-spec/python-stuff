# *args undefined number of arguments
# *kwargs undefined number of keyword arguments

def order_pizza(size, *toppings, **details):
    print(f"ordered a {size} pizza")
    for topping in toppings:
        print(f"-{topping}")
    for key,value in details.items():
        print(f"{key}: {value}")


order_pizza("large", "salami", "olives", delivery=True, tip=5)