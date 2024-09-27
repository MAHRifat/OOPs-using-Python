from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)}and drivers: {len(self.drivers)}'

class User(ABC):
    def __init__(self,name,email,nId) -> None:
        self.name = name
        self.email = email
        self.__id=0
        # todo: set user id dynamically
        self.__NID=nId
        self.wallet=0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nId,current_location,initial_amount) -> None:
        self.wallet=initial_amount
        self.current_location = current_location
        self.current_ride = None
        super().__init__(name, email, nId)

    def display_profile(self):
        print(f'Rider name: {self.name} and email: {self.email}')
    
    def update_locaiton(self,current_location):
        self.current_location = current_location

    def load_cash(self,ammount):
        if ammount > 0:
            self.wallet+=ammount
    
    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            ride_request = Ride_request(self,destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            self.current_ride=ride

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nId,current_locaiton) -> None:
        self.current_location = current_locaiton
        self.wallet = 0
        super().__init__(name, email, nId)

    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')

    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider=None
        self.start_time= None
        self.end_time=None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,rider,ammount):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details, started: {self.start_location} to {self.end_location}'

class Ride_request:
    def __init__(self,rider,end_location) -> None:
        self.rider = rider
        self.end_location=end_location


class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.available_driver=drivers

    def find_driver(self,rider_requent):
        if len(self.available_driver) > 0:
            # TODO: find the closest driver of the rider
            driver = self.available_driver[0]
            ride =Ride(rider_requent.rider.current_location,rider_requent.rider.end_location)
            driver.accept_ride(ride)

            return ride

class vehicle(ABC):

    speed = {
        'car': 50,
        'bike': 60,
        'cng': 40
    }

    def __init__(self,vegicle_type,license_plate,rate) -> None:
        self.vehicle_type = vegicle_type
        self.license_plate = license_plate
        self.rate=rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass

class Car(vehicle):
    def __init__(self, vegicle_type, license_plate, rate) -> None:
        super().__init__(vegicle_type, license_plate, rate)

    def start_drive(self):
        self.status='unavailable'

class Bike(vehicle):
    def __init__(self, vegicle_type, license_plate, rate) -> None:
        super().__init__(vegicle_type, license_plate, rate)

    def start_drive(self):
        self.status='unavailable'

# check the class integratin

niya_jao = Ride_sharing("Niye Jao")
sakib = Rider("sakib khan",'dkfj@gamil.com',535343,'mogakhali',1200)
niya_jao.add_rider(sakib)
kalu = Driver('kalu','dfhdf@gmail.com',343,'gulshan 1')
niya_jao.add_driver(kalu)

print(niya_jao)

sakib.request_ride(niya_jao,'uttara')
sakib.show_current_ride()
