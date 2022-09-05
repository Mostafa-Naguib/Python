# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))


for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i <= int(n / 2) and j > int(n / 2) + 1 or i > int(n / 2) + 1 and j <= int(n / 2):
            print(" ", end="")

        else:
            print("*", end="")

    print()


# The first solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))


for i in range(1, n + 1):

    if i <= n / 2:
        print("*" * (int(n / 2) + 1), end="")
        print(" " * int(n / 2), end="")

    elif i == int(n / 2) + 1:
        print("*" * n, end="")

    else:
        print(" " * int(n / 2), end="")
        print("*" * (int(n / 2) + 1), end="")

    print()
