hopes = {
    "Ahmed": {
        "First": "Football",
        "Second": "Video games",
        "Third": "Hiking"
    },
    "Mohamed": {
        "First": "Tennis",
        "Second": "Reading",
        "Third": "Walking"
    },
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

# print(hopes)
print(hopes["Ahmed"])
print(hopes["Mohamed"])
print(hopes["Mustafa"])
print(hopes["Yousef"])


for x in hopes:

    print(f"The hopes for {x} are: ")

    for y in hopes[x]:
        print(f"{y} => {hopes[x][y]}")
