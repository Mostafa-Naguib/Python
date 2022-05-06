# if, elif, else...
# And here we test (or, and, not) logical operators...
# This programe...Its job to test who can watch the movie...
# So, the one who is gonna watch this move should be:
#                                                     1-Over 18.
#                                                     2-Female.
#                                                     3-From Egypt or Palestine
#                                                       To have a discount...

P_movie = 100
movie_rate = 18
age = int(input("Enter your age: ").strip())
gender = input("Male or Female: ").capitalize()
country = input("Where are you coming from: ").capitalize()

if age >= 1 and age <= 18 and not gender == "Male":
    print(f"Because You're {age}\nSo, you're underage, therefore this movie isn't capable for you.")

elif not (age >= 1 and age <= 18):
    if not gender == "Male":
        print("Welcome to our newbrand movie...")

        if country == "Egypt" or country == "Palestine":
            print(f"Cause you're coming from {country}\nSo, you're just gonna pay {P_movie-90}")
        elif country == "Syria" or country == "Sudan":
            print(f"Cause you're coming from {country}\nSo, you're just gonna pay {P_movie-75}")
        else:
            print(f"You're gonna pay {P_movie-50}")

else:
    print("We're sorry this movie is just for Female")

# a_short condition...
print("#" * 55)

movieRate = 18
age = int(input("Enter your age: ").strip())

print("This movie isn't compatible 4u." if age < 18 else "This movie is good 4u.")

# problem_1...
print("#" * 55)
arabCountries = ["Egypt", "Libya", "Algeria", "Tunisia", "Morocco", "Mauritania"]

country = input("Where are you from: ").strip().capitalize()


if country in arabCountries:
    print(f"Because you're from {country}, so you have 80% discount on your purchases")

else:
    print(f"Because you're from {country}, so you have 50% discount on your purchases")


# problem_2....
student = True
if student is True:
    print("Welcome back to school......")

# problem_3...
x = 5
y = 4
# It skips the condition....
if x < y:
    pass
