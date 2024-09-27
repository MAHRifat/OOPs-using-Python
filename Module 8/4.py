class A:
    def A_info(self):
        print("A")

class B:
    def B_info(self):
        print("B")

class Bat(A,B):
    pass

b = Bat()
b.A_info()
b.B_info()