def greet(name):
    print(f"Hello {name}")

greet("Anees")


# function with two parameters
def greet_location(name, location):
    print(f"Hello {name} from {location}")

#function call using positional arguements
greet_location("Anees","India")

#function call using keyword arguements
greet_location(location="Mars", name="Alien")

