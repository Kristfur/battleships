# Import random for computer guesses
from random import randint
import random

# Import os to clear terminal
import os

# Import time to slow computer's turn speed
import time

# Import colorama for colorful text in terminal
from colorama import Fore

# Import pyfiglet for fancy title
from pyfiglet import Figlet


def clear_terminal():
    """
    Clear terminal window
    """
    os.system("cls || clear")


class Board:
    """
    Main board class. Sets board size, type (computer or user), number and
    types of ships. Has methods for adding ships, making guesses and
    printing the board
    """

    def __init__(self, size, ships, type):
        self.size = size
        self.board = [
            [Fore.BLUE + "\u2610" + Fore.RESET
                for x in range(size)] for y in range(size)]
        self.type = type
        self.guesses = []
        self.ship_coords = []

    # Print board to screen
    def print(self):
        clear_terminal()
        name = "  Computer"
        if self.type == "player":
            name = "  You"
        # Print compass for user to easily identify the direction
        print("  N")
        print("W + E")
        print(f"  S\n")
        print(name)
        num = "  "
        # Print numbers along the x and y axis for easy
        # coordinate identification
        for c in range(self.size):
            num += f'{c} '
        print(num + 'x')
        num = 0
        for row in self.board:
            r = ""
            for c in range(self.size):
                r += row[c] + " "
            print(f'{num} {r}')
            num += 1
        print('y\n')

    # Add guess to board, return confirmation if ship was hit
    def guess(self, x, y):
        self.guesses.append((x, y))

        if (x, y) in self.ship_coords:
            self.board[y][x] = Fore.RED + 'X' + Fore.RESET
            return 'Hit!'
        else:
            self.board[y][x] = '\u2576'
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
    clear_terminal()
    # Print fancy title
    f = Figlet(font='big')
    print(f.renderText('BATTLESHIPS'))

    print('\nWelcome to Battleships!')
    while True:
        # Ask user if they would like to see the rules
        answer = input('Would you like to see how to play? (y/n)\n').lower()
        if validate_answer(answer):
            if answer == 'y' or answer == 'yes':
                # Display the rules
                clear_terminal()
                print(
                    "\nThe aim of the game is to sink all of your opponent's"
                    "\nbattleships before your opponent sinks all of yours.")
                print(
                    "\nYou begin by placing your ships onto the board."
                    "\nyour ships are represented by '\u25A6 '"
                    "\nThen you and your opponent will take turns guessing"
                    "\ncoordinates on the other's grid."
                    "\nIf they guess a coordinate that contains a ship"
                    "\nthat is a Hit! and it is marked with an '"
                    + Fore.RED + 'X' + Fore.RESET + "'"
                    "\nOtherwise, if they miss,"
                    "\nit will be marked with a '\u2576'")
                print(
                    "\nYou alternate turns guessing coordinates"
                    "\nuntil a winner emerges!"
                    "\nGood Luck!")
                input("\nPress Enter to continue...")
                break
            else:
                break


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
                'Please input the board size: small, medium or large'
                ' (s, m, l)\n').lower()
            if size not in valid_sizes:
                raise ValueError(f"{size} is not a valid size")
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
    clear_terminal()
    return size


def place_ship(board, ship_length):
    """
    Gets input for position of ship, and calls board.add_ship
    """
    x = 0
    y = 0
    direction = ''
    if board.type == 'player':
        print(f'\nYou are placing a ship of length {ship_length}')
        print(
            'Choose the coordinates for one end of the ship:'
            f'\n(0, 0) to ({board.size - 1}, {board.size - 1})')

        # Get player's coordinate input and verify it
        while True:
            x = input('x : \n')
            y = input('y : \n')

            if validate_coords(x, y, ship_length, board, False):
                break

        # Get player's direction input and verify it
        while True:
            direction = input(
                'Please choose the direction'
                ' you want to place your ship (N, E, S, W)\n').lower()

            if validate_direction(
                    direction, int(x), int(y), ship_length, board, False):
                break

    elif board.type == 'computer':
        # Get computer's coordinate input and verify it
        while True:
            x = str(randint(0, board.size - 1))
            y = str(randint(0, board.size - 1))
            if validate_coords(x, y, ship_length, board, True):
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

            if validate_direction(
                    direction, int(x), int(y), ship_length, board, True):
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


