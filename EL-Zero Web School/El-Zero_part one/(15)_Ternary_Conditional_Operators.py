# Short if

movieRate = 18
age = int(input("Enter your age: ").strip())

#if age < movieRate:
    #print(f"We're sorry. \nThis movie isn't compatible 4U because you're {age} years old")

#else:
   #print(f"Welcome.\nThis movie is compatible 4U because you're {age} years old")

print("=" * 40)

print("This movie isn't compatible" if age < movieRate else "This movie is compatible")



