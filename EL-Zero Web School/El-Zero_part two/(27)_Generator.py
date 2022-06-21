def gen():
    yield "Welcome from generator"
    yield "My name is Moustafa"
    yield "I'm 20 years old"
    yield "I'm coming from Egypt"


x = gen()

print(next(x))

for info in x:
    print(info)
