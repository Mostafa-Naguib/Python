# Range:

X = range(100, 201)

for number in X:
    print(number)

print("=" * 78)

countries = {
    "China": "1.407.098",
    "India": "1.380.721",
    "USA": "331.893",
    "Indonesia": "275.122",
    "Pakistan": "238.181"
}

# print(countries["China"])
# print(countries.get("Pakistan"))


for country in countries:
    print(f"The population of {country} is {countries[country]}")
