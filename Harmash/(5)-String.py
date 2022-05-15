name = "Mostafa Naguib"
religion = 'Muslim Sunni'
fQuote = """you either live longer to see yourself become the villan
or you die  a Hero"""
sQuote = '''Many of life's failures are people who did not realize
how close they were to success when they gave up'''
print(name)
print(religion)
print(fQuote)
print(sQuote)
# indexing:
for x in range(0, 7):
    print(name[x], end="")
print()
for x in range(-5, 0):
    print(religion[x], end="")
print()
# slicing:
print('=' * 44)
print(name[:7])
print(religion[7:])

# Function (Searching)
# count()
print("=" * 55)
print(name.count("a"))

# find()
print("=" * 55)
print(name.find("M"))

# rfind()
print("=" * 55)
print(name.rfind("a"))

# index()
print("=" * 55)
print(name.index("Naguib"))  # give an error when it doesn't find the value

# rindex()
print("=" * 55)
print(name.rindex("Naguib"))

# function (Substring)
# split()
print("=" * 55)
opinion = "Python is the easist programing language in the world..."
arr = opinion.split(" ")

for x in arr:
    print(x, end=" ")
print()

# splitlines()
print("=" * 55)
ID = """My name is Mostafa.\nI'm 20 years old.\nI live in Cairo."""
arr = ID.splitlines()
print(len(arr))
for x in arr:
    print(x)

# function ()
# replace()
print("=" * 55)

opinion = "Python is the easist programing language in the world..."
print(opinion.replace("Python", "C++"))

# maketrans()
print("=" * 55)
myName = "Mostafa Naguib"
dict = str.maketrans(" ", "-")

print(myName)
print(myName.translate(dict))

password = "EL-Zamalek"
dictionary = str.maketrans({
    "-": "_",
    "L": "l",
    "m": "=m=",
})
print(password)
print(password.translate(dictionary))

massage = "From the Nile to the sea palestine is free"
print(massage.upper())
print(massage.lower())
print(massage.swapcase())
print(massage.capitalize())
print(massage.title())

name = 'Mostafa Naguib ElSayed Hassan'
arr = name.split()
deco = '-'
print(deco.join(arr))

name = " Mostafa "
print(name.center(11, "@"))


name = 'Mostafa\tNaguib\tElSayed\tHassan'
print(name.expandtabs(19))


name = "@#$Mostafa@#$"
print(name.strip("@#$"))
print(name.rstrip("@#$"))
print(name.lstrip("@#$"))

name = " Mostafa "
print(name.rjust(11, "@"))
print(name.ljust(11, "@"))
