from menu import Menu
class CoffeeMaker:
    def __init__(self):
        self.resources = {  
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.menu = Menu()
        self.choice = ""

    def report(self):
        print(f"Water: {self.resources.get("water")}\n" + 
              f"Milk: {self.resources.get("milk")}\n" +
              f"Coffee: {self.resources.get("coffee")}")
    
    def is_resource_sufficent(self, drink):
        choice = self.menu.get_item(drink)
        for item in choice.ingredients:
            if choice.ingredients[item] > self.resources[item]:
                print(f"Sorry! There is not enough {item}")
                return False
        return True
    
    def get_choice(self):
        self.choice = input("Enter your choice: ")
    
    def make_coffee(self, drink):
        choice = self.menu.get_item(drink)
        for item in self.resources:
            self.resources[item] -= choice.ingredients[item]
        print(f"Here is your {drink}. Enjoy!")
    

class MoneyMachine:
    def __init__(self):
        self.coin_values = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01
        }
        self.profit = 0
        self.amount_received = 0

    def report(self):
        print(f"Money: ${self.profit}")
    
    def process_coins(self):
        for coins in self.coin_values:
            self.amount_received += int(input(f"How many {coins}?: ")) * self.coin_values.get(coins)

        return self.amount_received
    
    def make_payment(self, cost):
        self.process_coins()

        if self.amount_received >= cost:
            change = round(self.amount_received - cost, 2)
            print(f"Here is the ${change} in change")
            self.profit += cost
            self.amount_received = 0
            return True 
        else:
            print("Sorry! the amount is not enough")
            self.amount_received = 0
            return False
