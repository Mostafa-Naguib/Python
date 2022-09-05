# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):

    print("0" * (i - 1), end="")
    print("*", end="")
    print("1" * (n - i))


# The first solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if j > i:
            print("0", end="")

        elif j == i:
            print("*", end="")

        else:
            print("1", end="")

    print()
