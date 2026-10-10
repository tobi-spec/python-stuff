# higher order functions take functions as argument or return functions

def my_map(my_func, my_iterable):
    result = []
    for item in my_iterable:
        result.append(my_func(item))
    return result


my_list = [1, 2, 3, 4, 5]
print(my_map(lambda x: x ** 3, my_list))


# also called closure
def logger(msg):
    def log_message():
        print("Log: ", msg)

    return log_message

log_hi = logger("Hi!")
log_hi() # hi logger can be called multiple times without the need of passing the string every time


# not working counter example
def log_message(msg):
    print("Log: ", msg)

def logger(msg):
    return log_message(msg)

log_hi = logger("Hi2")
log_hi() # throws error because logger("Hi2") happens immediately when called, not just returning a function that can be called later
