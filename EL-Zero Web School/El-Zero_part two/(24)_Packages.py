import termcolor
import pyfiglet

print(termcolor.colored("Mostafa", color="red"))
print(pyfiglet.figlet_format("Mostafa"))

print(termcolor.colored(pyfiglet.figlet_format("El-Zamalek"), color="green"))
