# with keyword is a context manager, to close file after use automatically
with open("./files/test.txt", "r") as file:
    content = file.read()
    print(content)

print("\n------------------")
# does not load all content into memory at once
with open("./files/test.txt", "r") as file:
    for line in file:
        print(line, end="")

print(" \n------------------")
# reads x characters of the file
with open("./files/test.txt", "r") as file:
    size_to_read = 10
    file_contents = file.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents, end="*")
        file_contents = file.read(size_to_read)



