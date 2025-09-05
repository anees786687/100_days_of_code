"""
Goal is to add cards to the largest number without oging over 21
if more than 21 then we lose

All cards from 2 to 10 have the same face value

face cards each count as 10

Ace can either be 1 or 11

if the dealer or the player has hand less than 17 then the  dealer has to draw

"""
import random
import os
clear = lambda: os.system('cls')

def end_game(player_cards,player_score,dealer_cards,dealer_score):
    print(f"Your final hand: {player_cards}, final score: {player_score}\nComputer's final hand: {dealer_cards}, final score: {dealer_score}\n")
    if player_score <= 21 and  player_score > dealer_score or dealer_score > 21:
        print("You Win")
    elif dealer_score <= 21 and player_score > 21 or player_score < dealer_score:
        print("You Lose")
    elif dealer_score == player_score:
        print("Draw")

def start_game(cards):
    while(True):
        dealer_cards =[]
        dealer_score = 0

        player_cards = []
        player_score = 0

        choice = input("Do you want to a play a game of Blackjack? Type 'y' or 'n': ")
        clear()
        if choice == 'y':
            dealer_cards =[random.choice(cards), random.choice(cards)]
            dealer_score = sum(dealer_cards)

            player_cards = [random.choice(cards), random.choice(cards)]
            player_score = sum(player_cards)

            if player_score >= 21 or dealer_score >= 21:
                end_game(player_cards, player_score,dealer_cards,dealer_score)
                continue
        
            print(f"Your cards: {player_cards}, current score: {player_score}\nComputer's first card: {dealer_cards[0]}\n")
            hit = input("Type 'y' to get another card, type 'n' to pass: ")

            while hit != 'n':
                new_card = random.choice(cards) 
                if new_card == 11 and player_score > 21:
                    new_card = 1 #ace value over 21
                
                player_cards.append(new_card)
                player_score += new_card
                if player_score > 21:
                    end_game(player_cards,player_score,dealer_cards,dealer_score)
                    break
                
                print(f"Your cards: {player_cards}, current score: {player_score}\nComputer's first card: {dealer_cards[0]}\n")
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                while dealer_score < 17:
                    new_card = random.choice(cards)
                    if new_card == 11 and dealer_score > 21:
                        new_card = 1
                    dealer_cards.append(new_card)
                    dealer_score += new_card
                
                end_game(player_cards,player_score,dealer_cards,dealer_score)
        else:
            break


cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
start_game(cards)


    






   

