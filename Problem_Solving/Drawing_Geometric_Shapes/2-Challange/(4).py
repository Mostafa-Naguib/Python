# my own solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, round(n/2)+1):
    print("*" * i)

for j in range(int(n/2)+1, n+1):
    print("*" * (n-j+1))


# the first solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    if i <= n/2:
        print("*" * i, end="")

    else:
        print("*" * (n-i+1), end="")

    print()

# the fifth solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

for i in range(1, round(n/2)+1):
    print("*" * i)

for j in range(1, round(n/2)+2):
    print("*" * (int(n/2) - j + 2))


# the sixth solution...
n = 0
while n <= 0 or n % 2 == 0:
    n = int(input("Enter the number of lines: "))

i = 1
while(i <= int(n/2)):

    j = 1
    while(j <= i):
        print("*", end="")
        j += 1

    print()
    i += 1

k = 1
while(k <= int(n/2)+1):

    o = 1
    while(o <= (int(n/2)-k+2)):
        print("*", end="")
        o += 1

    print()
    k += 1
