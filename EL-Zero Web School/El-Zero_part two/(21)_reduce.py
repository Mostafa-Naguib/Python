from functools import reduce


def num(x, y):
    return x + y


li = [1, 2, 3, 4, 5, 6, 7]


print(reduce(num, li))

# ========================================
print("=" * 44)

li = [11, 22, 33, 44, 55, 66, 77]

print(reduce((lambda x, y: x + y), li))
