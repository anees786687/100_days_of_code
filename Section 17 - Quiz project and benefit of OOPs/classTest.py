class User:
    # we can use a contructor to initialize the variables to their starting values
    # the __init__() method is a special function which acts like a constructor for a class
    # the self must always be given as a parameter
    def __init__(self, name, id):
        print("New User is created")
        self.name = name
        self.id = id

    def display_user(self):
        print(f"UserName: {self.name} UserId: {self.id}")


usr1 = User("Anees", 111)
usr2 = User("Alwani", 222)

print("Shows the address of memory where the object is stored", usr1)

usr1.display_user()
usr2.display_user()

#this is one way of adding attributes to the class
# this is not a very good way of adding attributes to classes
# as it needs to be done for every object over and over again
# and is prone to errors
# DO NOT USE THIS, LIKE NEVER!
# usr1.id = 111
# usr1.name = "Anees"

