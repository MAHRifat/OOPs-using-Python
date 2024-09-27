# Helper Function

class MathOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        def add():
            return self.a + self.b

        def multiply():
            return self.a * self.b

        result = add() * multiply()
        return result

math_obj = MathOperations(2, 3)
print(math_obj.calculate()) 
