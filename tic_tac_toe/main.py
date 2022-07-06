#
# Simple TicTacToe Project game

import os
import random

# Definitions
g_board = [' '] * 9


# display board
def display_board(board_):
    print('\n')
    print('\t   |   |   ')
    print(f'\t {g_board[6]} | {g_board[7]} | {g_board[8]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {g_board[3]} | {g_board[4]} | {g_board[5]} ')
    print('\t   |   |   ')
    print('\t-------------')
    print('\t   |   |   ')
    print(f'\t {g_board[0]} | {g_board[1]} | {g_board[2]} ')
    print('\t   |   |   ')


# player first input
def player_input():
    mark = input('Do you want to be X ot O? ')

    # random which player will play first
    print(f'Player {num} will go fisrt.')


# update board, place marker
def place_marker(board_, marker_, position_):
    pass


# win check
def win_check(board_, mark_):
    pass


# choose who plays first
def choose_first():
    pass


# space check
def space_check(board_, position_):
    """
    return: boolean. Is space available on position
    """
    pass


# full_board_check
def full_board(board_):
    """
    return: boolean. Checks if board is full
    """
    pass


# player choice
def player_choice(board_):
    pass


# replay the game
def replay():
    pass


# main function - Run the game
def run():
    print('Welcome to Tic Tac Toe')
    is_run = True

    while is_run:

        # Ask the player which mark he wants to play
        # player_input()

        input('Are you ready to play? Enter yes or no. ')

