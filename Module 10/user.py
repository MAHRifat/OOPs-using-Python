from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name =name
        self.phone = phone
        self.email =email
        self.address = address
    
class Customer(User):
    def __init__(self, name,money,phone,email,address) -> None:
        self.wallet = money
        self.__order = None
        self.bill_due=0
        super().__init__(name,phone,email,address)


    @property          #getter
    def order(self):
        return self.__order
    
    @order.setter        #setter
    def order(self,order):
        self.__order = order

    def place_order(self,order):
        self.order=order
        self.bill_due += order.bill
        print(f'{self.naem} placed an order with bill {order.bill}')

    def eat_food(self,order):
        print(f'{self.name} itme food {order.items}')


    def pay_for_order(self,amount):
        pass

    def give_tip(self,amount):
        pass

    def write_review(self,stars):
        pass

class Employee(User):
    def __init__(self, name,salary,starting_date,department,phone,email,address) -> None:
        super().__init__(name,phone,email,address)
        self.salary = salary
        self.starting_date=starting_date
        self.due = salary
        self.department = department

    def receive_salary(self):
        self.due = 0
    
class Chef(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address,cooking_item) -> None:
        super().__init__(name, salary, starting_date, department, phone, email, address)
        self.cooking_item = cooking_item

class Server(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address) -> None:
        self.tips_earning = 0
        super().__init__(name, salary, starting_date, department, phone, email, address)

    def take_order(self,order):
        pass

    def tranfer_order(self,order):
        pass

    def server_food(self,order):
        pass

    def receive_tips(self,amount):
        self.tips_earning=amount

class Manager(Employee):
    def __init__(self, name, salary, starting_date, department, phone, email, address) -> None:
        super().__init__(name, salary, starting_date, department, phone, email, address)

    