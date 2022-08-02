# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

x = 1
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")

    for k in range(1, x + 1):
        print("*", end="")
    x += 2
    print()


# the first solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*", end="")
    print("*" * (i*2-2))


# the second solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n+1):

    for j in range(1, n-i+1):
        print(" ", end="")

    print("*", end="")
    for k in range(1, i*2-1):
        print("*", end="")

    print()


# the third solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))


i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print(" ", end="")
        j += 1
    k = 1
    print("*", end="")
    while k <= i*2-2:
        print("*", end="")
        k += 1
    i += 1
    print()
