dict = {
    "FN": "Mostafa",
    "SN": "Naguib",
    "LN": "El-sayed"
}
# just show the function:
print(dict)
# index...
print(dict["FN"])
# get()
print(dict.get("SN"))
# len()
print(len(dict))
# add a key and value
dict["NickName"] = "Darsh"
# Searching for a key...
print("LN" in dict)
# Using "For Loop"...
for key in dict:
    print(f"{key}: {dict[key]}")
# For deleting:
del dict["NickName"]
del dict

# Function (class)
print("=" * 10, "1-Function", "=" * 10)
# clear()
print("=" * 20, "clear()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
A_Student.clear()
print(A_Student)

# copy()
print("=" * 20, "copy()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
clone = A_Student.copy()
print(clone)

# popitem()
print("=" * 20, "popitem()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
print(A_Student)
A_Student.popitem()
print(A_Student)

# pop()
print("=" * 20, "pop()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
print(A_Student)
print(A_Student.pop("Faculty", "There's an error"))
print(A_Student)

# keys(), Values()
print("=" * 20, "keys(), Values()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
print(A_Student.keys())
print(A_Student.values())

# items()
print("=" * 20, "items()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
print(A_Student.items())

# fromkeys()
print("=" * 20, "fromkeys()", "=" * 20)
tuple = ("First", "Second", "Third")
print(dict.fromkeys(tuple, "Not Defened"))

# setdefault()
print("=" * 20, "setdefault()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
print(A_Student.setdefault("Faculty"))
A_Student.setdefault("Religion", "Muslim")
print(A_Student)

# update()
print("=" * 20, "update()", "=" * 20)
A_Student = {
    "Name": "Mostafa",
    "Age": 20,
    "Faculty": "Agriculture",
}
A_Student.update({"Name": "Mostafa Naguib"})
print(A_Student)


# ===================================================
print("=#" * 10, "Two_dimensional_Dictionary", "#=" * 10)
countries = {
    "England": {
        "capital": "London",
        "population": 8.9
    },
    "Germany": {
        "capital": "Berlin",
        "population": 3.5
    },
    "Japan": {
        "capital": "Tokyo",
        "population": 13.96
    },
    "Russia": {
        "capital": "Moscow",
        "population": 11.9
    }

}

print(countries)
