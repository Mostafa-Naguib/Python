list1 = ["A", "B", "C", "D", "E", "F", "G"]
list2 = [1, 2, 3, 4]
tuple1 = ("planet", "continent", "country", "city")
dict1 = {"country": "Egypt", "language": "Arabic", "religion": "Islam"}


for x in zip(list1, list2, tuple1, dict1):
    print(x)

print("#" * 44)
