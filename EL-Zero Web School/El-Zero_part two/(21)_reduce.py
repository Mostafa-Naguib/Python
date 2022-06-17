from functools import reduce
import module_2 as x


def sum(num1, num2):
    return num1 + x.factorial(num2)


tuple = (1, 2, 3, 4)
result = reduce(sum, tuple)
print(result)

# -------------------------------lambda function-------------------------------------
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

result = reduce(lambda num1, num2: num1 + num2, tuple)
print(result)
