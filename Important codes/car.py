started = False
stopped = False
while(True):

    order = input("> ").lower()

    if order == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to  quit
        """)

    elif order == "start":

        if started:
            print("Car is aready started...")

        else:
            print("Car started...Ready to go")
            started = True

    elif order == "stop":

        if not stopped:
            print("Car is aready stopped...")

        else:
            print("Car stop...Ready to go")
            stopped = False

    elif order == "quit":
        break

    else:
        print("I don't understand that...")
