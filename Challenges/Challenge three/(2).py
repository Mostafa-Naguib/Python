# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))


print(" " * (int(n / 2)), end="*\n")

for i in range(2, int(n / 2) + 2):
    print(" " * (int(n / 2) - i + 1), end="")
    print("*", end="")
    print(" " * (i * 2 - 3), end="")
    print("*" * (i + 1 - i))

for j in range(2, int(n / 2) + 1):
    print(" " * (j - 1), end="")
    print("*", end="")
    print(" " * (n - j * 2), end="")
    print("*")

print(" " * (int(n / 2)), end="*\n")


# the first solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):

    if i <= n / 2:
        print(" " * (int(n/2) - i + 1), end="")
        print("*", end="")
        print(" " * (i * 2 - 3), end="")

        if i != 1:
            print("*", end="")

    else:
        print(' ' * (i - int(n / 2) - 1), end='')
        print('*', end='')
        print(' ' * ((n * 2) - (i * 2) - 1), end='')

        if i != n:
            print("*", end="")

    print()
