class Laptop:
    def __init__(self,brand,price,color,memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    def coding(self):
        return f'Learnign python and practicing'
    
class Phone:
    def __init__(self,brand,price,color,dule_sim) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.dule_sim=dule_sim
        