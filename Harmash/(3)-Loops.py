# (1)while loop

x = 0

while x <= 100:
    print(f"{x}%")
    x += 1

else:
    print("Done.")

while False:
    print("Hello there.")

# Infinite Loop:
# while 1 == 1:
#    print("Stop!")

# ====================================
# (2)for loop

list = [1, 2, 3, 4, 5, 6, 7, 8]

for x in list:
    # print(x)

    if x % 2 == 0:
        print(f"{x} is even number")
    else:
        print(f"{x} is odd number")

else:
    print("And we're done")

allMyLove = "ELZamalek"

for letter in allMyLove:
    print(letter, end="")

# range
x = range(0, 101)

for number in x:
    print(number)

    # break
    if number == 99:
        break


AsianCounries = ["Palestine", "Jordan", "Israel", "Saudi Arabia", "Syria", "Iraq"]

for realCountries in AsianCounries:

    # continue => skip
    if realCountries == "Israel":
        continue

    print(realCountries)
