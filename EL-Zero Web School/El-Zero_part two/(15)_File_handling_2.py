# functions that we use with mode(read "r") ==> read(), readline(), readlines(), seek()
file = open("Hello.txt")

print(file)
print("=" * 20, "name", "=" * 20)
print(file.name)
print("=" * 20, "mode", "=" * 20)
print(file.mode)
print("=" * 20, "encoding", "=" * 20)
print(file.encoding)

print("-" * 66)
# print(file.read())
# print(file.read(5))
# print(file.readline())
# convert the text to a list...
# print(file.readlines())
# print(type(file.readlines()))

for line in file:
    print(line)
    if line.startswith("4-"):
        break

file.close()

# seek()
file = open("Hello.txt")
file.seek(6)
print(file.read())

file.close()
