from random import randint


user_board = [[' '] * 8 for x in range(8)]

computer_board = [[' '] * 8 for x in range(8)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}

def print_board(board):
    print('A B C D E F G H')
    print('----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    for ship in range(8):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'x':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'x'

def play_game():
    pass

def valid_coordinates():
    pass

def make_choice():
    pass

def new_game():
    pass


