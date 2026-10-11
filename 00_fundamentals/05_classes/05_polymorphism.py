
# method overwrite
class Animal:
    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


for animal in [Dog(), Cat(), Animal()]:
    print(animal.speak())  # Woof, Meow, ...

# duck typing
class Robot:
    def speak(self) -> str:
        return "beep"

for thing in [Dog(), Robot()]:
    print(thing.speak())

# in standard methods

print(1 + 2)
print("1" + "2")