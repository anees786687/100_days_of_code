import random

"""
rock wins against scissors
scissors wins against papers
paper wins against rock
"""
choices = ["rock", "paper", "scissors"]

u_choice = choices[int(input("Enter your choice. 0 for rock, 1 for paper, and 2 for scissors: "))]
ai_choice = random.choice(choices)

print(f"You chose {u_choice}")
print(f"AI chose {ai_choice}")
if u_choice == "rock":
    # user choose rock
    if ai_choice == "paper":
        print("AI wins")
    elif ai_choice == "scissors":
        print("User wins")
    else:
        print("Draw")
elif u_choice == "paper":
    if ai_choice == "scissors":
        print("AI wins")
    elif ai_choice == "rock":
        print("User wins")
    else:
        print("Draw")
else:
    if ai_choice == "rock":
        print("AI wins")
    elif ai_choice == "paper":
        print("User wins")
    else:
        print("Draw")