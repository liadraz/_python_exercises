"""
*** BlackJack Card Game ***
Practicing OOP in python
Classes definitions
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
    'Eight': 8, 'Nine': 9, 'Ten': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}


# CARD
class Card:
    """
    Holds a single Card variation.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = g_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# DECK
class Deck:
    """
    A Deck of full 52 cards pack
    """
    def __init__(self):
        self.deck = []

        # Create a new deck with 52 cards
        for suit in g_suits:
            for rank in g_ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_cards = ''

        for card in self.deck:
            deck_cards += f'\n{card}'

        return f'The deck has : {deck_cards}'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# HAND
