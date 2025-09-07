"""
Apaprt from try, except, else, finally, we have a keyword called raise this allows us to 
raise out own exceptions and can be raise wherever appropritate

"""

# a_dict = {'key':'value'}
# try:
#     file = open('a_text.txt') # FIRST EXCEPTION CAUGHT HERE
#     # say we have a dict whose non existent key we try to access

#     # SECOND EXCEPTION IS CAUGHT HERE!
#     val = a_dict['key'] # this will create an error which will never be caught
#     # to solve this we have to specify all the possible error that can occur during ther
#     # execution of code in the try block
# except FileNotFoundError as e: # never use raw excepts
#    # other exceptions that can occur in try block will be missed and not handled correctly
#     print(f'File not found! creating file!')
#     file = open('a_text.txt', 'w')
#     file.write('Wrote something after creating file in except block!')
#     # more stuff can be done here!
# except KeyError as ke:
#     print(f'No key {ke} exists. Adding key value pair with random value in the dict!')
#     a_dict['asasas'] = 'sasasa'
# finally:
#     # we can raise some error of our know, do this wehere ever apporpriate
#     raise TypeError('Some made up error!')


# When should we raise an error!. Consider the case of caluclating BMI
height = float(input("Height in meters: "))
weight = int(input('Weight: '))

# say the user provides some unrealistic height which isnt humanly possible
# in this case we can raise an exception and informt the user to enter the correct height!

if height > 3.0:
    raise ValueError('Please enter height less than 3m!')
bmi = weight / height ** 2