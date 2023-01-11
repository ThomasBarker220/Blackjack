"""
@Today's Date : 1/6/2023

@Author : Thomas Barker
"""
import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
           "Queen", "King"]

class Deck:
    def __init__(self):
        self.cards = []
        self.create()
    def create(self):
        for number in numbers:
            for suit in suits:
                self.cards.append(number + " of " + suit)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.value = 0
    def addCard(self, card):
        self.cards.append(card)
    def handValue(self):
        for elem in self.cards:
            number = elem.split(" ")[0]
            if number.isdigit():
                self.value += int(number)
            elif number != "Ace":
                self.value += 10
            else:
                if self.value > 10:
                    self.value += 1
                else:
                    self.value += 11


if __name__ == '__main__':
    deck = Deck()
    deck.create()
    print(deck.cards)
    deck.shuffle()
    card = deck.deal()
    print(card)
    myHand = Hand()
    myHand.addCard(card)
    myHand.handValue()
    print(myHand.value)