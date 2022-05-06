# if, elif, else

email = input("Enter your email: ").strip()
country = input("Where are you from: ").strip().capitalize()

userName = email[:email.index("@")]
pEnlish_Course = 100
student = True

if country == "Egypt" or country == "Syria" or country == "Palestine":
    print(f"Welcome {userName} to our English course because you're coming from {country}")

    if student is True:
        print(f"You'll just pay: {pEnlish_Course-95}")
    else:
        print(f"You'll just pay: {pEnlish_Course-90}")

elif country == "Italy" or country == "Greece" or country == "England":
    print(f"Welcome {userName} to our English course because you're coming from {country}")
    print(f"You'll just pay: {pEnlish_Course-40}")

elif country == "Taiwan" or country == "South Korea" or country == "China":
    print(f"Welcome {userName} to our English course because you're coming from {country}")
    print(f"You'll just pay: {pEnlish_Course-50}")

else:
    print(f"Welcome {userName} to our English course because you're coming from {country}")
    print(f"You'll just pay: {pEnlish_Course-25}")
