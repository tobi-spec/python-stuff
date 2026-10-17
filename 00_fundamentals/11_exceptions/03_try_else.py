try:
    f = open("exists.txt")
    print(f.read())
except FileNotFoundError as e:
    print(e)
else:
    f.close()