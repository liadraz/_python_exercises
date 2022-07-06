#
# Simple TicTacToe Project game

import os
import random


# display board
def display_board(board_):
    print('\n')
    print('\t   |   |   ')
    print(f'\t {board_[7]} | {board_[8]} | {board_[9]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {board_[4]} | {board_[5]} | {board_[6]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {board_[1]} | {board_[2]} | {board_[3]} ')
    print('\t   |   |   ')
    print('\n')


# player chose mark X or O
def player_input():
    marker = ''

    # Get mark from user and validate the input
    while not ('X' == marker or 'O' == marker):
        marker = input('Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# update board, place marker
def place_marker(board_, marker_, position_):
    board_[position_] = marker_


# win check
def win_check(board_, mark_):
    # check wins in vertical, horizontal and in cross
    return board_[1] == board_[2] == board_[3] == mark_ or \
    board_[4] == board_[5] == board_[6] == mark_ or \
    board_[7] == board_[8] == board_[9] == mark_ or \
    board_[1] == board_[4] == board_[7] == mark_ or \
    board_[2] == board_[5] == board_[8] == mark_ or \
    board_[3] == board_[6] == board_[9] == mark_ or \
    board_[7] == board_[5] == board_[3] == mark_ or \
    board_[9] == board_[5] == board_[1] == mark_


# choose who plays first
def choose_first():
    if random.randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# space check
def space_check(board_, position_):
    """
    return: boolean. Is space available on position
    """
    return board_[position_] == ' '


# full_board_check
def full_board(board_):
    """
    return: boolean. Checks if board is full
    """
    for i in range(0, 9):
        if space_check(board_, i):
            return False

    return True


# player choice
def player_choice(board_):
    acceptable_range = list(range(1, 10))
    choice = 0

    while choice not in acceptable_range or not space_check(board_, choice):
        choice = int(input("Choose your next position: (1-9) "))

    # NOTE choice is in range 1-9. Hence, the minus 1
    return choice


# replay the game
def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')


# main function - Run the game
def run():
    print('\t<<< Welcome to Tic Tac Toe >>>')
    print('\t<<< ---------------------- >>>\n')

    # Start running the Game
    while True:
        # Reset The board
        board = ['#'] + [' '] * 10

        # Ask the player which mark he wants to play
        player1_marker, player2_marker = player_input()

        # Who will start the gmae
        turn = choose_first()
        print(f'\n{turn} will go first.')

        # Get input from the user to start the game
        ask_ready = input('>>> Are yor ready to play? \tEnter yes or no. ').lower()
        if ask_ready[0] == 'y':
            is_game_on = True
        else:
            is_game_on = False

        # Start the game
        while is_game_on:
            os.system("clear")

            display_board(board)
            position = player_choice(board)

            if 'Player 1' == turn:
                # Player's 1 turn
                place_marker(board, player1_marker, position)

                if win_check(board, player1_marker):
                    os.system("clear")
                    display_board(board)
                    print("Congratulations! You Have won the game!")
                    is_game_on = False

                elif full_board(board):
                    os.system("clear")
                    display_board(board)
                    print("The game is a draw! ")
                    is_game_on = False

                turn = 'Player 2'

            else:
                # Player's 2 turn
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print("Congratulations! You Have won the game!")
                    is_game_on = False
                elif full_board(board):
                    display_board(board)
                    print("The game is a draw! ")
                    is_game_on = False

                turn = 'Player 1'

        # check if the user wants to play again
        if not replay():
            break


run()