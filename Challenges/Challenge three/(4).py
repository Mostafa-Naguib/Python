# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of Rows and colums: "))


for i in range(1, n + 1):

    if i == 1 or i == n:
        print("*" * n)

    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*")
