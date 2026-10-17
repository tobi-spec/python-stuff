# with exception, doesnt break the program
try:
    f = open("not_exists.txt")
except Exception as e:
    print("This file does not exists")

# without exception, breaks the program
f = open("not_exists.txt")

print("I will not be reached")