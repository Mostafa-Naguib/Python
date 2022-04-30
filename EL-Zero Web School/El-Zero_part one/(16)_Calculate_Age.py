
print(" Welcom to our new website.".center(90, "@"))

age = int(input("Enter your age: ").strip())
unit = input("Which unit do you want to conver to it: ").strip().lower()


if unit == "month":
    month = age * 12
    print(f"You choosed {unit}. ")
    print("So, you lived ", str(month))

elif unit == "week":
    month = age * 12
    week = month * 4
    print(f"You choosed {unit}. ")
    print("So, you lived ", str(week))

elif unit == "day":
    day = age * 365
    print(f"You choosed {unit}. ")
    print("So, you lived ", str(day))

else:
    print("Somthing's wrong \nTry again")
