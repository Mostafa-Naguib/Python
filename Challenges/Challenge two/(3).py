# my own solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

i = n
while i >= 1:
    j = 1
    while j <= (n-i):
        print(" ", end="")
        j += 1
    k = 1
    while k <= i*2-1:
        print("*", end="")
        k += 1
    i -= 1
    print()

# the first solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

    for i in range(1, n+1):
        print(" " * (i-1), end="")
        print("*" * ((n*2)-(i*2-1)))


# the second solution...
n = 0
while n <= 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n+1):

    for j in range(1, i):
        print(" ", end="")

    for k in range(1, (n*2)-(i*2-1)+1):
        print("*", end="")

    print()
