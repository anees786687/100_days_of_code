class MenuItem:
    def __init__(self,name,cost, water,milk, coffee) :
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="Latte",cost=2.5, water=200,milk=150,coffee=24),
            MenuItem(name="Espresso",cost=1.5, water=50,milk=0,coffee=18),
            MenuItem(name="Cappuccino",cost=2.5, water=250,milk=50,coffee=24)
        ]

        self.item = None

    def get_items(self):
        str = ""
        for items in self.menu:
            str += f"{items.name}/"
        return str
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                self.item = item
                return True
        print(f"{order_name} not found!")

    def get_cost(self, choice):
        for item in self.menu:
            if choice == item.name:
                return item.cost
    
    def get_item(self, choice):
        for item in self.menu:
            if choice == item.name:
                return item