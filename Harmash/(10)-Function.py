def calculator(a, b):
    """This function is for addition..."""
    return a + b


print(calculator.__doc__)
print(calculator(4, 2))
# it's a different way to pass pramitars
print(calculator(b=2, a=4))

# default argument
print("=" * 55)


def name(name="Unknown"):
    print(f"Name: {name}")


name()
name("Mostafa")


# Variable-length Arguments: and the pramitars will be tuple
def calculator(*numbers):
    print(type(numbers))
    print(sum(numbers)/len(numbers))


calculator(1, 2, 3, 4, 5, 6, 7, 8, 9)


# Local Variables vs Global Variables:

# global variables are outside the functions...
x = 5


def test():
    # local variables are inside the functions...
    global y
    y = 10
    print(x)


test()
print(y)


# lambda functions...
# func = lambda born, date: date - born


# print(func(2001, 2022))

# print(func.__name__)
