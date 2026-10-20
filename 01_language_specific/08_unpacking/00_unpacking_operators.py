# from list to individual elements
# [1,2,3,4,5,6] -> 1, 2, 3, 4, 5, 6

# unpack list
values = [1,2,3,4,5,6]
print(values)
print(*values)

# unpack list into parameters
def my_sum(a,b,c):
    return a+b+c
values = [1,2,3]
print(my_sum(* values))

# unpack list in variables
values = [1,2,3]
v1, v2, v3 = values

print(v1, v2, v3)

values = [1,2,3,4,5,6]
v1, *v2, v3 = values

print(v1, v2, v3)

# combine lists
list1 = [1,2,3]
list2 = [4,5,6]
print([list1,list2])

combined = [*list1, "hi", *list2]
print(combined)

# add different amount of variables
def my_args(*args):
    results = 0
    for item in args:
        results += item
    return results
print(my_args(10,20,30,40,50))

# {"a": 1, "b":2, "c":3} -> myfunction(a=1, b=2, c=3)
def my_print(name, age, job):
    print(name, age, job)

d1 = {"name": "Jakob", "age": 20, "job": "programmer"}
my_print(**d1)

# combine dicts
d2 = {"height": 173, "weight": 85}
combined = {**d1, **d2}
print(combined)

def my_function(**kwargs):
    print("The following paramters were passed")
    for key, value in kwargs.items():
        print(key, value)

my_function(name="Jakob", age=20, job="programmer")
