# base class/parent class
# derived class,child class

class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Running laptop: {self.brand}'
    def __repr__(self) -> str:
        return f'Phone: {self.brand} ; price: {self.price} color: {self.color}'

class Laptop:
    def __init__(self,memory) -> None:
        self.memory = memory

    def coding(self):
        return f'Learnign python and practicing'
    
class Phone(Device):
    def __init__(self,brand,price,color,dule_sim) -> None:
        self.dule_sim=dule_sim
        super().__init__(brand,price,color)
    
    def __repr__(self) -> str:
        return super().__repr__()
class Camera:
    def __init__(self,pixel) -> None:
        self.pixel = pixel

my_phone=Phone('Iphone',193933,'Blue',True)

print(my_phone)
