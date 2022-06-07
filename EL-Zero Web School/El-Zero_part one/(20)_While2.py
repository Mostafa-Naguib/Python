Arab_World = []
North_Africa = ["Egypt", "libya", "Morocco", "Algeria", "Tunisia", "Mauritania", "Sudan"]
Gulf = ['Saudi Arabia', "UAE", "Bahrain", "Oman", "Kuwait", "Qatar", "Iraq"]
Levant_Country = ["Palestine", "Jordan", "Lebanon", "Syria"]
Other = ["Yemen", "Comoros", "Somalia", "Djibouti"]

x = (len(North_Africa) + len(Gulf) + len(Levant_Country) + len(Other))
print(f"Welcom to \"The Arab World\" \nWe're {x} Arab countries.\
     \nAnd here they are:")


Arab_World.extend(North_Africa)
Arab_World.extend(Gulf)
Arab_World.extend(Levant_Country)
Arab_World.extend(Other)

n = 0

while n < x:
    print(f"{str(n+1).zfill(2)}- {Arab_World[n]}")
    n += 1

choose = input("Choose which the country would you like to visit: ").strip().capitalize()
print(f"You're welcome to {choose} at any given time.")
