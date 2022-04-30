# predfiened function
def function(num):
    return num * num


li = [1, 2, 3, 4, 5, 6, 7]

for x in map(function, li):
    print(x)

print("==========================")

for y in map(lambda num: num * num, li):
    print(y)
