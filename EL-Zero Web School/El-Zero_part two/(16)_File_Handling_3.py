# functions we use with mode(write, w) ==> write() writelines()
x = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt", "w")
x.write("Now i just try to memorize...")


y = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test2.txt", "w")
li = ["Mostafa ", "Naguib ", "El-Sayed "]
y.writelines(li)

# the functions we use with mode(apped, a) ==> write(), truncate(), tell()
x = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt", "a")
x.write("\n\nand everything is fine...")

x = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt", "a")
x.truncate(26)

x = open(r"C:\Users\moust\Desktop\Prog\Python\EL-Zero Web School\El-Zero_part two\test1.txt", "a")
print(x.tell())
