"""
War Card Game
Practicing OOP in python
"""

from classes import *

HALF_DECK = 26

#
# GAME SETUP

player_one = Player("One")
player_two = Player("Two")

# Create a new deck
new_deck = Deck()
new_deck.shuffle()

# Split the hole deck to both players
for i in range(HALF_DECK):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# MAIN LOOP
