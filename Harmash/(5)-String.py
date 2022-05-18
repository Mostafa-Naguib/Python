name = "Mostafa Naguib"
religion = '"Muslim"\
Sunni'
fQuote = """you either live longer to see yourself become the villan
or you die  a Hero\b"""
sQuote = '''Many of life's failures are people who did not realize
how close they were to \"success\" when they gave up'''
print("I was born on 2001\\10\\10")
print(name)
print(religion)
print(fQuote)
print(sQuote)

# indexing:
print('=' * 20, 'indexing', '=' * 20)
for x in range(0, 7):
    print(name[x], end="")
print()
for x in range(-5, 0):
    print(religion[x], end="")
print()

# slicing:
print('=' * 20, 'slicing', '=' * 20)
print(name[0:7:1])
print(religion[8:])

# Function (Searching)
print('=' * 10, '@Function(searching)@', '=' * 10)

# count()
print('=' * 20, 'count()', '=' * 20)
print(name.count("a"))

# find()
print('=' * 20, 'find()', '=' * 20)
print(name.find("M"))  # It gets the index of this "letter"

# index()
print('=' * 20, 'index()', '=' * 20)
print(name.index("Naguib"))  # give an error when it doesn't find the value


# function (Substring)
print('=' * 10, '@Function(Substring)@', '=' * 10)

# split()
print('=' * 20, 'split()', '=' * 20)
opinion = "Python is the easist programing language in the world..."
print(opinion.split())

# splitlines()
print('=' * 20, 'splitlines()', '=' * 20)
ID = """My name is Mostafa.\nI'm 20 years old.\nI live in Cairo."""
print(ID.splitlines())


# function(Replacing)
print('=' * 10, '@Function(Replacing)@', '=' * 10)

# replace()
print('=' * 20, 'replace()', '=' * 20)
opinion = "Python is the easist programing language in the world..."
print(opinion.replace("Python", "C++"))

# maketrans() and translate()
print('=' * 20, 'maketrans() & translate()', '=' * 20)
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

# function(Comparison)
print('=' * 10, '@Function(Comparison)@', '=' * 10)

massage = "From the Nile to the sea palestine will be free"
print('=' * 20, 'upper()', '=' * 20)
print(massage.upper())
print('=' * 20, 'lower()', '=' * 20)
print(massage.lower())
print('=' * 20, 'swapcase()', '=' * 20)
print(massage.swapcase())
print('=' * 20, 'capiltalize()', '=' * 20)
print(massage.capitalize())
print('=' * 20, 'title()', '=' * 20)
print(massage.title())

# split()
print('=' * 20, 'join()', '=' * 20)
name = 'Mostafa Naguib ElSayed Hassan'
arr = name.split()
deco = '-'
print(deco.join(arr))

# center()
print('=' * 20, 'center()', '=' * 20)
name = " Mostafa "
print(name.center(11, "@"))

# expandtabs()
print('=' * 20, 'expandtabs()', '=' * 20)
name = 'Mostafa\tNaguib\tElSayed\tHassan'
print(name.expandtabs(19))

# strip()
print('=' * 20, 'strip()', '=' * 20)
name = "@#$Mostafa@#$"
print(name.strip("@#$"))
print(name.rstrip("@#$"))
print(name.lstrip("@#$"))

# just()
print('=' * 20, 'just()', '=' * 20)
name = " Mostafa "
print(name.rjust(11, "@"))
print(name.ljust(11, "@"))


# function(Manipulation)
print('=' * 10, '@Function(Manipulation)@', '=' * 10)

# startswith()
print('=' * 20, 'startswith()', '=' * 20)
tuple = ('Egypt', 'Sudan', 'Libya')
massage = 'Egypt is the place where i live rightnow...'
print(massage.startswith(tuple))

# endswith()
print('=' * 20, 'endswith()', '=' * 20)
massage = 'Welcome to our website python.edu'
domain = ('com', 'net', 'edu', 'org')
print(massage.endswith(domain))

# isalpha() just accept alphabet letter
print('=' * 20, 'isalpha()', '=' * 20)
text = 'abcdefg'
print(text.isalpha())

text = 'abcd efg'
print(text.isalpha())

# isnumeric() just accept normal number
print('=' * 20, 'isnumeric()', '=' * 20)
number = '1234'
print(number.isnumeric())

# isdigit() doesn't accept any fraction number (just integer)
print('=' * 20, 'isdigit()', '=' * 20)
number = '1234'
print(number.isdigit())

# isalnum() can accept (A, a, 1, 2)
print('=' * 20, 'isalnum()', '=' * 20)
massage = '32 MOSTAFATWENTY'
print(massage.isalnum())

name = 'Mostafa'
print('=' * 20, 'islower()', '=' * 20)
print(name.islower())  # it cares about the whole text
print('=' * 20, 'isupper()', '=' * 20)
print(name.isupper())  # it cares about the whole text
print('=' * 20, 'istitle()', '=' * 20)
print(name.istitle())  # it cares about the whole text
print('=' * 20, 'isspace()', '=' * 20)
print(name.isspace())  # it cares about the whole text

print("=" * 55)
s = 'Python is an easy language'
print('easy' in s)
print('easy' not in s)
