class A:
    pass


class B:
    pass


class C(B):
    pass


obj = C()

print(isinstance(obj, C))
print(isinstance(obj, B))
print(isinstance(obj, A))
