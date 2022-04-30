
employees = ["Mostafa", "Naguib", "Elsayed", "Hassan", "Ali"]

name = input("Enter your name: ").strip().capitalize()


if name in employees:
    print("Welcom back")
    option = input("Do you want to delete or update: ").strip().lower()

    if option == "update":
        newName = input("Type your new name: ").strip().capitalize()
        employees[employees.index(name)] = newName
        print("success \nyour name is updated")
        print(employees)

    elif option == "delete":
        employees.remove(name)
        print("success \nyour name is deleted")
        print(employees)

else:
    print("A wrong name.")
    addName = input("If you want us to add you press \"add\": ").strip().lower()

    if addName == "add":
        print("You've added")
        employees.append(name)
        print(employees)
