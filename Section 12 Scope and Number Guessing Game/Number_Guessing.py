import random

num = random.randint(1,100)
won = False

def check_ans(ip, num):
    if ip < num:
        print("Too low.\nGuess again")
    elif ip > num:
        print("Too high.\nGuess again")
    else:
        print(f"You guessed the number! it is {num}")
        return True

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy" or difficulty == "hard":
        break
    else:
        print("Choose between easy or hard!")

if difficulty == "easy":
    chances = 10
else:
    chances = 5

while chances != 0:
    ip = int(input(f"you have {chances} attempts remaining\nMake a guess: "))

    won = check_ans(ip, num)

    if won:
        break
    
    chances -= 1

if not won:
    print("You are all out of attempts, you lose!")
