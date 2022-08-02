class Struct:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def info(self):
        print(f"Your name is: {self.name}")
        print(f"Your age is: {self.age}")
        print("=" * 55)
