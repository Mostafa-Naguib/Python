number_of_line = int(input("Eter the number of line: "))

i = 1
while i <= number_of_line:
    z = 1
    while z <= i:
        print("*", end="")
        z = z + 1
    print("\n")
    i = i + 1
