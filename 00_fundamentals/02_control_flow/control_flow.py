# for loop
for i in range(10):
    print(i)

# while loop
counter = 0
while counter < 15:
    if counter % 2 == 0:
        counter += 1
        continue
    else:
        print(counter)
        counter += 1
    if counter == 10:
        break



