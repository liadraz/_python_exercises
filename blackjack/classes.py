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
# NOTE Ace in BlackJack can have both values 1 or 11. Depends on the hand
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
class Hand:
    """
    Class holds dealt cards of each player,
    and calculates the value of those cards.
    """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        current_hold = ''
        for card in self.cards:
            current_hold += f'{g_values[card.rank]}-{card} | '

        return f'{current_hold}\nTotal = {self.value}'

    def add_card(self, card):
        self.cards.append(card)
        self.value += g_values[card.rank]

        # Count encountered ace
        if 'Ace' == card.rank:
            self.aces += 1

    # Handle 'Ace' situation. Where it can be 1 or 11
    def adjust_for_ace(self):
        # When value exceeds above 21 convert ace value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# CHIP
class Chip:
    """
    Track of player's starting chips, bets and ongoing winnings.
    By default, user gets 100 coins
    """

    def __init__(self, total_=100):
        self.total = total_
        self.bet = 0

    def __str__(self):
        return f'\nTotal chips <{self.total}>'

    def set_bet(self, bet_):
        self.bet += bet_

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

