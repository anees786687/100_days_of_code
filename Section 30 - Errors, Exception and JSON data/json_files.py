"""
There is an inbuilt library in python to work with 
JSON string.

Most uses methods are 
json.dump() - Write
json.load() - Read
json.update() - Update
"""
import json

"""Working with JSON strings"""
# json_string = '''
# {
#     "students": [
#         {
#             "id": 1,
#             "name": "Tim",
#             "age": 21,
#             "full-time": true
#         },
#         {
#             "id": 2,
#             "name": "Joe",
#             "age": 33,
#             "full-time": false
#         }
#     ]
# }
# '''
# # loading a json string
# data = json.loads(json_string) # this returns a dict after parsing the json string
# # print(data)

# ## dumping dict to json
# # add some random key value to the dict
# data['State'] = True

# new_data = json.dumps(data, indent=4) # this gives a string!
# print(new_data)

"""Working with JSON files"""
# reading and writing to an existing json file
with open('./data.json', 'r') as f:
    data = json.load(f)


print(data) # this will be a dict!
new_student = {
    "id": 3,
    "name": "Anna",
    "age": 25,
    "full-time": True
}
data['students'].append(new_student)
with open('./data.json', 'w') as f:
    json.dump(data,f,indent=4)