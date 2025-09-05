# Consider the following snippet
# number = [1,2,3]
# new_list = []

# for n in number:
#     add_1 = n + 1
#     new_list.append(add_1)

"""
in the above snippet we have to create a for loop in order to operate on each element of 
the list, this can be skipped if simple operations have to be perfomed on the elments of the list

Using list comprehension we can take all these lines and turn it into a single line of code

new_list = [new_item for item in list] 
THis is the basic structure of list comprehension, we can replace the keywords with the desired variables to generate a new list
so the above snippet can be replaced by the following list comprehension

list comprehension takes sequences (list, tuples, strings, range) and goes through the items in a specific order and 
then something will be done on the item.

there can be a conditional list comprehension as well whose form is as follows
new_list = [new_item for item in list if test]

So the new_item is only added to the new_list if the test passes for the item in the list 

Here’s a generalized structure for a list comprehension with multiple for loops and conditions:

[(expression) 
 for item1 in iterable1 if condition1 
 for item2 in iterable2 if condition2
 ...]

You can add more for-loops and conditions as needed.
Each for-loop can be followed by an if condition that filters items at that stage.
The expression at the start defines what each element in the resulting list will be.
"""

# new_list = [n + 1 for n in number]
# print(new_list)

# squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# get even number from a list of strings
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# we can also work with strings in list comporehension
# op will be ['A', 'n', 'e', 'e', 's']
# name = 'Anees'
# name_list = [letter for letter in name]
# print(name_list)

# using range in lists
# double_num = [num * 2 for num in range(1,5)]
# print(double_num)

# using conditional list comprehension
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# len names is less than equal to 5
# short_names = [name for name in names if len(name) <=5 ]
# print(short_names)

# upper case names who length is greater than 5
# cap_names = [name.upper() for name in names if len(name) > 5]
# print(cap_names)

with open('./file1.txt') as file:
    num_list_1 = file.read().splitlines()

with open('./file2.txt') as file:
    num_list_2 = file.read().splitlines()

result = [int(num) for num in num_list_1 if num  in num_list_2]
print(result)