A_Student = {
    "Name": "mostafa",
    "Age": 20,
    "faculty": "Agriculture",
    "My favorite years": [1911, 1973, 1999, 2001],
    ("Egypt", "Palestine", "Syria"): "are my favorite countries",
    "Name": "Mostafa naguib"
}


# print(A_Student.items())


for X, Y in A_Student.items():
    print(f"{X} => {Y}")


print("=" * 50)

hopes = {
    "Mustafa": {
        "First": "Handball",
        "Second": "Photographer",
        "Third": "Swimming"
    },
    "Yousef": {
        "First": "Basketball",
        "Second": "Drawing",
        "Third": "Skiing"
    },

}


for mainKey, mainValue in hopes.items():
    print(f"{mainKey}'s hopes => ")

    for secondKey, secondValue in mainValue.items():
        print(f"{secondKey}: {secondValue}")

    print("-" * 22)
