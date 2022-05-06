# All data in python are "objects"...

help("keywords")

# Syntax => [Variable Name] [Assignment Operator] [Value]

a = b = c = 10
A, B, C = 10, 100, 1000

print(a, b, c)
print(A, B, C)

name = "Mostafa "
age = 20
religion = " Muslim"

# Concatinate many variables in just one...
identity = name + str(age) + religion
print(identity)

cairo = "I love cairo "  # Single word=> standard
egyptCairo = "I love cairo"  # Tow words=> camelCase
egypt_cairo = "I love cairo"  # Tow words=> snake_case
