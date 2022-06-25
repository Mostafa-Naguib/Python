"""
This function is for calculate factorial number
"""


def factorial(num):
    """Calculate factorial number"""
    if num == 1:
        return 1
    return num * factorial(num - 1)
