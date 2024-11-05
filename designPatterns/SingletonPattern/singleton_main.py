from designPatterns.SingletonPattern.singleton import Singleton

singleton1 = Singleton()
singleton1.show_message()

singleton2 = Singleton()
singleton2.show_message()

if singleton1 is singleton2:
    print("Both references are the same instance.")
else:
    print("Different instances.")