
try:
    f = open("exists.txt")
    if f.name=="exists.txt":
        raise Exception("Corrupt File")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("error!")
else:
    f.close()
finally:
    print("done")