# Practical Slice Email


fName = input("Enter your name: ").strip().capitalize()
email = input("Enter your email: ").strip().capitalize()

userName = email[:email.index("@")]
domain = email[email.index("@"):]

print(f"Hello {userName}. \nThe domain is {domain}")
