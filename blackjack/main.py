"""
*** BlackJack Card Game ***
Practicing OOP in python
Main function - Implementation
"""

from classes import Card, Deck, Hand, Chip


def place_bet(chips_):
    """
    NOTE User must have enough chips to make a bet
    :return: integer
    """
    while True:
        try:
            chips_.bet = int(input("Please, Place a bet : "))
        except ValueError:
            print("Invalid input. Please provide amount.")
        else:
            if chips_.bet > chips_.total:
                print(f"Sorry, you don't have enough chips! {chips_.total}")
            else:
                break


def hit(deck_, hand_):
    """
    This function will be called during gameplay
    anytime a Player requests a hit, or a Dealer's hand is
    less than 17.
    """
    hand_.add_card(deck_.deal())
    hand_.adjust_for_ace()


def ask_hit_or_stand(deck_, hand_):
    """
    Asks the player whether he wants to Hit or Stand
    :return: key 'HIT', or 'STAND'.
    """
    pass


def show_some(player_, dealer_):
    """
    Shows only Player's cards, the dealer's first card is hidden. Happens when the game starts,
    and after each time Player takes a card.
    """
    pass


def show_all(player_, dealer_):
    """
    Show all cards on table, and each hand's total value
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


def replay():
    pass


# The main gameplay function
def game_play():

    action = ' '
    is_run = True

    while is_run:
        print('\n<~<~<~ $ Welcome To BlackJack $ >~>~~>\n')

        # Create & shuffle the deck
        deck = Deck()
        deck.shuffle()

        # Set up player and dealer
        player = Hand()
        dealer = Hand()

        # deal two cards to each player
        for i in range(2):
            player.add_card(deck.deal())
            dealer.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chip()

        # Prompt the player for their bet
        place_bet()

        # Show some cards. Keep one dealer card hidden
        show_some(player, dealer)

        #
        # Start a round
        is_round = True
        while is_round:

            #
            # Player's turn
            # Prompt for player to Hit or Stand
            action = ask_hit_or_stand(deck, player)

            if action == "Hit":
                hit(deck, player)

            # Show cards. Keep one dealer card hidden
            show_some(player, dealer)
            # Invoke here adjust_for_ace() ?!
            # If player's hand exceeds 21 player busted
            if player.value > 21:
                player_busts()
                dealer_wins()

                is_round = False

            #
            # Dealer's turn
            if action == "Stand":
                show_all(player, dealer)

                # Dealer plays until reaches 17
                hit(deck, dealer)

        # Inform player's total chips and cards.
        show_all(player, dealer)
        print(player_chips)

        # Ask to play again
        is_round = replay()


