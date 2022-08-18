# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

    if n % 2 == 0:
        n += 1

for i in range(1, n + 1):
    if i <= int(n/2):
        print("*" * (i - 1), end="")
        print(" ", end="")
        print("*" * (n - i * 2), end="")
        print(" ", end="")
        print("*" * (i - 1))

    elif i == int(n / 2) + 1:
        print("*" * (i - 1), end="")
        print(" ", end="")
        print("*" * (i - 1))

    else:
        print("*" * (n - i), end="")
        print(" ", end="")
        print("*" * (i * 2 - n - 2), end="")
        print(" ", end="")
        print("*" * (n - i))


# the first solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

    if n % 2 == 0:
        n += 1


for i in range(1, n + 1):

    for j in range(1, n + 1):

        if j == i or j == n - i + 1:
            print(" ", end="")

        else:
            print("*", end="")

    print()
