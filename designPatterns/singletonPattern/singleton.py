class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Singelton instance created!")
        return cls._instance

    def show_message(self):
        print("Hello from the Singleton Instance")
