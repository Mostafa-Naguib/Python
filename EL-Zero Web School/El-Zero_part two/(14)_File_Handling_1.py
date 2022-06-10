# absolute path....
import os
x = open(r"C:\Users\moust\Desktop\pass.txt")

# relative path....
x = open(r"Hello.txt")


print("===============================")


print(os.getcwd())

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
