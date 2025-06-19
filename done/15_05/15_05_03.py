class A:
    def speak(self):
        print("Я клас A")


class B(A):
    def speak(self):
        print("Я клас B")


class C(A):
    def speak(self):
        print("Я клас C")


class D(B, C):
    def speak(self):
        print("Я клас D")


def show_mro(cls):
    print(f"MRO для класу {cls.__name__}:")
    for base in cls.__mro__:
        print(f" - {base.__name__}")


d = D()
d.speak()
show_mro(D)
