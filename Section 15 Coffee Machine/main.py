MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cap": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = 0

"""
check if enough resources are present, if yes the return true and an empty string. If not the return false 
and the resouce which is in insufficient amount

"""
def check_resources(choice):
    coffee_deets  = MENU[choice]
    ingredients = coffee_deets.get("ingredients")
    if choice == "espresso":
        if resources["water"] < ingredients["water"]:
            return False, "water"
        elif resources["coffee"] < ingredients["coffee"]:
            return False, "coffee"
    elif choice == "latte" or choice == "cap":
        if resources["water"] < ingredients["water"]:
            return False, "water"
        elif resources["coffee"] < ingredients["coffee"]:
            return False, "coffee"
        elif resources["milk"] < ingredients["milk"]:
            return False, "milk"
    
    return True, ""

"""
function to calculate the total amount inserted by the user
"""
def total_amt(quarter, dimes, nickles, pennies):
    return quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

"""
function to generate a report of the resources and money in the coffee machine 
"""
def gen_report(resources, coins):
    print(
        f"Water: {resources.get("water")}\nMilk: {resources.get("milk")}\nCoffee: {resources.get("coffee")}\nMoney: ${coins}")

"""
function that makes the coffee according to the choice of the user
"""
def make_coffee(choice, quarter, dimes, nickles, pennies):
    coffee_deets  = MENU[choice]
    ingredients = coffee_deets.get("ingredients")

    if choice == "espresso":
            resources["water"] -= ingredients["water"]
            resources["coffee"] -= ingredients["coffee"]
    elif choice == "latte" or choice == "cap":
            resources["water"] -= ingredients["water"]
            resources["milk"] -= ingredients["milk"]
            resources["coffee"] -= ingredients["coffee"]
        
    
    change = abs(total_coins - coffee_deets.get("cost"))
    global money
    money += coffee_deets.get("cost")
    print(f"Here is ${format(change,'.2f')}.\nEnjoy your {choice}")


"""
loop that keeps the machine on and asks the user for their choice, if turned off the loop breaks
user can ask for report of the coffee machine resources
"""
while True:
    choice = input("What would you like? (espresso/latte/cap)").lower()
    if choice == "off":
        break
    elif choice == "report":
        gen_report(resources, money)
    else:
        print("Please insert coins.")
        quarter = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_coins = total_amt(quarter,dimes,nickles,pennies) # calc the total amt from the coins put in
        enough_resources, dep_resource = check_resources(choice) 
        cost = MENU[choice].get("cost")

        if enough_resources and total_coins > cost:
            make_coffee(choice, quarter, dimes, nickles, pennies)
        else:
            if not enough_resources:
                print(f"There is not enough {dep_resource}")
            elif total_coins < cost:
                print("Insufficeint amount inserted!")




