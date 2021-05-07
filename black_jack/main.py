import random
import os
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""
cards={'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10}
print(logo)
print("Welcome to the game of BlackJack!")
keys=[x for x in cards.keys()]

def scoreCalculation(tCards):
    tScore=0
    for card in tCards:
        tScore+=cards[card]
    if 'A' in tCards:
        if tScore + 10 <= 21:
            tScore=tScore+10
    return tScore

def hit(tCards):
    tCards.append(random.choice(keys))
    return scoreCalculation(tCards)

def bj():
    yourCards.append(random.choice(keys))
    yourCards.append(random.choice(keys))
    currentScore=scoreCalculation(yourCards)
    print(f"Your cards: {yourCards}, current score: {currentScore}")

    dealerCards.append(random.choice(keys))
    dealerScore=cards[dealerCards[0]]
    print(f"Computer's first card: {dealerCards}, dealer score is {dealerScore}")

    if currentScore == 21 :
        print("Blackjack!  You've won!")
        return

    while input("Type 'h' (hit) to get another card, type 's' (stay) to pass: ") == 'h':
        currentScore=hit(yourCards)
        if currentScore == 21:
            print("Black Jack!  You win!  You got 21!")
            return
        elif currentScore > 21:
            print(f"Busted! You lose! Your score is {currentScore}")
            return
        else:
            print(f"Your cards: {yourCards}, current score: {currentScore}")

    #if pass, now it's time to hit dealer
    print("You have chosen pass.  Now it's dealer's turn")
    print(f"Your cards: {yourCards}, current score: {currentScore}")

    while dealerScore < 17:
        dealerScore=hit(dealerCards)
        print(f"Dealer's cards: {dealerCards}, current score: {dealerScore}")

    if dealerScore ==21:
        print("Dealer's got BlackJack!  You lose!")
    elif dealerScore > 21:
        print ("Dealer busted!  You win!")
    elif currentScore < dealerScore:
        print("You lose! Dealer has won!")
    elif currentScore > dealerScore:
        print("You win! Dealer has lost!")
    else:
        print("The game is a tie!")

nextGame=True

while nextGame:
    yourCards=[]
    dealerCards=[]
    bj()
    if input("Would you like another game? (y/n)").lower() != 'y':
        nextGame=False
    else:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