def validate_coords(x, y, ship_length, board, is_silent):
    """
    Validate selected coordinates
    """
    try:
        if not x.isnumeric() or not y.isnumeric():
            raise ValueError(f'The coordinate ({x}, {y}) is not a number')
        x = int(x)
        y = int(y)
        if (x >= board.size or y >= board.size) or (x < 0 or y < 0):
            raise ValueError(
                f'The coordinate ({x}, {y})'
                f' is not on the board. The board ranges from (0, 0) to'
                f' ({board.size - 1}, {board.size - 1})')
        elif (x, y) in board.ship_coords:
            raise ValueError(
                f'The coordinate ({x}, {y}) is already occupied'
                f' by one of your ships')

        # Check if ship can be placed in any direction from selected coordinate
        # Stops ships being cornered in
        d = ['n', 'e', 's', 'w']
        c = 0
        while True:
            if validate_direction(d[c], x, y, ship_length, board, True):
                break
            if c >= 3:
                raise ValueError(
                    f'The area you selected is too small for the ship to fit')
            c += 1

    except ValueError as e:
        if not is_silent:
            print(f"\nInvalid data: {e}, please try again.\n")
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
                if (x + (dirX * segment) >= board.size or
                        y + (dirY * segment) >= board.size or
                        x + (dirX * segment) < 0 or
                        y + (dirY * segment) < 0):
                    # Blocked by edge of board
                    raise ValueError(
                        f'Ship cannot be placed outside the game board')
                elif (x + (dirX * segment),
                        y + (dirY * segment)) in board.ship_coords:
                    # Blocked by another boat
                    raise ValueError(
                        f'{direction} is blocked by a ship at'
                        f' ({x + (dirX * segment)}, {y + (dirY * segment)})')
    except ValueError as e:
        if (not is_silent):
            print(f"\nInvalid data: {e}, please try again.\n")
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
            x = input('x : \n')
            y = input('y : \n')

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
            raise ValueError(
                    f'The coordinate ({x}, {y}) is not on the board. The board'
                    f' ranges from (0, 0) to ({board.size}, {board.size})')
        elif (x, y) in board.guesses:
            raise ValueError(
                    f'The coordinate ({x}, {y}) has already been guessed')

    except ValueError as e:
        if not is_computer:
            print(f"Invalid data: {e}, please try again.\n")
        return False

    # Update board
    if is_computer:
        print(f'The computer guessed ({x}, {y}).')
    time.sleep(.5)
    print(f'{board.guess(x, y)}\n')
    time.sleep(.5)
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
            if cell == Fore.RED + 'X' + Fore.RESET:
                # If cell is a 'X', check it's neighbours
                for d in direction:
                    if d == 'n' and row >= 1:
                        if (board.board[row - 1][col] ==
                                Fore.BLUE + "\u2610" + Fore.RESET or
                                board.board[row - 1][col] == "\u25A6"):
                            compute_guess_result(col, row - 1, board, True)
                            return
                    elif d == 'e' and col < board.size - 1:
                        if (board.board[row][col + 1] ==
                                Fore.BLUE + "\u2610" + Fore.RESET or
                                board.board[row][col + 1] == "\u25A6"):
                            compute_guess_result(col + 1, row, board, True)
                            return
                    elif d == 's' and row < board.size - 1:
                        if (board.board[row + 1][col] ==
                                Fore.BLUE + "\u2610" + Fore.RESET or
                                board.board[row + 1][col] == "\u25A6"):
                            compute_guess_result(col, row + 1, board, True)
                            return
                    elif d == 'w' and col >= 1:
                        if (board.board[row][col - 1] ==
                                Fore.BLUE + "\u2610" + Fore.RESET or
                                board.board[row][col - 1] == "\u25A6"):
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
    Check board if all ship coordinates have been guessed,
    returns True or False
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
        print('Congratulations! You Win!\n')
    else:
        print('You lost all your battleships\n')
    play_again(winner)


def play_again(winner):
    """
    Ask user if they would like to play again
    """
    if type(winner) == int:
        # Increase score counter
        scores[winner % 2] += 1

    print(f'Score: Player: {scores[0]}  --  Computer: {scores[1]}\n')
    while True:
        answer = input('Would you like to play again? (y/n)\n').lower()
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
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def display_game_boards(player_board, computer_board):
    """
    Display player board and computer board
    side by side for better user experience
    """
    clear_terminal()
    print(f'Score: Player: {scores[0]}  --  Computer: {scores[1]}\n')
    # Print compass for user to easily identify the direction
    print("  N")
    print("W + E")
    print(f"  S\n")

    num = " "
    board_gap = "        "
    text_gap = ""
    for _ in range(player_board.size - 1):
        text_gap += "  "
    text_gap += board_gap + " "
    print(f"  You{text_gap}Computer")
    # Print numbers along the x and y axis for easy
    # coordinate identification
    for c in range(player_board.size):
        num += f'{c} '
    print(f'{num}x{board_gap}{num}x')
    num = 0
    for row in range(player_board.size):
        r = f'{num}'
        for col in range(player_board.size):
            r += player_board.board[row][col] + " "
        r += f'{board_gap} {num}'
        for col in range(computer_board.size):
            r += computer_board.board[row][col] + " "
        print(r)
        num += 1
    print(f'y{text_gap}  y\n')


def game_loop(player_board, computer_board):
    """
    Main game loop
    """
    turn = randint(0, 1)  # even = player, odd = computer
    display_game_boards(player_board, computer_board)
    while True:
        if turn % 2 == 0:
            # Player's turn
            display_game_boards(player_board, computer_board)
            make_guess(computer_board)
            is_win = check_for_win(computer_board)
            if is_win:
                display_game_boards(player_board, computer_board)
                win_game(turn)
                break
        else:
            # Computer's turn
            # get_computer_guess()
            make_guess(player_board)
            input("Press Enter to continue...")
            display_game_boards(player_board, computer_board)
            is_win = check_for_win(player_board)
            if is_win:
                win_game(turn)
                break
        turn += 1
        time.sleep(.5)


def run_game(winner):
    """
    Set up game
    """
    if type(winner) != int:
        # Print introduction if it is first game of session
        introduction()

    # Print scores
    clear_terminal()
    print(f'Score: Player: {scores[0]}  --  Computer: {scores[1]}\n')

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
            player_board.print()
            place_ship(player_board, int(ship_length))
            place_ship(computer_board, int(ship_length))

    game_loop(player_board, computer_board)


scores = [0, 0]
if __name__ == '__main__':
    run_game('start')
