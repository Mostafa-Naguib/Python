import datetime

print(dir(datetime))

print("=" * 200)

print(dir(datetime.datetime))

# whole date
print("=" * 50)
print(datetime.datetime.now())

# year
print("=" * 50)
print(datetime.datetime.now().year)

# month
print("=" * 50)
print(datetime.datetime.now().month)

# day
print("=" * 50)
print(datetime.datetime.now().day)


# min of the date
print("=" * 50)
print(datetime.datetime.min)

# max of the date
print(datetime.datetime.max)

# time
print("=" * 50)
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)

# min of the time
print("=" * 50)
print(datetime.time.min)

# max of the time
print(datetime.time.max)

datetime.datetime(2001, 10, 10)

born = datetime.datetime(2001, 10, 10)
DateTimeNow = datetime.datetime.now()

print(f"I have {int((( DateTimeNow - born).days)/365)}")


# ===================================
# Format date
# ===================================
myBirthday = datetime.datetime(2001, 10, 10)
print("=" * 20, "Without format", "=" * 20)
print(myBirthday)
print("=" * 20, "With format", "=" * 20)
print(myBirthday.strftime("%A / %B / %Y"))
