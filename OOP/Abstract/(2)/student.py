from person import Person


class Student(Person):

    def __init__(self, name, gender, birthday, is_married, specialization):

        super().__init__(name, gender, birthday, is_married)

        self.specialization = specialization

    def print_info(self):
        print("=" * 50)
        print(f"name: {self.name}")
        print(f"gender: {self.gender}")
        print(f"birthday: {self.birthday}")
        print(f"Is_married: {self.is_married}")
        print(f"specialization: {self.specialization}")
        print("=" * 50)
