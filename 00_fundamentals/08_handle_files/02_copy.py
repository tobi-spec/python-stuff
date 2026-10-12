with open("./files/test.txt", "r") as read_file:
    content = read_file.read()

    with open("./files/test_copy.txt", "w") as copy_file:
        copy_file.write(content)