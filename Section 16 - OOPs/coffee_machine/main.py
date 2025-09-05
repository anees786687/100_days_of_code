from menu import Menu
from coffee_machine import CoffeeMaker, MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()

while True:
    coffee_maker.get_choice()
    if coffee_maker.choice == "off":
        break
    elif coffee_maker.choice == "report":
        coffee_maker.report()
        money_maker.report()
    elif menu.find_drink(coffee_maker.choice):
        if coffee_maker.is_resource_sufficent(coffee_maker.choice) and money_maker.make_payment(menu.get_cost(coffee_maker.choice)):
            coffee_maker.make_coffee(coffee_maker.choice)
           