# absolute path....
x = open(r"C:\Users\moust\Desktop\pass.txt")

# relative path....
x = open(r"Hello.txt")


print("===============================")

import os

print(os.getcwd())

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())