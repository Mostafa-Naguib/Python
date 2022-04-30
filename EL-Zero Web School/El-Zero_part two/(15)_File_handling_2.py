x = open("Hello.txt")

print(x)
print(x.name)
print(x.mode)
print(x.encoding)


# print(x.read())
# print(x.read())

# print(x.readline())
# print(x.readline(10))

# print(x.readlines())
# print(type(x.readlines()))

for L in x:
    print(L)
    if L.startswith("5"):
        break

x.close()
