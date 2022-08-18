from person import Person


class Employee(Person):

    def __init__(self, name, age, specialization):

        super().__init__(name, age)

        self.specialization = specialization

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Specialization: {self.specialization}")
