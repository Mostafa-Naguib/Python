# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, int(n/2)+2):
    print(" " * (int(n/2) - i + 1), end="")
    print("*" * (i * 2 - 1))

for j in range(1, int(n/2)+1):
    print(" " * j, end="")
    print("*" * (n - j * 2))


# the first solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):

    if i <= int(n/2):
        print(" " * (int(n/2) - i + 1), end="")
        print("*" * (i * 2 - 1))

    else:
        print(" " * (i - (int(n/2) + 1)))
        print("*" * (i-1 * 2) + 2)
