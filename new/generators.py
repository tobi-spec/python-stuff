my_nums = [1,2,3,4,5]

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

print(square_numbers(my_nums))

# doesn't hold complete result in memory
# but processes inputs step by step
# can be used when the amount of objects to loop over
# is to high to keep all of it in memory
def square_numbers_generator(nums):
    for i in nums:
        yield i*i

my_gen_numbers = square_numbers_generator(my_nums)
print(next(my_gen_numbers))
print(next(my_gen_numbers))
print(next(my_gen_numbers))
print(next(my_gen_numbers))
print(next(my_gen_numbers))

########################
import psutil
import os


def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem


import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.perf_counter()
people = people_list(1000000)
t2 = time.perf_counter()

print ('Memory (After) : {}Mb'.format(memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))

t1 = time.perf_counter()
people = people_genjjkerator(1000000)
t2 = time.perf_counter()

print ('Memory (After) : {}Mb'.format(memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))
