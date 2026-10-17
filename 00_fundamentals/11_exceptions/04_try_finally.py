try:
    f = open("exists.txt")
except FileNotFoundError as e:
    print(e)
else:
    f.close()
finally:
    print("done")


try:
    f = open("exists_not.txt")
except FileNotFoundError as e:
    print(e)
else:
    f.close()
finally:
    print("done also")