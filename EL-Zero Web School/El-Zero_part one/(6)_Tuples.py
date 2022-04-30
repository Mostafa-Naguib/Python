# Tuples

Arab_Countries = ("Palestine", "Egypt", "Lybia", "Qatar")
European_Countries = "Italy", "England", "Germany", "Greece"
print(Arab_Countries)
print(European_Countries)

print("My favorite country in the arab world " + Arab_Countries[0])
print("My favorite country in Europe " + European_Countries[3])


# Tuples are immutable=>You can't change it.....


X = ("Mostafa")
Y = "mostafa",
print(type(X))
print(type(Y))
print(len(X))
print(len(Y))


# Concatenation
Arab_Countries = ("Palestine", "Egypt", "Lybia", "Qatar")
Europe_Countries = "Italy", "England", "Germany", "Greece"
The_World = Arab_Countries + Europe_Countries
print(The_World)


# Repeat " * "
X = ("Mostafa",)
print(X * 5)


print("\n@#$___________________________________________________@#$\n")


# count()
A = (1, 2, 3, 4, 5, 5, 5, 6, 7)
print(A.count(5))

# index()
A = (1, 2, 3, 4, 5, 5, 5, 6, 7)
print("The position of the index is {:d}" .format(A.index(5)))


# Destruct()
Numbers = (1, 2, 0, 3)
A, B, _, C = Numbers

print(A)
print(B)
print(C)
