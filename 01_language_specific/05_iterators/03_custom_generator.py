def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1,10)

for num in nums:
    print(num)