capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
} # Simple dictionary

# dictionary with nested lists
travel_log = {
    "Maharashtra" : ["Mumbai", "Pune", "Karad"],
    "Canada" : ["Winnipeg", "Alberta"],
    "America" : ["Ohio","Texas","Atlanta"]
}

# printing Pune from the above list
#print(travel_log["Maharashtra"][1])

# 2d list
mat = [[1 ,2,3],[4,5,6],[7,8,9]]

# for i in mat:
#     for j in i:
#         print(j,end=" ", sep = " ")
#     print()

# dict within a dict aka dict-ception

grades = {
    "Sem 1":{
        "Maths 1":90,
        "BEE":85,
        "Physics":90
    },
    "Sem 2":{
        "Maths 2":90,
        "Chem":100,
        "Mechanics":95
    }
}

for sem in grades:
    for sub in grades[sem]:
        print(sub,grades[sem][sub])
    print()