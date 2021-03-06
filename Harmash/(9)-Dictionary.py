# Dict "key" need to be immutable=>(String, Numbers, Tuples) Lists aren't allow
# Dict key need to be unique
# Dict "value" can have any data types

dict = {
    "FN": "Mostafa",
    "SN": "Naguib",
    "LN": "El-sayed",
    "LN": "Dawod",
    20: "is my age",
    ("Egypt", "Palestine", "Syria"): "are my favorite countries",
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

# copy(shallow copy)
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

# items()
print("=" * 20, "items()", "=" * 20)
a_student = {
    "Name": "mostafa",
    "Age": 20,
    "faculty": "Agriculture",
    "My favorite years": [1911, 1973, 1999, 2001],
    ("Egypt", "Palestine", "Syria"): "are my favorite countries",
    "Name": "Mostafa naguib"
}

# print(a_student.items())
for key, value in a_student.items():
    print(f"{key}==> {value}")

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

# print(countries)
# print(countries["Russia"])
# print(countries["Russia"]["capital"])

# items()
print("=" * 20, "items()", "=" * 20)
# print(countries.items())

for key, value in countries.items():
    print(f"{key} ==> ")
    for key, value in value.items():
        print(f"{key}: {value}")
    print("-" * 22)

# type conversoin
# dict()
print("=" * 20, "dict()", "=" * 20)
Y = [["Egypt", "Cairo"], ["Australia", "Canberra"], [
    "Netherland", "Amsterdam"], ["Belgium", "Brussels"]]
Z = (("One", 1), ("Two", 2), ("Three", 3), ("Four", 4))
# can't convert sets
print(dict(Y))
print(dict(Z))
