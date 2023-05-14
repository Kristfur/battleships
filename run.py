
class Board:
    """
    Main board class. Sets board size, type (computer or user), number and
    types of ships. Has methods for adding ships, making guesses and 
    printing the board
    """

    def __init__(self, size, ships, type):
        self.size = size
        self.board = [["\u2610" for x in range(size)] for y in range(size)]
        self.ships = []
        self.type = type
        self.guesses = []
        self.ship_coords = []

    # Print board to screen
    def print(self):
        print("  N")
        print("E + W")
        print("  S")
        num = "  "
        for c in range(self.size):
            num += f'{c}  '
        print(num)
        num = 0
        for row in self.board:
            r = ""
            for c in range(self.size):
                r += row[c] + "  "
            print(f'{num} {r}\n')
            num += 1

    # Add guess to board, return confirmation if ship was hit
    def guess(self, x, y):
        self.guesses.append((x, y))

        if (x, y) in self.ship_coords:
            self.board[x][y] = '\u25A3'
            return 'Hit'
        else:
            self.board[x][y] = '\u25A0'
            return 'Miss'

    # Add ship to board, if it is player's board, show ships on board
    def add_ship(self, lenght, x, y, dirX, dirY):
        for segment in range(lenght):
            self.ship_coords.append(
                (x + (dirX * segment), y + (dirY * segment)))
            if self.type == 'player':
                self.board[y + (dirY * segment)][x + (dirX * segment)] = '\u25A6'


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


def place_ship(board, ship_length):
    """
    Gets input for position of ship, and places ship
    """
    if board.type == 'player':
        print(f'You are placing a ship of length {ship_length}')
        print('Choose a coordinate for one end of the ship')

        while True:
            x = input('x : ')
            y = input('y : ')

            if validate_coords(x, y, ship_length, board):
                break

        direction = ''
        while True:
            direction = input(
                'Please choose the direction you want to place your ship (N, E, S, W)\n').lower()

            if validate_direction(direction, int(x), int(y), ship_length, board):
                break
        # Valid coordinates, add ship to board
        dirX = 0
        dirY = 0
        if (direction == 'n' or direction == 'north'):
            dirY = -1
        elif (direction == 'e' or direction == 'east'):
            dirX = 1
        elif (direction == 's' or direction == 'south'):
            dirY = 1
        elif (direction == 'w' or direction == 'west'):
            dirX = -1

        board.add_ship(ship_length, int(x), int(y), dirX, dirY)


def validate_coords(x, y, ship_length, board):
    """
    Validate selected coordinates
    """
    try:
        if not x.isnumeric() or not y.isnumeric():
            raise ValueError(f'The coordinate ({x}, {y}) is not a number')
        x = int(x)
        y = int(y)
        if (x > board.size or y > board.size) or (x < 0 or y < 0):
            raise ValueError(f'The coordinate ({x}, {y}) is not on the board. The board ranges from (0, 0) to ({board.size}, {board.size})')      
        elif (x, y) in board.ship_coords:
            raise ValueError(f'The coordinate ({x}, {y}) is already occupied by one of your ships')      
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

        # TODO Run validate_directions check with all directions before 
        # confirming valid coordinates to make sure a ship can be placed at this location
    return True


def validate_direction(direction, x, y, ship_length, board):
    """
    Validate ship direction based of the chosen coordinates
    """
    valid_directions = ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']
    try:
        if (direction not in valid_directions):
            raise ValueError(f'{direction} is not a valid direction')
        else:
            dirX = 0
            dirY = 0
            if (direction == 'n' or direction == 'north'):
                dirY = -1
            elif (direction == 'e' or direction == 'east'):
                dirX = 1
            elif (direction == 's' or direction == 'south'):
                dirY = 1
            elif (direction == 'w' or direction == 'west'):
                dirX = -1

            for segment in range(ship_length):
                if (x + (dirX * segment) > board.size or y + (dirY * segment) > board.size) or (x + (dirX * segment) < 0 or y + (dirY * segment) < 0):
                    # Blocked by wall
                    raise ValueError(f'Ship cannot be placed outside the game board')
                elif (x + (dirX * segment), y + (dirY * segment)) in board.ship_coords:
                    # Blocked by boat
                    raise ValueError(f'{direction} is blocked by a ship at ({x + (dirX * segment)}, {y + (dirY * segment)})')
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

        # TODO Run validate_directions check with all directions before 
        # confirming valid coordinates to make sure a ship can be placed at this location
    return True


def run_game():
    introduction()
    board_size = get_board_size()
    grid = 0
    all_ships = []

    # Get grid length from selected board size
    # all_ships represents the number of each type of ship in play
    # all_ship{'ship_length' : ship_count}

    if board_size == 's' or board_size == 'small':
        grid = 5
        all_ships = {'5': 0, '4': 0, '3': 1, '2': 2}
    elif board_size == 'm' or board_size == 'medium':
        grid = 8
        all_ships = {'5': 0, '4': 1, '3': 2, '2': 2}
    elif board_size == 'l' or board_size == 'large':
        grid = 10
        all_ships = {'5': 1, '4': 1, '3': 2, '2': 3}

    # Create player and computer board
    player_board = Board(grid, all_ships, 'player')
    computer_board = Board(grid, all_ships, 'computer')

    # Place each ship individually, ships are different sizes
    for ship_length in all_ships:
        for _ in range(all_ships[ship_length]):
            place_ship(player_board, int(ship_length))
            place_ship(computer_board, int(ship_length))
            player_board.print()


run_game()
