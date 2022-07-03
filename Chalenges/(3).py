# My Own Solution....
n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))


for i in range(1, n + 1):
    print("*" * ((n+1) - i))

# The first solution...
print("=" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))

for i in range(1, n+1):
    for j in range(1, (n+2)-i):
        print("*", end="")
    print()

# The second solution...
print("=" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number of line: "))

i = 1
while i <= n:
    j = 1
    while j <= n+1 - i:
        print("*", end="")
        j += 1
    print()
    i += 1
