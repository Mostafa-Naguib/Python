try:
    x = int(input("Enter your phone number: "))
    print(f"This is your phone number {x}")

except ValueError:
    print("please enter a valid value...")

else:
    print("How is it going? ")

finally:
    print("See you soon...")
