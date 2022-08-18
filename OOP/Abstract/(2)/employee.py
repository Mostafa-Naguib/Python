from person import Person


class Employee(Person):

    def __init__(self, name, gender, birthday, is_married, salary):

        super().__init__(name, gender, birthday, is_married)

        self.salary = salary

    def print_info(self):
        print("=" * 50)
        print(f"name: {self.name}")
        print(f"gender: {self.gender}")
        print(f"birthday: {self.birthday}")
        print(f"Is_married: {self.is_married}")
        print(f"salary: {self.salary}")
        print("=" * 50)
