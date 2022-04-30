def decorate(x):

    def input():
        import termcolor
        import pyfiglet

        print(termcolor.colored(pyfiglet.figlet_format("Welcome"), color="green"))
        x()

    return input


@decorate
def name():
    name = input("Enter your name: ")
    print("Your name is: ", name)


name()
