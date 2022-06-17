from module_1 import checker


def arabCountries(name):
    return checker(name)


list = ["Saudi Arabia", "Syria", "Iraq", "Germany", "Iran", "Turkey"]


for value in filter(arabCountries, list):
    print(value)
