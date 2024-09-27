class aminal:
    def __init__(self,name) -> None:
        self.name=name

    def make_sound(self):
        print('Animal are shouting')

class dog(aminal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheu gheu')

class cat(aminal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("mau mau")
class Tiger(aminal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Bha Bha')

don = Tiger('Don')
shepard = dog('Shepard')
goat = cat('Cat')

animals = [don,shepard,goat]

for animal in animals:
    animal.make_sound()

