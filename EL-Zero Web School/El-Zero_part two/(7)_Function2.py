
def greeting(fName, lName):
    print(f"Hello {fName.capitalize().strip()} {lName.capitalize():.1s}")


greeting(input("Enter your first name: "), input("Enter your second name: "))


print("=" * 34)


def multiplication(n1, n2):
    x = int(n1) * int(n2)
    print(f"{n1} * {n2} = {x}")


multiplication(input("Enter the first number: "), input("Enter the second number: "))
