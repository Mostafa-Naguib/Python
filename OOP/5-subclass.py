# "Subclass" (Child Class, Extended class, Derived class) => 'Who inherit from other class'
# "superclass" (Parent class, Base class)
# issubclass(subclass, superclass)

class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(A, C))
print(issubclass(A, B))
