test = [1, 2, 3, 4, 5]
print(test)
print(*test)

print("=" * 44)

def hopes(name, *HOPES):
    print(f"Hello {name} your hopes are:")
    for x in HOPES:
        print(f"-{x}")



hopes("Mostafa", "Football", "Video games", "Reading", "Learning")
