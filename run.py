
class Board:
    """
    Main board class. Sets board size, type (computer or user), number and
    types of ships. Has methods for adding ships, making guesses and 
    printing the board
    """
    def __init__(self, size, ships, type):
        self.size = size
        self.board = [["\u2610" for x in range(size)] for y in range(size)]
        self.ships = {}
        self.type = type
        self.guesses = []
        self.ship_coords = []

    # Print board to screen
    def print(self):
        for row in self.board:
            print(row)
    
    # Add guess to board, return confirmation if ship was hit
    def guess(self, x, y):
        self.guesses.append((x, y))
        
        if (x, y) in ship_coords:
            self.board[x][y] = '\u25A3'
            return 'Hit'
        else:
            self.board[x][y] = '\u25A0'
            return 'Miss'

    # Add ship to board, if it is player's board, show ships on board
    def add_ship(self, lenght, x, y, dirX, dirY):
        for segment in range(lenght):
            self.ship_coords.append(
                (x + (dirX[0] * segment), y + (dirY[1] * segment)))
            if self.type == 'player':
                self.board[x + (dirX[0] * segment][y + (dirY[1] * segment)] = '\u25A6'


def introduction():
    """
    Print introduction and game rules
    """
    print('\nWelcome to Battleships!')
    print('Here are the rules...\n')


def get_board_size():
    """
    Get board size input from user and validate it
    """
    # List of all valid user inputs (lowercase)
    valid_sizes = ['small', 's', 'medium', 'm', 'large', 'l']
    while True:
        # Recieve input and convert it to lowercase
        # Check if input is valid, if not, inform user and try again
        try:
            size = input(
                'Please input the board size (large, medium, small)\n').lower()  
            if size not in valid_sizes:
                raise ValueError(f"{size} is not a valid size")
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return size


def run_game():
    introduction()
    board_size = get_board_size()


run_game()
