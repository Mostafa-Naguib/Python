import os

# relative path....
x = open("Hello.txt")
# absolute path....
x = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt")


print("=" * 59)
print(os.getcwd())

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

y = open("test1.txt")

# to delete file:
# os.remove(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt")
