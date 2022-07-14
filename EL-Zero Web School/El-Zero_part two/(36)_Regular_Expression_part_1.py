import re

# search() --> "return the first match only"

my_name = re.search("[A-Z]", "Mostafa")

print(my_name)
print(my_name.string)
print(my_name.span())
print(my_name.group())


print("=" * 50)
email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|org|net|info)", "mostafanaguib200gmail.com")

if email:
    print("This is a valid Email...")

else:
    print("This isn't a valid Email...")


# findall() --> "return a list of all matches and empty list if there's no match"
print("=#" * 50)
phone_number = re.findall(r"\d{3}\s|\d{3}-\d{4}\s|\d{4}-\d{4}|\d{4}",  "010 1602 5695")

print(phone_number)

if phone_number != []:
    print("a valid phone number...")

else:
    print("an unvalid phone number...")
