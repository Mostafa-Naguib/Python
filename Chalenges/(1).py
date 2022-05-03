# My own solution...
n = 0
while n <= 0:
    n = int(input("Eter the number of line: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

# First solution....
print("#" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number line: "))

for i in range(1, n+1):
    print("*" * i)

# Second solution...
print("#" * 50)

n = 0
while n <= 0:
    n = int(input("Enter the number line: "))

for i in range(1, i+1):
    for j in range(1, i+1):
        print("*", end="")

    print("")
