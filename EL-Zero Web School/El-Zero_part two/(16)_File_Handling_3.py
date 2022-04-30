# write...

file = open("test1.txt", "w")
file.write("Hello everyone\n")
file.write("Ramadan kareem")


myList = ["Egypt ", "El-Zamalek ", "Sinai "]
favorite = open("test2.txt", "w")
favorite.writelines(myList)


# append
favorite = open("test2.txt", "a")
favorite.write("\nHello everybody\n")
favorite.write("How the fast is going? ")
