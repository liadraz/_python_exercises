"""
War Card Game
Practicing OOP in python
"""

import random

# DEFINITIONS
# LUT of the various options of available cards
g_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
g_ranks = (
    'Two', 'Three', 'Four',
    'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace'
    )
g_values = {
    'Two': 2, 'Three': 3, 'Four': 4,
    'Five': 5, 'Six': 6, 'Seven': 7,
    'Eight': 8, 'Nine': 9, 'Ten' : 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}


# CARD
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = g_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# DECK
class Deck:

    def __init__(self):
        self.all_cards = []

        # Create a new deck with 52 cards
        for suit in g_suits:
            for rank in g_ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)


# PLAYER