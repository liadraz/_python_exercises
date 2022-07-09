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


def ask_hit_or_stand():
    """
    Asks the player whether he wants to Hit or Stand
    :return: string 'HIT', or 'STAND'.
    """
    while True:
        action = input("Would you like to 'Hit' or 'Stand'?\nEnter H or S")
        if action[0].upper == 'H':
            return "HIT"
        elif action[0].upper == 'S':
            return "STAND"
        else:
            print("Sorry, please try again.")


def show_some(player_, dealer_):
    """
    Show all player's cards, and only one card of the dealer.
    """
    print(player_)
    print(dealer_.cards[0])


def show_all(player_, dealer_):
    """
    Show all cards on table, and each hand's total value.
    """
    print(player_)
    print(dealer_)


# Functions handle end of game scenarios
def player_busts(chips_):
    print("Player busts!")
    chips_.lose_bet()


def player_wins(chips_):
    print("Player wins!")
    chips_.win_bet()


def dealer_busts(chips_):
    print("Dealer busts!")
    chips_.win_bet()


def dealer_wins(chips_):
    print("Dealer wins!")
    chips_.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")



def replay():
    """
    :return: boolean
    """
    while True:
        answer = input("Would you like to play again? Enter Yes or No")
        if answer[0].upper == 'Y':
            return True
        elif answer[0].upper == 'N':
            return False
        else:
            print("Sorry, please try again.")


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
        place_bet(player_chips)

        # Show some cards. Keep one dealer card hidden
        show_some(player, dealer)

        #
        # Start a round
        is_round = True
        while is_round:

            #
            # Player's turn
            # Prompt for player to Hit or Stand
            action = ask_hit_or_stand()

            if "HIT" == action:
                hit(deck, player)

            # Show cards. Keep one dealer card hidden
            show_some(player, dealer)
            # Invoke here adjust_for_ace() ?!
            # If player's hand exceeds 21 player busted
            if player.value > 21:
                player_busts(player_chips)

                is_round = False

            #
            # Dealer's turn
            if "STAND" == action:
                show_all(player, dealer)

                # Dealer plays until reaches 17
                hit(deck, dealer)

        # Inform player's total chips and cards.
        show_all(player, dealer)
        print(player_chips)

        # Ask to play again
        is_round = replay()


