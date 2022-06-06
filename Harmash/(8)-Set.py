# the items in the sets are unique
set = {1, 2, 3, 4, (1, 3, 4, 7), 5, 6, 7, 7, 8}
print(set)
# del set
print(0 in set)

# Function (class)
print("=" * 10, "1-Function", "=" * 10)
# add()
print("=" * 20, "add()", "=" * 20)
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
numbers.add(0)
print(numbers)

# discard() It doesn't give error when it doesn't find the exact value...
print("=" * 20, "discard()", "=" * 20)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 546}
print(numbers)
numbers.discard(546)
print(numbers)

# remove() It gives error when it doesn't find the exact value...
print("=" * 20, "remove()", "=" * 20)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 546}
print(numbers)
numbers.remove(546)
print(numbers)
# numbers.remove(3456)

# clear()
print("=" * 20, "clear()", "=" * 20)
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
numbers.clear()
print(numbers)

# pop() delete random value
print("=" * 20, "pop()", "=" * 20)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 55}
print(numbers)
print(numbers.pop())
print(numbers)

# copy(shallow)
print("=" * 20, "copy()", "=" * 20)
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Base_10 = numbers.copy()
print(Base_10)

# difference()
print("=" * 20, "difference()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
print(set_1.difference(set_2))  # set_1 - set_2

# difference_update()
print("=" * 20, "difference_update()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
set_1.difference_update(set_2)
print(set_1)

# intersection()
print("=" * 20, "intersection()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
print(set_1.intersection(set_2))  # set_1 & set_2

# intersection_update()
print("=" * 20, "intersection_update()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
set_1.intersection_update(set_2)
print(set_1)

# symmetric_difference()  # it gives the differences between two sets
print("=" * 20, "symmetric_difference()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
print(set_2.symmetric_difference(set_1))  # set_1 ^ set_2

# symmetric_difference_update()
print("=" * 20, "symmetric_difference_update()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, "y", 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5, "X"}
set_1.symmetric_difference_update(set_2)
print(set_1)

# union()
print("=" * 20, "union()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {10, 11, 12, 13, 14, 15}
set_3 = {16, 11, 12, 13, 14, 15}
NewSet = set_1.union(set_2, set_3)
print(set_1 | set_2 | set_3)
print(NewSet)

# Update()
print("=" * 20, "update()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {10, 11, 12, 13, 14, 15}
set_3 = {16, 11, 12, 13, 14, 15}
set_1.update(set_2, set_3)
print(set_1)

# isdisjoint()
print("=" * 20, "isdisjoint()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {11, 12, 13, 14, 15}
set_3 = {0, 11, 12, 13, 14, 15}
print(set_1.isdisjoint(set_2))
print(set_1.isdisjoint(set_3))

# issuperset()
print("=" * 20, "issuperset()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5}
set_3 = {0, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15}
print(set_1.issuperset(set_2))
print(set_1.issuperset(set_3))

# issubset()
print("=" * 20, "issubset()", "=" * 20)
set_1 = {0, 1, 2, 3, 4, 5, 6}
set_2 = {0, 1, 2, 3, 4, 5}
set_3 = {0, 1, 2, 3, 4, 5, 6, 11, 12}
print(set_1.issubset(set_2))
print(set_1.issubset(set_3))
