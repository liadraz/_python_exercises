"""
War Card Game
Practicing OOP in python
"""

from classes import Card, Player, Deck

HALF_DECK = 26


def war_game():
    #
    # GAME SETUP
    player1 = Player("One")
    player2 = Player("Two")

    # Create a new deck
    new_deck = Deck()
    new_deck.shuffle()

    # Split the hole deck to both players
    for i in range(HALF_DECK):
        player1.add_cards(new_deck.deal_one())
        player2.add_cards(new_deck.deal_one())

    #
    # MAIN LOOP
    game_on = True
    round_counter = 0

    while game_on:
        round_counter += 1
        print(f"Round {round_counter}")

        # Checks if one of the players lost
        if len(player1.all_cards) == 0:
            print("Player One, out of cards! Player Two wins!")
            game_on = False
            break
        elif len(player2.all_cards) == 0:
            print("Player Two, out of cards! Player One wins!")
            game_on = False
            break

        # START A NEW ROUND
        player1_table_cards = []
        player1_table_cards.append(player1.remove_one())

        player2_table_cards = []
        player2_table_cards.append(player2.remove_one())

        #
        # WAR
        at_war = True

        while at_war:

            # Checks if Player One won
            if player1_table_cards[-1].value > player2_table_cards[-1].value:
                player1.add_cards(player1_table_cards)
                player1.add_cards(player2_table_cards)

                at_war = False

            # Checks if Player Two won
            elif player1_table_cards[-1].value < player2_table_cards[-1].value:
                player2.add_cards(player2_table_cards)
                player2.add_cards(player1_table_cards)

                at_war = False

            # In case of a tie
            else:
                print("WAR!")

                # Check if players have enough cards to play war
                if len(player1.all_cards) < 5:
                    print("Player One unable to declare war")
                    print("Player Two WINS!")
                    game_on = False
                    break
                elif len(player2.all_cards) < 5:
                    print("Player Two unable to declare war")
                    print("Player One WINS!")
                    game_on = False
                    break

                # In tie draw five cards from the deck
                for num in range(5):
                    player1_table_cards.append(player1.remove_one())
                    player2_table_cards.append(player2.remove_one())