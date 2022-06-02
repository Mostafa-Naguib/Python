def greeting(name):
    return f"Welcome {name}"


print(greeting("Mostafa"))


def x(name): return f"Welcome {name}"


print(x("Mostafa"))


print(greeting.__name__)
print(x.__name__)

print(type(x))
