# Hanif Poribohon

class company:
    def __init__(self,name,address,) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers= []
        self.counter= []
        self.managers= []
        self.supervisors= []

class Driver:
    def __init__(self,name,age,license,accident_history) -> None:
        self.license = license
        self.name= name
        self.age= age
    
class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self,start,destination):
        pass
class Passenger:
    pass
class Supervisor:
    pass

red_mia = Driver("Rad_mia",38,'23383738',True)

