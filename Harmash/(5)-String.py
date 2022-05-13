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
print(name[0] + name[1] + name[2] + name[3] + name[4] + name[5] + name[6])
print(religion[-5] + religion[-4] + religion[-3] + religion[-2] + religion[-1])
# slicing:
print('=' * 44)
print(name[:7])
print(religion[7:])

# Function (Searching)
# count()
print("=" * 55)
print(name.count("M"))

# find()
print("=" * 55)
print(name.find("M"))

# rfind()
print("=" * 55)
print(name.rfind("a"))

# index()
print("=" * 55)
print(name.index("Naguib"))

# rindex()
print("=" * 55)
print(name.rindex("Naguib"))
