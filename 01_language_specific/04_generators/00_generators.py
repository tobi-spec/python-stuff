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


