#
# Simple TicTacToe Project game

import os
import random


# display board
def display_board(board_):
    print('\n')
    print('\t   |   |   ')
    print(f'\t {board_[6]} | {board_[7]} | {board_[8]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {board_[3]} | {board_[4]} | {board_[5]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {board_[0]} | {board_[1]} | {board_[2]} ')
    print('\t   |   |   ')


# player chose mark X or O
def player_input():
    marker = ''

    # Get mark from user and validate the input
    while not ('X' == marker) or ('O' == marker):
        marker = input('Do you want to be X ot O? ').upper()

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
    return board_[0] == board_[1] == board_[2] == mark_ or \
    board_[3] == board_[4] == board_[5] == mark_ or \
    board_[6] == board_[7] == board_[8] == mark_ or \
    board_[0] == board_[3] == board_[6] == mark_ or \
    board_[1] == board_[4] == board_[7] == mark_ or \
    board_[2] == board_[5] == board_[8] == mark_ or \
    board_[6] == board_[4] == board_[2] == mark_ or \
    board_[8] == board_[4] == board_[0] == mark_


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
    acceptable_range = list(range(0, 9))
    choice = 10

    while choice not in acceptable_range or not space_check(board_, choice):
        choice = int(input("Choose your next position: (0-9) "))

    # NOTE choice is in range 1-9. Hence, the minus 1
    return choice - 1


# replay the game
def replay():
    return print(f"Do you want to play again? Enter Yes or No: ").lower.startwith('y')


# main function - Run the game
def run():
    print('Welcome to Tic Tac Toe')
    is_round = True

    # Start running rounds
    while is_round:

        # Reset The board
        board = [' '] * 9

        # Ask the player which mark he wants to play
        player1_marker, player2_marker = player_input()

        # Who will start the agem
        turn = choose_first()
        print(f'{turn} will go first.')

        # Get input from the user to start the game

        ask_ready = input('Are yor ready to play? Enter yes or no. ').lower()
        if ask_ready[0] == 'y':
            is_gmae_on = True
        else:
            is_gmae_on = False

        # Start the game
        while is_gmae_on:


