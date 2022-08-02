class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f"Your name is: {self.name}")
        print(f"Your age is: {self.age}")
        print(f"your gender is: {self.gender}")
        print("=" * 55)


p1 = Person("Mostafa", 20, 'M')
p2 = Person("ALaa", 22, 'F')


p1.info()
p2.info()
