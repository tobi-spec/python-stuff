var1 = "Hello World"
num1 = 1
num2 = 2

merge = var1 + str(num1)
print(merge)

if var1 == "Hello World":
    print("The variable is equal to 'Hello World'")
else:
    print("The variable is not equal to 'Hello World'")

for i in range(5):
    print(i)

list1 = []
list1.append("value1")
list1.append("value2")
list1.append("value3")

for element in list1:
    print("Item: " + element)

def simple_addition(a, b):
    return a + b

result = simple_addition(num1, num2)
print(("Addition result: " + str(result)))

class SimpleClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print("Value is:", self.value)

simple_class = SimpleClass(10)
simple_class.display_value()