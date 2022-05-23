li = [None] * 5  # or li = [Not Specified] * 5

li[0] = 'Mostafa'
li[1] = 20
li[2] = 'Student'
li[3] = 'Egypt'
li[4] = 'Muslim'

print(li)

li = [0, 2, 4, 6, 8, 10]

total = 0
for x in li:
    total += x
print(f"The total is {total}")

list = [12, 13, 14, 1345, 456]

del list[3]
del list[3]
del list[0:2]
del list

ID = ['Mostafa', 20, 'Student', 'Egypt', 'Muslim']
requerment = ID[0:2]
print(requerment)

li_1 = [0, 2, 4, 6, 8, 10]
li_2 = [1, 3, 5, 7, 9, 11]
total = li_1 + li_2
print(total)

# function:
print("=" * 10, "Function", "=" * 10)
# append(value)
print("=" * 20, "append()", "=" * 20)
countries = ["Egypt", "Saudi Arabia", "Palestine", "Italy", "South Korea"]
print(f"Now: {countries}")

countries.append("Syria")
print(f"Then: {countries}")

# extend(iterable)
print("=" * 20, "extend(iterable)", "=" * 20)
li_1 = [0, 2, 4, 6, 8, 10]
li_2 = [1, 3, 5, 7, 9, 11]

li_1.extend(li_2)  # default is Ascending
li_1.sort()
print(f"Ascending: {li_1}")
li_1.sort(reverse=True)
print(f"Descending: {li_1}")


# insert(index, obj)
print("=" * 20, "insert(index, obj)", "=" * 20)
fullName = ["Mostafa", "El-sayed", "Hassan"]
fullName.insert(1, "Naguib")
print(fullName)

# pop(index) "Remove a value form the list"
print("=" * 20, "pop(index)", "=" * 20)
number = [1, 2, 3, 4, 4, 5, 6]
print(number.pop(3))
print(number)

# remove(value)
print("=" * 20, "remove(value)", "=" * 20)
number = [1, 2, 3, 4, 4, 5, 6]
number.remove(4)
print(number)

# clear()
print("=" * 20, "clear()", "=" * 20)
number = [1, 2, 3, 4, 5, 6]
number.clear()
print(number)

# copy()
print("=" * 20, "copy()", "=" * 20)
number = [1, 2, 3, 4, 5, 6]
clone = number.copy()
print(clone)

# count(value)
print("=" * 20, "count(value)", "=" * 20)
number = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(number.count(1))

# index(value, strart, end) it gives the first value it can find
print("=" * 20, "index(value, start, end)", "=" * 20)
number = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(number.index(3, 0, 6))

# reverse()
print("=" * 20, "reverse()", "=" * 20)
number = [1, 2, 3, 4, 5, 6]
number.reverse()
print(number)

# ==============================================
# Function()
number = [1, 2, 3, 4, 5, 6]
print("=" * 20, "len()", "=" * 20)
print(len(number))
print("=" * 20, "min()", "=" * 20)
print(min(number))
print("=" * 20, "max()", "=" * 20)
print(max(number))
