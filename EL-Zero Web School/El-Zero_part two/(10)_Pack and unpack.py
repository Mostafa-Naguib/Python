companies = ("Microsoft", "Apple", "Google", "IBM", "Intel", "AMD")

companies_with_dates = {
    "Microsoft": 1975,
    "Apple": 1976,
    "Google": 1998,
    "IBM": 1911,
    "Intel": 1968,
    "AMD": 1969
}


def history(writer, *companies, **dates):
    print(f"This article is written by {writer}.")
    print("It talks about the history of high-tech companies...")
    for x in companies:
        print(f"- {x}")

    for x, y in dates.items():
        print(f"- {x} is founded in {y}")


history("Mustafa", *companies, **companies_with_dates)
