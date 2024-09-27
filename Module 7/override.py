class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def eat(self):
        print('vat mango polau horma')
    def exercise(self):
        raise NotImplementedError

class Crickter(Person):
    def __init__(self, name, age,team) -> None:
        self.team = team
        super().__init__(name, age)

#   override
    def eat(self):
        print('ruti vegetable')

    def exercise(self):
        print('Do exercise everyday')
# operator overload
    # + sign overload
    def __add__(self,other):
        return self.age + other.age
    # * sign overload
    def __mul__(self,other):
        return self.age * other.age
    def __len__(self):
        return self.age

sakib = Crickter('sakib',35,'BD')
sakib.eat()
sakib.exercise()
mushi = Crickter('Mushi',34,'BD')
# operator overload

print(3+8)
print('Rakib'+'Karim')
print(sakib+mushi)  # add sakib and mushi age sum
print(sakib*mushi)
print(len(sakib))


