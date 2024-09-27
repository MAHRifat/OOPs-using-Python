from abc import ABC, abstractmethod
# abc -> abstract base class
class animal(ABC):
    @abstractmethod   # enforce all derived class to have a eat method
    def eat(self):
        print('I need food')

    def move(self):
        pass

class monkey(animal):
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()

    def eat(self):
        print('Eating banana')

jonker = monkey('Jonkar')
jonker.eat()
    

    