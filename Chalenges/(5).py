# my own solution...
row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))


for i in range(1, row + 1):
    print(" " * (i - 1), end="")
    print("*" * column, end="")
    print()


# the first solution...
row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))

i = 1
while i <= row:
    j = 1
    while j < i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= column:
        print("*", end="")
        k += 1
    i += 1
    print()


# the second solution...
row = 0
while row <= 0:
    row = int(input("Enter the number of rows: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of columns: "))

for i in range(1, row + 1):
    for j in range(1, i):
        print(" ", end="")

    for k in range(1, column + 1):
        print("*", end="")
    print()
