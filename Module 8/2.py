class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a {self.name} .I am {self.age} years old.')
    def make_sound(self):
        pass
class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

animal = Animal('Dog',1.8)
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

animal.info()

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()
