tuple = (2001, ) * 5

odd = (1, 3, 5, 7, 9, 11)
for num in odd:
    print(num)
print("-"*40)
# index[]
num_1 = odd[0]
print(num_1)
# slicing[:]
num_2 = odd[0:3]
print(num_2)

even = (0, 2, 4, 6, 8, 10)
odd = (1, 3, 5, 7, 9, 11, even[0])
num = even + odd
print(num)
print(0 in even)

# function: class
print("=" * 10, "1-Function", "=" * 10)
# count()
print("=" * 20, "count()", "=" * 20)
tuple = (1, 2, 2, 2, 3, 4, 5)
print(tuple.count(2))

# index() it gives error when it doesn't find the value...
print("=" * 20, "index()", "=" * 20)
tuple = (1, 2, 2, 2, 3, 4, 5)
print(tuple.index(2, 2, 4))

# function: (built in)
print("=" * 10, "2-Function", "=" * 10)
base_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("=" * 20, "len()", "=" * 20)
print(len(base_10))

print("=" * 20, "min()", "=" * 20)
print(min(base_10))

print("=" * 20, "max()", "=" * 20)
print(max(base_10))


# Destruct...
Numbers = (1, 2, 0, 3)
A, B, _, C = Numbers

print(A)
print(B)
print(C)
