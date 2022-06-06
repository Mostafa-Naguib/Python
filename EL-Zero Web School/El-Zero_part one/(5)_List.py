# Lists

myList = ["Egypt", "El-Zamalek", 1973, 1911, "Sinai"]

# Index
print("{0:s} recaptured {2:s} from Zionist in {1:d} " .format(myList[0], myList[2], myList[-1]))

# Slice
print(myList[0:5:2])


print("\n@#$___________________________________________________@#$\n")

# methods

# append()
Years = [1911, 1975, 1949, 1992, 1999]
Countries = ["El-Zamalek", "Microsoft", "China", "Amazon"]
Years.append(1918)
Years.append("Cairo")
Years.append(Countries)
print(Years)
print("My favorite club is " + Countries[0])

# extend()
Countries = ["Canada", "Brazil", "Belgium", "Greece"]
Capitals = ["Ottawa", "Brasília", "Brussels", "Athens"]
Countries.extend(Capitals)
print(Countries)

# remove()
Numbers = [5, 3, 1, 4, 6, 2, 4]
Numbers.remove(4)
print(Numbers)

# sort()
Numbers = [5, 3, 1, 4, 6, 2, 4]
Numbers.sort()
print(Numbers)  # Ascend
Numbers.sort(reverse=True)
print(Numbers)  # descend

# reverse()
Numbers = [5, 3, 1, 4, 6, 2, 4]
Numbers.reverse()
print(Numbers)

# clear()
Numbers = [5, 3, 1, 4, "mostafa", 6, 2, 4]
Numbers.clear()
print(Numbers)

# copy(Deep Copy)
V = [11, 22, 33, 44, 55, 66]
X = V.copy()
print(X)

V.append(77)
C = V.copy()

print(V)
print(C)

# count()
X = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
print(X.count(1))

# index()
Countries = ["Canada", "Brazil", "Belgium", "Greece"]
print(Countries.index("Belgium"))

# insert()
Countries = ["Canada", "Brazil", "Belgium", "Greece"]
Countries.insert(-2, "Netherland")
print(Countries)

# pop()
Countries = ["Canada", "Brazil", "Belgium", "Greece"]
print(Countries.pop(-1))
print(Countries)
