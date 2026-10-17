
try:
    f = open("not_exists.txt")
except FileNotFoundError:
    print("No config found in directory")
except PermissionError:
    print("Application hasn´t the permission to read file")
except UnicodeDecodeError:
    print("Error in unicode decoding")
except OSError:
    print("IOError: An I/O error occurred")