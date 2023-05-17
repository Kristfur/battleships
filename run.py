from random import randint
import random


class Board:
    """
    Main board class. Sets board size, type (computer or user), number and
    types of ships. Has methods for adding ships, making guesses and 
    printing the board
    """

    def __init__(self, size, ships, type):
        self.size = size
        self.board = [["\u2610" for x in range(size)] for y in range(size)]
        self.type = type
        self.guesses = []
        self.ship_coords = []

    # Print board to screen
    def print(self):
        # Print compass for user to easily identify the direction
        print("  N")
        print("W + E")
        print(f"  S    {self.type}")
        num = "  "
        # Print numbers along the x and y axis for easy 
        # coordinate identification
        for c in range(self.size):
            num += f'{c} '
        print(num)
        num = 0
        for row in self.board:
            r = ""
            for c in range(self.size):
                r += row[c] + " "
            print(f'{num} {r}')
            num += 1

    # Add guess to board, return confirmation if ship was hit
    def guess(self, x, y):
        self.guesses.append((x, y))

        if (x, y) in self.ship_coords:
            self.board[y][x] = 'X'
            return 'Hit!'
        else:
            self.board[y][x] = '\u2B1E'
            return 'Miss!'

    # Add ship to board, if it is player's board, show ships on board
    def add_ship(self, lenght, x, y, dirX, dirY):
        for segment in range(lenght):
            self.ship_coords.append(
                (x + (dirX * segment), y + (dirY * segment)))
            if self.type == 'player':
                self.board[y + (dirY * segment)][x +
                                                 (dirX * segment)] = '\u25A6'


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
    Gets input for position of ship, and calls board.add_ship
    """
    x = 0
    y = 0
    direction = ''
    if board.type == 'player':  
        print(f'You are placing a ship of length {ship_length}')
        print('Choose a coordinate for one end of the ship')

        # Get player's coordinate input and verify it
        while True:
            x = input('x : ')
            y = input('y : ')

            if validate_coords(x, y, ship_length, board):
                break

        # Get player's direction input and verify it
        while True:
            direction = input(
                'Please choose the direction you want to place your ship (N, E, S, W)\n').lower()

            if validate_direction(direction, int(x), int(y), ship_length, board, False):
                break

    elif board.type == 'computer':
        # Get computer's coordinate input and verify it
        while True:
            x = str(randint(0, board.size - 1))
            y = str(randint(0, board.size - 1))
            if validate_coords(x, y, ship_length, board):
                break

        # Get computer's direction input and verify it
        while True:
            direction = randint(0, 3)
            if direction == 0:
                direction = 'n'
            elif direction == 1:
                direction = 'e'
            elif direction == 2:
                direction = 's'
            else:
                direction = 'w'

            if validate_direction(direction, int(x), int(y), ship_length, board, False):
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
        if (x >= board.size or y >= board.size) or (x < 0 or y < 0):
            raise ValueError(f'The coordinate ({x}, {y}) is not on the board. The board ranges from (0, 0) to ({board.size - 1}, {board.size - 1})')      
        elif (x, y) in board.ship_coords:
            raise ValueError(f'The coordinate ({x}, {y}) is already occupied by one of your ships')      
        
        # Check if ship can be placed in any direction from selected coordinate
        # Stops ships being cornered in
        d = ['n', 'e', 's', 'w']
        c = 0
        while True:
            if validate_direction(d[c], x, y, ship_length, board, True):
                break
            if c >= 3:
                raise ValueError(f'The area you selected is too small for the ship to fit')
            c += 1

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_direction(direction, x, y, ship_length, board, is_silent):
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
                if (x + (dirX * segment) >= board.size or y + (dirY * segment) >= board.size) or (x + (dirX * segment) < 0 or y + (dirY * segment) < 0):
                    # Blocked by edge of board
                    raise ValueError(f'Ship cannot be placed outside the game board')
                elif (x + (dirX * segment), y + (dirY * segment)) in board.ship_coords:
                    # Blocked by another boat
                    raise ValueError(f'{direction} is blocked by a ship at ({x + (dirX * segment)}, {y + (dirY * segment)})')
    except ValueError as e:
        if (not is_silent):
            print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def make_guess(board):
    """
    Get the coordinates for a guess
    """
    if board.type == 'computer':
        # Player's guess
        print("It's your turn to guess!")
        while True:
            x = input('x : ')
            y = input('y : ')

            if compute_guess_result(x, y, board, False):
                break
    else:
        # Computer's guess
        print("It's the computer's turn to guess!")
        computer_smart_guess(board)


def compute_guess_result(x, y, board, is_computer):
    """
    Validate guess coordinates, and update game board
    """
    try:
        if not is_computer:
            if not x.isnumeric() or not y.isnumeric():
                raise ValueError(f'The coordinate ({x}, {y}) is not a number')
        x = int(x)
        y = int(y)
        if (x >= board.size or y >= board.size) or (x < 0 or y < 0):
            raise ValueError(f'The coordinate ({x}, {y}) is not on the board. The board ranges from (0, 0) to ({board.size}, {board.size})')      
        elif (x, y) in board.guesses:
            raise ValueError(f'The coordinate ({x}, {y}) has already been guessed')      

    except ValueError as e:
        if not is_computer:
            print(f"Invalid data: {e}, please try again.\n")
        return False

    # Update board
    if is_computer:
        print(f'The computer guessed ({x}, {y}).')
    print(f'{board.guess(x, y)}\n')
    return True


def computer_smart_guess(board):
    """
    Use previous hits to work out likely coordinates for the next guess. 
    Otherwise, guess random coordinates
    """
    direction = ['n', 'e', 's', 'w']
    random.shuffle(direction)
    # for each X on board, guess 4 neighbours
    #     if two x in row, guess next square in line
    # else, return empty and use random coords
    row = 0
    for r in board.board:
        col = 0
        for cell in r:
            if cell == "X":
                # If cell is a 'X', check it's neighbours
                for d in direction:
                    if d == 'n' and row >= 1:
                        if board.board[row - 1][col] == "\u2610" or board.board[row - 1][col] == "\u25A6":
                            compute_guess_result(col, row - 1, board, True)
                            return
                    elif d == 'e' and col < board.size - 1:
                        if board.board[row][col + 1] == "\u2610"  or board.board[row][col + 1] == "\u25A6":
                            compute_guess_result(col + 1, row, board, True)
                            return
                    elif d == 's' and row < board.size - 1:
                        if board.board[row + 1][col] == "\u2610"  or board.board[row + 1][col] == "\u25A6":
                            compute_guess_result(col, row + 1, board, True)
                            return
                    elif d == 'w' and col >= 1:
                        if board.board[row][col - 1] == "\u2610"  or board.board[row][col - 1] == "\u25A6":
                            compute_guess_result(col - 1, row, board, True)
                            return
            col += 1
        row += 1

    # Choose random coordinates
    while True:
        x = randint(0, board.size - 1)
        y = randint(0, board.size - 1)
        if compute_guess_result(x, y, board, True):
            break
    return


def check_for_win(board):
    """
    Check board if all ship coordinates have been guessed, returns True or False
    """        
    for segment in board.ship_coords:
        if segment not in board.guesses:
            return False
    return True


def win_game(winner):
    """
    Print win/lose screen depending on the winner
    """
    if winner % 2 == 0:
        print('Congratulations! You Win!')
    else:
        print('You lost all your battleships')
    play_again(winner)


def play_again(winner):
    """
    Ask user if they would like to play again
    """
    while True:
        answer = input('Would you like to play again?\n').lower()
        if validate_answer(answer):
            if answer == 'n' or answer == 'no':
                print('\nExiting the program\nThank You for playing')
                quit()
            else:
                break
    run_game(winner)


def validate_answer(answer):
    """
    Validata user's response
    """
    valid_answers = ['y', 'yes', 'n', 'no']
    try:
        if (answer not in valid_answers):
            raise ValueError(f'{answer} is not a valid answer')
    except ValueError as e:
        if (not is_silent):
            print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def game_loop(player_board, computer_board):
    """
    Main game loop
    """
    turn = randint(0, 1)  # even = player, odd = computer
    while True:
        if turn % 2 == 0:
            # Player's turn
            make_guess(computer_board)
            computer_board.print()
            is_win = check_for_win(computer_board)
            if is_win:
                win_game(turn)
                break
        else:
            # Computer's turn
            # get_computer_guess()
            make_guess(player_board)
            player_board.print()
            is_win = check_for_win(player_board)
            if is_win:
                win_game(turn)
                break
        turn += 1


def run_game(winner):
    """
    Set up game
    """
    if type(winner) == int:
        # Increase score counter, if user is playing again
        scores[winner % 2] += 1
    else:
        # Print introduction if it is first game of session
        introduction()

    # Print scores
    print(f'Scores: Player: {scores[0]}  --  Computer: {scores[1]}')

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
            print('player')
            place_ship(player_board, int(ship_length))
            print('computer')
            place_ship(computer_board, int(ship_length))
            player_board.print()

    game_loop(player_board, computer_board)


scores = [0, 0]
if __name__ == '__main__':
    run_game('start')
