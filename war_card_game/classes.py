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
        self.all_cards = []

        # Create a new deck with 52 cards
        for suit in g_suits:
            for rank in g_ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# PLAYER
class Player:
    """
    Each Player object will hold a current list of cards
    A player should be able to add or remove cards from their hand.
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # A player "plays" a card from the "top" of the list.
    def remove_one(self):
        return self.all_cards.pop(0)

    # Players will add cards to the "bottom" of the list.
    def add_cards(self, new_cards):
        if type([]) == type(new_cards):
            # Multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # A single card objects
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



