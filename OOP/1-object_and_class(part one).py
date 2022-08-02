class num:
    x = 5


# any object has unique properties
o1 = num()
o2 = num()

o1.x = 100
o2.x = 101

print(f'o1 = {o1.x}')
print(f'o2 = {o2.x}')

# =======================================================================================


class Salary:
    value = 0

    def print_the_salary(self):
        print(f"Your salary is: {self.value}")

    def print_net_salary(self, rate):
        taxes = self.value / rate
        print(f"Your net salary is: {self.value-taxes}")


an_employee = Salary()

an_employee.value = 15000

an_employee.print_the_salary()

an_employee.print_net_salary(10)
