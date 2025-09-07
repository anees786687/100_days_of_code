"""
We need to better handle errors and exception in order to handle the program exit
correctly and in a graceful manner, in addiiton, we have to notify the user about the error or exception that
has occurred 

There are things that can go wrong and they must be taken care of pre-emptively, same thing goes with 
programs! So we have to handle these situations correctly

we use try-catch to catch and handle exceptions

try:
    Something that might cause an exceptiomn

except:
    do this if there was an exception, it is a must to specify the Exception and not use raw except
    as other errors that can occur can be missed! So what happens is if an error occurrs the type of error must be 
    used with the except keyword so every type of error can be handled. So the correct format for except will be

    except SomeError:
        some lines to excute!

    We can have multiple except blocks where each block runs when a particular error occurs. The format would be
    try:
        to do some task A and B
    except A_error:
        handle error for task A
    except B_error:
        handle error for task B
else:
    do this if there were NO exceptions

finally:
    do this no matter what happens!! Always going to be executed, mainly used to clean things up

so this is more like and if statement, if we try to do something which can cause an error then do somethin in except 
"""

# file not found error
# try:
#    file = open('a_text.txt')
# except: # never use raw excepts
#    print(f'File not found! creating file!')
#    open('a_text.txt', 'w')
#    # more stuff can be done here!


##  WHY NOT TO USE RAW EXCEPT!
a_dict = {'key':'value'}
try:
   file = open('a_text.txt') # FIRST EXCEPTION CAUGHT HERE
   # say we have a dict whose non existent key we try to access

   # SECOND EXCEPTION IS CAUGHT HERE!
   val = a_dict['asasas'] # this will create an error which will never be caught
   # to solve this we have to specify all the possible error that can occur during ther
   # execution of code in the try block
except FileNotFoundError as e: # never use raw excepts
   # other exceptions that can occur in try block will be missed and not handled correctly
   print(f'File not found! creating file!')
   file = open('a_text.txt', 'w')
   file.write('Wrote something after creating file in except block!')
   # more stuff can be done here!
except KeyError as ke:
   print(f'No key {ke} exists. Adding key value pair with random value in the dict!')
   a_dict['asasas'] = 'sasasa'


## using the else block. THis excutes where there arent any error
# all the the errors were handled correctly in the above block of code
# so no exceptions shall occur here! else block will be excuted!
try:
   file = open('a_text.txt')
   # say we have a dict whose non existent key we try to access
   val = a_dict['asasas'] # this will create an error which will never be caught
   # to solve this we have to specify all the possible error that can occur during ther
   # execution of code in the try block
except FileNotFoundError as e: # never use raw excepts
   # other exceptions that can occur in try block will be missed and not handled correctly
   print(f'File not found! creating file!')
   file = open('a_text.txt', 'w')
   file.write('Wrote something after creating file in except block!')
   # more stuff can be done here!
except KeyError as ke:
   print(f'No key {ke} exists!')
else:
   print('Everything works! no error occurred in try block')
   content = file.read()
   print(content)

   print(a_dict)
finally:
   # in this block do the cleaning up which is necessary to 
   # save resources and prevent unkown behaviour!
   file.close()

