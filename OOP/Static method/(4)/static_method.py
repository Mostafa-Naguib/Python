class StaticMethod:

    x = 99

    @staticmethod
    def print_info():
        print(f"The number is: {StaticMethod.x}")
