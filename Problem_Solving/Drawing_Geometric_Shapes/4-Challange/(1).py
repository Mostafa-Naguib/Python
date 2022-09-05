# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    print("*" * (i - 1), end="")
    print(" ", end="")
    print("*" * (n - i))


# First Solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i == j:
            print(" ", end="")

        else:
            print("*", end="")

    print()
