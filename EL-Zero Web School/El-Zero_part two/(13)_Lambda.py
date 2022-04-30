def greeting(name):
    return f"Welcome {name}"


print(greeting("Mostafa"))

x = lambda name: f"Welcome {name}"

print(x("Mostafa"))


print(greeting.__name__)
print(x.__name__)

print(type(x))