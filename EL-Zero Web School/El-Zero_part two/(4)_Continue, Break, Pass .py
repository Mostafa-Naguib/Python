# (Continue, Break, Pass)

AsianCounries = ["Palestine", "Jordan", "Israel", "Saudi Arabia", "Syria", "Iraq"]

for realCountries in AsianCounries:

    if realCountries == "Israel":
        continue

    print(realCountries)

print("=" * 33)


for realCountries in AsianCounries:

    if realCountries == "Israel":
        break

    print(realCountries)

print("=" * 33)


for realCountries in AsianCounries:

    if realCountries == "Israel":
        pass

    print(realCountries)
