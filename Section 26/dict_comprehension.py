"""
We can create a new dict from the values in existing dict or list
the format is as follows

new_dict = {new_key:new_value for item in list}
The above format is for creating a dictionary from a list

We can also create a new dictionary from an existing dictionary

new_dict = {new_key:new_value for (key,value) in dict.items()}

get hold of all the items in the dict and then split in a key and value, so we are looping through each key and value from 
the old dict to create a new dict

We can also use conditional dict comprehension

new_dict = {new_key:new_value for (key,value) in dict.items() if test}

if the test is passed on the (key,value) pair then the new key:value pair is added to the new_dict

generalized structure for a dictionary comprehension with multiple for loops and conditions:

{key_expression: value_expression
 for item1 in iterable1 if condition1
 for item2 in iterable2 if condition2
 ...}

example:

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'e', 'i']
result = {(x, y): f"{x}-{y}" for x in list1 if x % 2 == 0 for y in list2 if y in 'aeiou'}

//op: {(2, 'a'): '2-a', (2, 'e'): '2-e', (2, 'i'): '2-i', (4, 'a'): '4-a', (4, 'e'): '4-e', (4, 'i'): '4-i'}

You can add more for-loops and conditions as needed.
Each for-loop can be followed by an if condition to filter items.
The key_expression and value_expression define the keys and values for the resulting dictionary.
"""

import random
# create dict and genrate a random score for each student
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# score_dict = {f'{name}':random.randint(1,100) for name in names}
# print(score_dict)

# use score_dict to make dict of students who have passed
# passed_dict = {name:score for (name,score) in score_dict.items() if score >= 40}
# print(passed_dict)


"""
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the 
given sentence and calculates the number of letters in each word. 
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split(" ")
result = {word:len(word) for word in word_list}
print(result)

"""
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. To convert temp_c into temp_f use this formula: 

(temp_c * 9/5) + 32 = temp_f 
"""
def convert_C_to_F(temp: int):
    return temp * 9/5 + 32

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:convert_C_to_F(temp) for (day,temp) in weather_c.items()}

print(weather_f)