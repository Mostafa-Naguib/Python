# Truncate
x = open("Hello.txt", "a")
x.truncate(30)

x = open("Hello.txt", "a")
print(x.tell())

x = open("Hello.txt", "r")
x.seek(8)
print(x.read())
