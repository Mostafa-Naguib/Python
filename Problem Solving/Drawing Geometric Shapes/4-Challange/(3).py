# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

    if n % 2 == 0:
        n += 1

i = 1
while i <= n:

    j = 0
    while j <= n:

        if j == i or j == n - i + 1:
            print("*", end="")

        else:
            print(" ", end="")

        j += 1
    i += 1
    print()
