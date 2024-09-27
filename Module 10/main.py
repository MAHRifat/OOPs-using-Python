from menu import Pizza,Burger,Menu,Drinks
from resgaurant import Restaurant
from user import Chef,Customer,Server,Manager
from Order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki pizza',1500,15,'large',['shutki','peyaj','moric'])
    menu.add_menu_itme('pizza',pizza_1)
    pizza_2 = Pizza('Chikhan pizza',1000,15,'large',['chicken','peyaj','moric'])
    menu.add_menu_itme('pizza',pizza_2)
    pizza_3 = Pizza('Meat pizza',1200,15,'large',['meat','peyaj','moric'])
    menu.add_menu_itme('pizza',pizza_3)

    # add burger to the menu
    burger_1=Burger('chicken burger',110,20,'chikhan',['sosa','peyej','moric'])
    menu.add_menu_itme('burger',burger_1)
    burger_2=Burger('Meat burger',110,20,'Meat',['sosa','peyej','moric'])
    menu.add_menu_itme('burger',burger_2)

    # add drinks to the menu
    coke = Drinks('Coke',30,2,True)
    menu.add_menu_itme('drink',coke)
    coffee = Drinks('Coffee',120,10,False)
    menu.add_menu_itme('drink',coffee)

    menu.show_menu()

    # show menu
    menu.show_menu()

    restaurant = Restaurant('Sai Baba Restaurant', 1000, menu)

    # add employess
    manager=Manager('kala chan',1500,'5','All',25665256,'kala@gmail.com','kalapur')

    restaurant.add_employee('manager',manager)

    chef =Chef(
        'Taj',2500,10,'Chef',35454,'taj@gmail.com','Foridpur','all'
    )
    restaurant.add_employee('Chef',chef)

    server = Server('Raj',1000,5,'Server',46538,'raj@gmail.com','Foridpur')
    restaurant.add_employee('Server',server)

    # show employees
    restaurant.show_employees()

    # customer
    customer_1 = Customer('a',5000,276375,'a@gmail.com','Cumilla')
    order_1=Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order_1

    
# call the main
# main()

if __name__ == '__main__':
    main()

