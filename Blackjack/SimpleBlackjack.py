"""
@Today's Date : 1/6/2023

@Author : Thomas Barker
"""
import random


def createDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
               "Queen", "King"]
    # Combine each number with each suit to get a full deck of cards
    deck = [number + " of " + suit for number in numbers for suit in suits]
    return deck
    # print(deck, len(deck))

def deckVals(deck):
    deckval = {}
    for card in deck:
        number = card.split(" ")[0]
        if number.isdigit():
            deckval[card] = int(number)
        else:
            if number == "Ace":
                deckval[card] = 11
            else:
                deckval[card] = 10
    return deckval
    # print(deckval)

def initHands():
    for i in range(2):
        playerHand.append(shuffledDeck.pop(0))
        dealerHand.append(shuffledDeck.pop(0))

def winCheck():

    if playerVal == 21 and dealerVal != 21:
        print("You got Blackjack, you win")
        if input("Do you want to play again > ") == "no":
            return False
        else:
            return True

def bustCheck(playerVal):
    if playerVal > 21:
        if any("Ace" in card for card in playerHand):
            playerVal -= 10
            return False
        else:
            return True

if __name__ == '__main__':
    print("Welcome to Blackjack")
    # Initialize Variables
    play = True
    deck = createDeck()
    deckValues = deckVals(deck)
    # Keep running while player wants to play
    while play is True:
        # Initialize conditions
        hit = True
        bust = False
        win = False
        #Shuffle the deck and initialize hands
        shuffledDeck = deck.copy()
        random.shuffle(shuffledDeck)
        playerHand = []
        dealerHand = []
        initHands()
        playerVal = sum(deckValues[val] for val in playerHand)
        dealerVal = sum(deckValues[val] for val in dealerHand)
        bustCheck(playerVal)
        if winCheck():
            continue
        if winCheck() is False:
            play = False
            break
        print("Player Hand: %s" % playerHand)
        print("Dealer's First Card: %s" % dealerHand[0])
        print("Player Value: %s" % playerVal)
        while hit and not bust:
            response = input("Hit or stand > ").lower()
            if response == "hit":
                playerVal += deckValues[shuffledDeck[0]]
                playerHand.append(shuffledDeck.pop())
                print("Player hand: %s " % playerHand)
                print("Player value: %s " % playerVal)
                if bustCheck(playerVal):
                    print("You busted!")
                    if input("Play again? > ") == "yes":
                        bust = True
                        break
                    else:
                        play = False
                        bust = True
                        break
                else:
                    continue
            if response == "Stand" or response == "stand":
                print("Stand")
                break
        if not play:
            break
        if bust:
            continue
        print("Dealer Hand: %s " % dealerHand)
        print("Dealer Value: %s " % dealerVal)
        while dealerVal < 17:
            dealerVal += deckValues[shuffledDeck[0]]
            dealerHand.append(shuffledDeck.pop())
            print(dealerHand)
            print(dealerVal)
            if(bustCheck(dealerVal)):
                print("Dealer busted! You win")
                if input("Play again? > ") == "yes":
                    win = True
                    break
                else:
                    play = False
                    break
            else:
                continue
        print("Player Value: %s " % playerVal)
        print("Dealer Value: %s " % dealerVal)
        if playerVal > dealerVal:
            print("You win!")
            if input("Play again? > ") == "yes":
                win = True
                break
            else:
                play = False
                break
        if not play:
            break
        if win:
            continue