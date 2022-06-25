try:
    num = int(input("Enter your phone number: "))
    print(f"This is your phone number {num}")

except ValueError:
    print("Please enter a valid value...")

except NameError:
    print("Invalid syntax")

except:
    print("There's an error in the code")

else:  # It just excutes when the code works well...
    print("How is it going? ")

finally:  # It excutes whatever happens...
    print("See you soon...")
