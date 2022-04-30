x = input("Enter our name:").capitalize()

if x.startswith("Mr"):
    raise Exception("This isn't the right place to sign in..")

else:
    print(f"Wecome {x}")
