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
        board[ship_row][ship_column] = 'X'

def play_game():
    pass

def valid_coordinates():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print("Please select a valid number between 1 and 8 inclusive")
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print("Please choose a valud option between A and H inclusive")
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]
  
def ships_sunk(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def new_game():
    pass


