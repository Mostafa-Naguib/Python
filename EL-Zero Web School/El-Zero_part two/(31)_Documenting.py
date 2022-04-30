def greeting(name):
    ''' This function is just for greeting people when they log in '''
    return f"Hello {name} \nWolcome to our website..."


print(greeting(input("Enter your name: ")))

print(dir(greeting))

print(greeting.__doc__)

help(greeting)
