# First Solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * i, end="")
    print()


# second Solution...
print("#" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end="")
    print()

# Third Solution...
print("#" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))
i = 1

while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= i:
        print("*", end="")
        k += 1
    i += 1
    print()
