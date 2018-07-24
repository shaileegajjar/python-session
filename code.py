# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:20:56 2018

@author: shaileeg
"""

from enum import Enum
from enum import IntEnum
from random import *



full_deck = []
distributed_deck = []



#card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    
    

#suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

#class to hold information for playing cards
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit
        


def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))  
    return full_deck

        
 
    """      
    for i in range(0, len(full_deck)):
    print("Card:", full_deck[i].card)
    print("Suit:", full_deck[i].suit)
    """

#Draw a single card from the deck    
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)

create_deck()
distributed_deck = list(full_deck)

selected_card = draw_card(distributed_deck)
print("You drew a card:", selected_card.card, selected_card.suit)








    
    
    
    
    
    