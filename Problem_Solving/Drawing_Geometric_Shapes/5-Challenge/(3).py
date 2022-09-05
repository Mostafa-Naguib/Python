# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))


for i in range(1, n + 1):

    if i <= int(n / 2):

        for j in range(1, n + 1):

            if i == 1 and j >= int(n / 2) + 1 or j == int(n / 2) + 1 or j == n:
                print("*", end="")

            else:
                print(" ", end="")

    elif i == int(n / 2) + 1:
        print("*" * n, end="")

    else:
        for j in range(1, n + 1):

            if j == 1 or j == int(n / 2) + 1 or j <= int(n / 2) + 1 and i == n:
                print("*", end="")

            else:
                print(" ", end="")

    print()
