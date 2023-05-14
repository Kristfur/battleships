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
