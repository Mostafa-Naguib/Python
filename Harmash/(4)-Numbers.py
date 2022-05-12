# complex number
# you can't convert a complex number to any type
import math
import random
c = 3+5j
print(complex(3, 5))
print(f"{c} is {type(c)}")
print("The real part is: ", c.real)
print("The imaginary part is: ", c.imag)


# binary   'base 2'
print("=" * 50)
b = "10101"
# to convert binary 'in string' to decimal
print(int(b, 2))


# Octal  'base 8'
print("=" * 50)
o = 0o5
print(o)
print(int(str(o), 8))


# Hexa-decimal 'base 16'
print("=" * 50)
h = 0x5
print(h)
print(int(str(h), 16))


print("======================================================")
# Functions:

# abs()
x = -3
print(f"The absolute value for {x} => {abs(x)}")


# round()
print("=" * 55)
x = 3.14159265359
print(f"PI is {round(x, 2)}")


# max()
print("=" * 55)
LI = [1, 2, 3, 4, 5]
print(f"The maximum number is: {max(LI)}")


# min()
print("=" * 55)
LI = [1, 2, 3, 4, 5]
print(f"The minimum number is: {min(LI)}")


print("=================================")
# module:

# ceil(math)
x = 3.543
print(f"The nearst number to {x} is: {math.ceil(x)}")

# floor(math)
print("=" * 55)
x = 3.543
print(f"The nearst number to {x} is: {math.floor(x)}")

# pow(math)
print("=" * 55)
x, y = 2, 2
print(f"{x} power {y} is: {math.pow(2, 2)}")

# sqrt(math)
print("=" * 55)
x = 9
print(f"{x} square equals: {math.sqrt(x)}")

# gsd(math)
print("=" * 55)
x, y = 25, 44
print(f"The Greatest Common Divisor is: {math.gcd(x, y)}")

# pi and exponential
print("=" * 55)
print(f"pi = {math.pi}")
print(f"exponential = {math.e}")

# random(random)
print("=" * 55)
print(f"a random number is:  {random.random()}")
print(f"a random number is converted to decimal: {math.ceil(random.random()*10)}")


# uniform(random)
print("=" * 55)
x = 1
y = 13
print(f"a random float number between {x, y} is: {random.uniform(x, y)}")

# randrange(random)
print("=" * 55)
x = 0
y = 10
print(f"a random integer number between {x, y} is: {random.randrange(x, y, 2)}")

# choice(random)
print("=" * 55)
list = ["Car", "Villa", "Phone", "Laptop", "Traveling"]
print(f"A random wish: {random.choice(list)}")

# shuffle(random)
print("=" * 55)
LI = [1, 2, 3, 4, 5]
print(LI)
random.shuffle(LI)
print(LI)
