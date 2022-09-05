# my own solution...
row = 0
while row <= 0:
    row = int(input("Enter the number of row: "))

column = 0
while column <= 0:
    column = int(input("Enter the number of column: "))

for i in range(1, row + 1):

    if i == 1 or i == row:
        print("*" * column)

    else:
        print("*", end="")
        print(" " * (column - 2), end="")
        print("*")
