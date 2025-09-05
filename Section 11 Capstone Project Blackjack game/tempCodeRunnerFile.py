             new_card = random.choice(cards)
                if new_card == 11 and player_score >= 21:
                    new_card = 1
                dealer_cards.append(new_card)
                dealer_score += new_card
            
            end_game(player_cards,player_score,