

def Recursion(number):

    print(number)
    if len(number) == 1:
        return number

    if number[0] == number[1]:
        return Recursion(number[1:])

    return number[0] + Recursion(number[1:])


print(Recursion("111222333444555"))
