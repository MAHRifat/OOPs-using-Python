class Food:
    def __init__(self,name,price,cooking_time) -> None:
        self.name=name
        self.price = price
        self.cooking_time=cooking_time

class Burger(Food):
    def __init__(self, name, price, cooking_time,meat,ingredients ) -> None:
        super().__init__(name, price, cooking_time)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, cooking_time,size,toppings) -> None:
        super().__init__(name, price, cooking_time)
        self.size=size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, cooking_time,is_cold=True) -> None:
        super().__init__(name, price, cooking_time)
        self.is_cold = is_cold

class Menu:
    def __init__(self) -> None:
        self.pizzas =[]
        self.burgers = []
        self.drinks = []

    def add_menu_itme(self,itme_type,item):
        if itme_type == 'pizza':
            self.pizzas.append(item)
        elif itme_type == 'burger':
            self.burgers.append(item)
        elif itme_type == 'drink':
            self.drinks.append(item)

    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'{pizza.name} price: {pizza.price}')
        for burger in self.burgers:
            print(f'{burger.name} price: {burger.price}')
        for drink in self.drinks:
            print(f'{drink.name} price: {drink.price}')


