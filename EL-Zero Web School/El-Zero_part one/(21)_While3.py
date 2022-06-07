
Correct_password = "python12345"

X = input("Please, Enter your password: ")

Tries = 5

while X != Correct_password:
    print(
        f"Incorrect password \nYou have {'last chance' if Tries == 1 else  f'{Tries} chances'} to try")
    X = input("Please, Enter your password again: ")
    Tries -= 1

    if Tries == 0:
        print("All chances are gone")

        break

else:
    print("Correct Password")
