# map is a predfiened function...
def typeNumber(num):
    if num % 2 == 0:
        return f"{num} is even number"
    else:
        return f"{num} is odd number"


tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for x in map(typeNumber, tuple):
    print(x)

# using lambda function...
print("=" * 55)

list = [11, 12, 13, 14, 15, 16, 17, 18, 19]

for x in map(lambda num: f"{num} is even number" if num % 2 == 0 else f"{num} is odd number", list):
    print(x)
