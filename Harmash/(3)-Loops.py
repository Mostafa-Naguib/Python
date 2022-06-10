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


# here you can find how loops deal with dictionary
print("#" * 20, "loop and dictionary", "#" * 20)
print("=" * 10, "One dimensional dictionary", "=" * 10)
countries = {
    "China": "1.407.098",
    "India": "1.380.721",
    "USA": "331.893",
    "Indonesia": "275.122",
    "Pakistan": "238.181"
}

# print(countries["Pakistan"])

for x in countries:
    print(f"{x}: {countries[x]}")


# Two_dimensional_Dictionary
print("=" * 10, "Two dimensional dictionary", "=" * 10)
countries = {
    "England": {
        "Capital": "London",
        "Population": 9.5
    },
    "Germany": {
        "Capital": "Berlin",
        "Population": 3.5
    },
    "Japan": {
        "Capital": "Tokyo",
        "Population": 37
    },
    "Russia": {
        "Capital": "Moscow",
        "Population": 12
    }

}

# print(countries["Japan"])
# print(countries["Russia"]["capital"])

for x in countries:
    print(f"{x}:")
    for y in countries[x]:
        print(f"-{y} ==> {countries[x][y]}")
