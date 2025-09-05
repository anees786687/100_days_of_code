"""
We can pass unlimited arguements to  a function using the *args parameter
the arguments passed will be used as a typle in the given function. the name args is not necessary but the * is 
the * denotes that the function accepts any number of arguements
"""

# make an add function which takes unlimited number of args and adds them up
def add(*args):
    sum = 0

    for n in args:
        sum += n

    return sum

# print(add(1,2,3,4,5))


"""
Now what if we want to refer to the arguements by name rather thn indices, for this we can use kwargs
kwargs acts asa dcitionary in the function and the way it can be called is my giving keyword arguements while calling the function

Basically i can look through all the inputs and find the ones that I want and do something with it.

We basically name the values that we are passing to the function
"""
def calculate(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']

    print(n)

calculate(5, add = 3, multiply = 5)


"""
As in the case of Label in tkinter we see that the constructor also has kwargs while instantiating the object,
thus kwargs can be implemented at the constructor level as well
"""
class Car:
    def __init__(self, **kwargs):
        # this is one way of getting values from dicitonary dick['key'] but 
        # if say model is not mentioned this will give us an error
        # self.make = kwargs['make']
        # self.model = kwargs['model']

        # so to over come the error we use get('key') method, if no such key is there then None is returned
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

    def details_print(self):
        print(self.make,self.model)

# my_car = Car(make='ford', model='fiesta')
# my_car.details_print()

# example for using get method to for kwargs dictionary
my_car_1 = Car(make='hyundai')
my_car_1.details_print()