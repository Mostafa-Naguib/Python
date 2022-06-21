def decorator(func):
    def first():
        print("Hello")
        func()
        print("You're welcome")
    return first


@decorator
def name():
    print(input("Enter your name: "))


name()
