def recursion(num):
    if num == 1:
        return 1
    else:
        # the first num is stash
        return num * recursion(num - 1)


print(recursion(5))
