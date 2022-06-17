Arab_World = []
North_Africa = ["Egypt", "libya", "Morocco", "Algeria", "Tunisia", "Mauritania", "Sudan"]
Gulf = ['Saudi Arabia', "UAE", "Bahrain", "Oman", "Kuwait", "Qatar", "Iraq"]
Levant_Country = ["Palestine", "Jordan", "Lebanon", "Syria"]
Other = ["Yemen", "Comoros", "Somalia", "Djibouti"]

x = (len(North_Africa) + len(Gulf) + len(Levant_Country) + len(Other))

Arab_World.extend(North_Africa)
Arab_World.extend(Gulf)
Arab_World.extend(Levant_Country)
Arab_World.extend(Other)


def checker(name):
    i = 0
    while i < x:
        if name == Arab_World[i]:
            return name
        i += 1
