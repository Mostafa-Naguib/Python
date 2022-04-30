# all()
list = [1, 2, 3, 4, 5, 0]
if all(list):
    print("Everything is fine")
else:
    print("There's a problem in the program")

print("=======================================")

# any()
list = [1, 2, 3, 4, 5, 0]
if any(list):
    print("There's a true value")
else:
    print("There's no true value in the list")


print("=======================================")


# bin()
print(bin(2001))


print("=======================================")

# id()
x = "Mosafa"
print(id(x))


print("=======================================")

# sum()
List = [1, 2, 3, 4, 5, 6, 7]
print(sum(list))
print(sum(list, 100))


print("=======================================")

# round(number, numOfDigit)
a = 10.998
print(round(a, 2))


print("=======================================")

# range()
# List = [1, 2, 3, 4, 5, 6, 7]
# print(List.range(1, 7, 1))


print("=======================================")

# print()
print("Mostafa", "Naguib", "EL-Sayed", "Hassan", sep="-")
print("Welcome to Arab World", end="=>")
print("In Egypt")


print("=======================================")

# abs()
print(abs(100))
print(abs(-100))
print(abs(99.9))


print("=======================================")

# pow()
print(pow(2, 2))
print(pow(2, 2, 2))


print("=======================================")

# min()
tuple = (1, -2, 3, 4, 5)
print(min(2, 4, 6, 7))
print(min("a", "s", "v", "z"))
print(min(tuple))


print("=======================================")

# slice()
x = [112, 232, 332, 44, 543, 6434]
print(x[:])
print(x[slice(0, 100)])


print("=======================================")

# enumerate()
capitals = ["Ottawa", "Brasília", "Brussels", "Athens"]

counter = enumerate(capitals, 1)
print(type(counter))

for x, y in counter:
    print(f"{x}- {y}")


print("=======================================")
# help()
print(help(print))


print("=======================================")
# reversed()
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in reversed(li):
    print(x)
