import random
import data
import logo
import os

clear = lambda: os.system('cls')

print(logo.logo)

cmp1 = random.choice(data.data)
score = 0
while True:
    cmp2 = random.choice(data.data)
    if cmp1 == cmp2:
        cmp2 = random.choice(data.data)
    if score > 0:
        print(f"You're right! Current score:{score}")
    print(f"Compare A: {cmp1.get("name")}, a {cmp1.get("description")}, from {cmp1.get("country")}.")
    print(logo.vs)
    print(f"Compare B: {cmp2.get("name")}, a {cmp2.get("description")}, from {cmp2.get("country")}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (choice == 'a' and cmp1["follower_count"] > cmp2["follower_count"] ) or (choice == 'b' and cmp1["follower_count"] < cmp2["follower_count"]):
        score+=1
    else:
        print(f"Wrong! Your score is {score}")
        break
    cmp1 = cmp2
      
    clear()
    print(logo.logo)


