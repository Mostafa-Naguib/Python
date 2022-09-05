# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

    if n % 2 == 0:
        n += 1


for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i == 1 or i == n or j == 1 or j == n or j == i or j == n - i + 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()
