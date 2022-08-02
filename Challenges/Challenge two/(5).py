# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, round(n/2) + 2):
    print(" " * (round(n/2) - i + 1), end="")
    print("*" * i)

for j in range(round(n/2) + 1, n + 1):
    print(" " * (j-round(n/2)), end="")
    print("*" * (n - j))

# the first solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n+1):

    if (i <= int(n/2)):
        print(" " * (int(n/2) - i + 1), end="")
        print("*" * i)
    else:
        print(" " * (i - int(n/2) - 1), end="")
        print("*" * (n - i + 1))
