"""
*** BlackJack Card Game ***
Practicing OOP in python
Main function - Implementation
"""


def take_bet():
    """
    NOTE User must have enough chips to make a bet
    :return: integer
    """
    pass


def hit(deck_, hand_):
    """
    Thid function will be called during gameplay
    anytime a Player requests a hit, or a Dealer's hand is
    less than 17
    """
    pass


def hit_or_stand(deck_, hand_):
    """
    Asks the player whether her wants to Hit or Stand
    :return: key 'HIT', or 'STAND'.
    """


def show_some(player_, dealer_):
    """
    Shows only Player's cards, the dealer's first card is hidden. Happens when the game starts,
    and after each time Player takes a card.
    """
    pass


def show_all(player_, dealer_):
    """
    Show all cards, and each hand's total value
    """
    pass


# Functions handle end of game scenarios

def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


# The main gameplay function
def game_play():

    while True:
        # Print an opening statement

        # Create & shuffle the deck

        # deal two cards to each player

        # Set up the Player's chips

        # Prompt the player for their bet

        # Show cards. Keep one dealer card hidden

        while is_playing:
            # Prompt for player to Hit or Stand

            # Show cards. Keep one dealer card hidden

            # If player's hand exceeds 21, run player_busts()
            # and break up the loop

            # If player hasn't busted, play dealer's hand until Dealer reaches 17

                # Show all cards
                # Run different winning scenarios

            # Inform Player of their chips total

            # Ask to play again
