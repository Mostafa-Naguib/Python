# Dictionary
# Dict items are contains key : value
# Dict "key" need to be immutable=>(String, Numbers, Tuples) Lists aren't allow
# Dict key need to be unique
# Dict "value" can have any data types


A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "faculty": "Agriculture",
    "My favorite years": [1911, 1973, 1999, 2001],
    ("Egypt", "Palestine", "Syria"): "are my favorite countries",
    "Name": "Mostafa naguib"
}

print(A_Student)
print(A_Student.keys())
print(A_Student.values())
print(A_Student["Age"])
print(A_Student.get("Age"))
print("-" * 80)

# Two_dimensional_Dictionary

countries = {
    "England": {
        "Capital": "London",
        "Population": 8.9
    },
    "Germany": {
        "Capital": "Berlin",
        "Population": 3.5
    },
    "Japan": {
        "Capital": "Tokyo",
        "Population": 13.96
    },
    "Russia": {
        "Capital": "Moscow",
        "Population": 11.9
    }

}

print(countries)
print(countries["Germany"])
print("I'm hoping in future to visit {}" .format(countries["England"]["Capital"]))
print(len(countries))
print(len(countries["England"]))


Germany = {
    "Capital": "Berlin",
    "Population": 3.5
}
Japan = {
    "Capital": "Tokyo",
    "Population": 13.96
}
Egypt = {
    "Capital": "Cairo",
    "Population": 9.8
}

All_Countries = {
    "European_countrry": Germany,
    "Asian_countrry": Japan,
    "African_countrry": Egypt
}

print(All_Countries)


print("\n@#$___________________________________________________@#$\n")
# methods

# clear()
A_Student = {
    "Name": "mostafa",
    "Age": 20,
    "faculty": "Agriculture"
}
A_Student.clear()
print(A_Student)
print("=" * 35)


# Update()
A_Student = {"Name": "mostafa", "Age": 20, "faculty": "Agriculture", "Nationality": "Egyption"}
A_Student.update({"Religion": "Muslim"})
print(A_Student)
print("=" * 35)

# copy()
# Shallow copy
A_Student = {
    "Name": "mostafa",
    "Age": 20,
    "faculty": "Agriculture"
}
X = A_Student.copy()
print(X)
A_Student.update({"Language": "Arabic"})
print(A_Student)
print(X)
print("=" * 35)


# SetDefault()
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "faculty": "Agriculture"
}
print(A_Student.setdefault("religion", "Muslim"))
print(A_Student)
print("=" * 35)

# popitem()
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "faculty": "Agriculture"
}
print(A_Student.popitem())  # last item
print("=" * 35)

# items()
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "faculty": "Agriculture"
}
All_Info = A_Student.items()
A_Student["Qualities"] = "Patient"
print(All_Info)
print("=" * 35)

# fromkeys()
X = ("Egypt", "Morocco", "Comoros")
Y = "An African country"
print(dict.fromkeys(X, Y))
