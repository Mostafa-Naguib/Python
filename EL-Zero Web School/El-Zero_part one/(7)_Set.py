# Sets
# Set Items are not ordered and not indexed
# Set indexing and slicing can't be done
# Set has immutable data type(Numbers, String, Tuples) List & Dict aren't

MyFirstSet = {7, 3.14, (1, 2, 3, 4), False}
print(MyFirstSet)

# Items in Sets are unique
Test = {1, 2, 3, 4, 4, 4}
print(Test)


print("\n@#$___________________________________________________@#$\n")

# clear()
Test = {1, 2, 3, 4, 5}
Test.clear()
print(Test)
print("=" * 35)

# union()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 3}
Test3 = {"Ukraine", 2, "Russia", 4, True}
print(Test1 | Test2)
print(Test1.union(Test2, Test3))
print("=" * 35)

# add()
Test = {1, 2, 3, 4, 5}
Test.add(1000)
print(Test)
print("=" * 35)

# copy()
# Shallow copy
Test = {1, 2, 3, 4, 5}
X = Test.copy()
print(X)
print("=" * 35)

# remove()
Test = {1, 2, 3, 4, 5}
Test.remove(3)
print(Test)
print("=" * 35)

# discard()
Test = {1, 2, 3, 4, 5}
Test.discard(1)
print(Test)
Test.discard(49)
print(Test)
print("=" * 35)

# pop()
Test = {1, 2, 3, 4, 5}
print(Test.pop())
print("=" * 35)

# update()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
Test4 = ["A", "B", "C", "D"]
Test1.update(Test4)
Test1.update(Test2)
print(Test1)
print("=" * 35)

# difference()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
print(Test1.difference(Test2))
print(Test1)
print("=" * 35)

# difference_update
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
Test2.difference_update(Test1)
print(Test2)
print("=" * 35)

# intersection()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
print(Test1.intersection(Test2))
print(Test1)
print("=" * 35)

# intersection_update()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
Test1.intersection_update(Test2)
print(Test1)
print("=" * 35)

# symmetric_difference()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
print(Test1.symmetric_difference(Test2))
print(Test1)
print("=" * 35)

# symmetric_difference_update()
Test1 = {1, 2, 3, 4, 5}
Test2 = {"One", "Two", "Three", "Four", "Five", 1, 2}
print(Test1)
Test1.symmetric_difference_update(Test2)
print(Test1)
print("=" * 35)


# isSuperSet()
Test1 = {1, 2, 3, 4, 5, 32}
Test2 = {1, 2, 3, 4, 5}
Test3 = {1, 2, 3, 4, 55}
print(Test1.issuperset(Test2))
print(Test1.issuperset(Test3))
print("=" * 35)

# isSubSet()
Test1 = {1, 2, 3, 4, 5}
Test2 = {1, 2, 3, 4, 5, 33, 44}
Test3 = {1, 2, 3, 4, 55}
print(Test1.issubset(Test2))
print(Test1.issubset(Test3))
print("=" * 35)

# isDisJoint()
Test1 = {1, 2, 3, 4, 5}
Test2 = {1, 2, 3, 4, 5, 33, 44}
Test3 = {100, 101, 109, 111}
print(Test1.isdisjoint(Test2))
print(Test1.isdisjoint(Test3))
