# Type conversion

# str()
X = 5
print(type(X))
print(type(str(X)))
print("=" * 40)

# list()

X = "Zamalek"
Y = (11, 22, 33, 44, 55)
Z = {99, 88, 77, 66, 55}
K = {"Egypt": 104, "Saudi Arabia": 40}
print(list(X))
print(list(Y))
print(list(Z))
print(list(K))
print("=" * 40)


# tuple()

X = "Zamalek"
Y = [11, 22, 33, 44, 55]
Z = {99, 88, 77, 66, 55}
K = {"Egypt": 104, "Saudi Arabia": 40}
print(tuple(X))
print(tuple(Y))
print(tuple(Z))
print(tuple(K))
print("=" * 40)


# set()

X = "Zamalek"
Y = [11, 22, 33, 44, 55]
Z = (99, 88, 77, 66, 55)
K = {"Egypt": 104, "Saudi Arabia": 40}
print(set(X))
print(set(Y))
print(set(Z))
print(set(K))
print("=" * 40)


# dict()

Y = [["Egypt", "Cairo"], ["Australia", "Canberra"], [
    "Netherland", "Amsterdam"], ["Belgium", "Brussels"]]
Z = (("One", 1), ("Two", 2), ("Three", 3), ("Four", 4))
# can't convert sets
print(dict(Y))
