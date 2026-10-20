nums = [1,2,3]

for num in nums:
    print(num)

# iterable: nums has __iter__ for looping
print(dir(nums))

# iterator: has a state to be aware of its position by __next__
i_nums = iter(nums) # same has nums.__iter__
print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
