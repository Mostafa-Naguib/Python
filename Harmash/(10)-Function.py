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


# packing and unpacking
print("=" * 10, "Packing and unpacking", "=" * 10)
companies_with_dates = {
    "Microsoft": 1975,
    "Apple": 1976,
    "Google": 1998,
    "IBM": 1911,
    "Intel": 1968,
    "AMD": 1969
}


def history(writer, **companies_with_dates):
    print(type(companies_with_dates))

    for key, value in companies_with_dates.items():
        print(f"{key} is founded in \"{value}\"...")


history("Mostafa", **companies_with_dates)


# recursive functions...
print("=" * 10, "recursive-Function", "=" * 10)
f = 1


def recursion(num):
    if num == 1:
        return 1
    else:
        # the first num is stash
        return num * recursion(num - 1)


print(recursion(6))
