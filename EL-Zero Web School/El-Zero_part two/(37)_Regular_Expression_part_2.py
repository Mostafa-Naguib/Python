import re

# split()
massage = "I love ELZamalek_and_Jerusalem"

print(re.split(r"\s|_", massage, 5))


# sub
print("=" * 50)

massage = "I love ELZamalek_and_Jerusalem"

print(re.sub(r"\s|_", "-", massage, 5))
