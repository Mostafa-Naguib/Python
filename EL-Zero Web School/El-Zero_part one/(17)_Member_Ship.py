
arabCountries = ["Egypt", "Libya", "Algeria", "Tunisia", "Morocco", "Mauritania"]

country = input("Where are you from: ").strip().capitalize()


if country in arabCountries:
    print(f"Because you're from {country}, so you have 80% discount on your purchases")

else:
    print(f"Because you're from {country}, so you have 50% discount on your purchases")
