# my own solution...
row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))


for i in range(1, row + 1):

    for j in range(1, (row-i)+1):
        print(" ", end="")
    for k in range(1, column + 1):
        print("*", end="")
    print()


# the first solution...
print("=" * 50)

row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))


for x in range(1, row + 1):
    print(" " * (row - x), end="")
    print("*" * column, end="")
    print()


# the second solution...
print("=" * 50)

row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))

i = 1
while row >= i:
    j = 1
    k = 1
    while row-i >= j:
        print(" ", end="")
        j += 1
    while column >= k:
        print("*", end="")
        k += 1
    print()
    i += 1
