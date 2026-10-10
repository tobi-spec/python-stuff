# inline functions

def add(x, y):
    return x + y

result = lambda x,y : x + y
print(result(5, 5))

print((lambda x,y : x + y)(4,6))

