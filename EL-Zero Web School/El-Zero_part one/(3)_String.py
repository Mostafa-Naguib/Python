# String

FullName = "'Mostafa' Naguib El-Sayed Hassan Ali"
FullName = '"Mostafa" Naguib El-Sayed Hassan Ali'

ID1 = """I'm Mostafa
I'm 20 years old
I live in "Egypt"
I'm learning 'python'
"""
a_quote = """you either live longer to see yourself become the \\\ villan
or you die  a Hero"""
print(a_quote)

print("______________________________________________")

# Index
country = "I love Egypt so much"
print(country[0])

# Slicing
country = "I love palestine so much"
print(country[:16])
print(country[0::2])

print("______________________________________________")
print("______________________________________________")

# Start from String methods

print("______________________________________________")
# 1- strip() rstrip() lstrip()
country1 = "       I love palestine so much         "
country2 = "@@@@@I love palestine so much@@@@@"

print(country1.strip())
print(country2.rstrip("@"))
print(country2.lstrip("@"))


print("______________________________________________")
# 2-title()
news = "egypt confirmed that it couldn't install 5g network due to \
exprnsive g5 architecture"
print(news.title())

print("______________________________________________")
# 3-capitalize()
news = "egypt confirmed that it couldn't install 5g network due \
to exprnsive g5 architecture"
print(news.capitalize())

print("______________________________________________")
# zfill
a, b, c, d = "1", "19", "199", "1999"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))


print("______________________________________________")
# split=>convert to list
FullName = "Mostafa Naguib El-Sayed Hassan Ali"
print(FullName.split())
print(FullName.splitlines())

FullName = "Mostafa-Naguib-ElSayed-Hassan-Ali"
print(FullName.split("-"))
print(FullName.split("-", 3))
print(FullName.rsplit("-", 2))

print("______________________________________________")
# 2-Center()
Name = "Mostafa"
print(Name.center(11, "@"))


print("______________________________________________")
# count
Quote = "IF NOT NOW WHEN"
print(Quote.count("NOW"))


print("______________________________________________")
# swapcase
Quote = "Never stop learning because life never stops teaching"
print(Quote.swapcase())


print("______________________________________________")
# Startswith
Quote = "Over thinking killing your happeniss"
print(Quote.startswith("Over"))


print("______________________________________________")
# Index (Substring, Start, End)
Quote = "When it hurts-observe. Life is trying to teach you something"
print(Quote.index("Life", 5, 53))
# print(Quote.index("Life",5,7))


print("______________________________________________")
# Find (Substring, Start, End)
Quote = "A journey of a thousand miles begins with a single a step"
print(Quote.find("j", 0, 14))
print(Quote.find("j", 0, 1))


print("______________________________________________")
# rjust(Width, Fill char)    ljust(Width, Fill char)
Brand = "Addidas"
print(Brand.rjust(17, "@"))
print(Brand.ljust(17, "@"))


print("______________________________________________")
# SplitLines
Populatation = """China
India
USA"""
print(Populatation.split())
print(Populatation.splitlines())


print("______________________________________________")
# Expandtabs
billioners = "Jeff bezuoz\tElon musk\tMark zuggerberg\tBill gates"
print(billioners.expandtabs(5))

print("______________________________________________")
# is
News = "Now China is developing 6G of network"
print(News.istitle())

warning = "YOU HAVE TO WEAR A MASK IN TRANSPORTATIONS"
print(warning.isupper())

ID = "@Mostafa"
print(ID.isidentifier())

X = "AAAABBBBBCCCC"
Y = "AAAABBBCCC111222333"
print(X.isalpha())
print(Y.isalpha())
print(Y.isalnum())
print(X.isalnum())


print("______________________________________________")
# replace(Old value, New value, count)
X = "Ahmed naguib Elsayed Hassan Ali"
print(X.replace("Ahmed", "Moustafa", 1))


print("______________________________________________")
# Join(Iterable)
Name = ["Moustafa", "Naguib", "Elsayed", "Hassan", "Ali"]
print("-".join(Name))


# ---------------------------------------------------------------------
print("\n\n\n@#________$____________@#____________$_____________@#")
print("_____________________________________________________")
print("@#________$____________@#____________$_____________@#")


# Formating old way
# place_holder
print("Formating old way\n")
Name = "Mostafa"
Age = 20
Salary = 35000
print("My name is: %s I'm %d, I'm working in secret group of programmers and,\
my salary is %.1f" % (Name, Age, Salary))


print("____________________________________________________")
# Formating New way
# place_holder
print("Formating New way\n")
Name = "Mostafa"
Age = 20
Salary = 35000
print("My name is: {:s} I'm {:d}, I'm working in secret group of programmers and, \
my salary is {:d}\n\n" .format(Name, Age, Salary))


# Truncate String
Message = " One day palestine will be free"
print("Trust me when i tell you that {:.100000s}" .format(Message))


# Format_money
Mymoney = 9975222
print("I have {:,d} in my Depit card" .format(Mymoney))


# ReArange item
Player1, Player2, Player3 = "Ronaldo", "Messi", "Mohammed Saleh"
print("Rank of the best players of the world {2:s} {0:s} \
{1:s}" .format(Player1, Player2, Player3))

# Fromat in Python 3.6+
Player = "Shikaballa"
His_Age = 35
print(f"My favorite player is {Player}, and his age is {His_Age:d}")
