import os
file = None
tries = 3
key = "#12131415#"

name = input("Enter the file's name: ").strip()

if name == "pass":
    print("""This file is encrypted\nSo you need to enter the file's password
\"BTW\"
you jus have 3 chances to try""")
    while tries > 0:
        password = input("Enter the file's password: ")
        if password != key:
            print(f"the file's password is incorrect\ntry again\n{tries} is left")
            tries -= 1
        else:
            file = open(r"C:\Users\moust\Desktop\pass.txt")
            print(file.read())
            break
    else:
        print("All chances are done...")
else:
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        file = open(name)
        print(file.read())

    except FileNotFoundError:
        print("The file is not found, Try again...")


if file is not None:
    file.close()
