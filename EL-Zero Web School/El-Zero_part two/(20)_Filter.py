def type(num):
    return num % 2 == 0


li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(type, li)))


print("=" * 55)

i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter((lambda num: num % 2 == 0), i)))
