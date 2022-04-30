# Input

Name = input("What's your name: ")
Country = input("Where are you from: ")
City = input(f"In which city do you live in {Country.strip().capitalize()}: ")

Name = Name.strip().capitalize()
Country = Country.strip().capitalize()
City = City.strip().capitalize()


print(f"Welcom {Name}, you're from {Country:.3s}, and you're living in {City}")
