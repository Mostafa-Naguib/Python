class Exame:

    subject = "Physics"
    duration = 60
    grade = "11th"
    school = "Al-khediou Ismael"

    @staticmethod
    def print_info():
        print(f"The subject: {Exame.subject}")
        print(f"The duration: {Exame.duration}")
        print(f"Grade: {Exame.grade}")
        print(f"The school: {Exame.school}")
