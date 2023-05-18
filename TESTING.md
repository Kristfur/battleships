# Categories
* [Game Functions](#game-functions)
* [Input Validation](#input-validation)
    * [Want to See the Rules](#want-to-see-the-rules)
    * [Select Board Size](#select-board-size)
    * [Place Ship Coordinate](#place-ship-coordinate)
    * [Place Ship Direction](#place-ship-direction)
    * [Play Again](#play-again)
* [Computer Smart Guess](#computer-smart-guess)

# Game Functions
Throughout development, every function was thoroughly tested to ensure the function will do what it was designed to do. After each function was created, I ran multiple tests with a range of acceptable values to ensure the function performed correctly.

# Input Validation
Every function was tested to ensure they function correctly with the correct values. Sometimes users can enter incorrect values. Input validation ensures the user enters correct values, so the program functions can receive acceptable values.

All inputs are automatically put into lowercase using the method .lower() for easily identifying the intended input.

## Want to See the Rules

|Description|Step|Step Description|Expected Result|Actual Result|Pass\Fail
|-|-|-|-|-|-
|Input is checked to ensure it is a valid input|1|Run game, and wait for it to ask if you would like to see the rules
| |2|Type 'n'|Game proceeds to select board size question|As expected|Pass
| |3|Type 'y'|Game proceeds to show the rules|As expected|Pass
| |4|Type 'hello'|Informs user that their answer is invalid and prompts them to try again|As expected|Pass

## Select Board Size

|Description|Step|Step Description|Expected Result|Actual Result|Pass\Fail
|-|-|-|-|-|-
|Input is checked to ensure it is a valid input|1|Run game, and navigate to the select board size question
| |2|Type 's'|Game proceeds to place ship section with a small board|As expected|Pass
| |3|Type 'm'|Game proceeds to place ship section with a medium board|As expected|Pass
| |4|Type 'l'|Game proceeds to place ship section with a large board|As expected|Pass
| |5|Type 'hello'|Informs user that their answer is invalid and prompts them to try again|As expected|Pass

## Place Ship Coordinate

|Description|Step|Step Description|Expected Result|Actual Result|Pass\Fail
|-|-|-|-|-|-
|Input is checked to ensure it is a valid input|1|Run game, and navigate to the place ship section
| |2|Type x : '0' y : '0'|Game proceeds to ask for ship direction|As expected|Pass
| |3|Type x : '100' y : '100'|Informs user that their answer is not on the grid and prompts them to try again|As expected|Pass
| |4|Type x : 'hello' y : 'hello'|Informs user that their answer is not a number and prompts them to try again|As expected|Pass
| |5|Place a ship at (0, 0, s)|
| |6|Type x : '0' y : '0'|Informs user that the coordinates are already occupied by one of their ships, and prompts them to try again|As expected|Pass
| |7|Place two ships, one at (0, 1, s) and the other at (1, 0, e)|Results in the tile (0, 0) being empty, but all of it's neighbours are occupied
| |8|Type x : '0' y : '0'|Informs user that the area they selected is too small for a ship to fit inside, and prompts them to try again|As expected|Pass

## Place Ship Direction
|Description|Step|Step Description|Expected Result|Actual Result|Pass\Fail
|-|-|-|-|-|-
|Input is checked to ensure it is a valid input|1|Run game, and naviagte to the place ship section. Place a ship at (0, 0), wait for game to ask you for the ship direction.
| |2|Type 'n'|Informs user that the ship cannot be placed outside the board, and prompts them to try again|As expected|Pass
| |3|Type 'e'|Game proceeds to place ship|As expected|Pass
| |4|Type 's'|Game proceeds to place ship|As expected|Pass
| |5|Type 'w'|Informs user that the ship cannot be placed outside the board, and prompts them to try again|As expected|Pass
| |6|Type x : 'hello' y : 'hello'|Informs user that their answer is not valid and prompts them to try again|As expected|Pass
| |7|Place a ship at (1, 0, s)
| |8|Try to places ship at (0, 0, e)|Informs user that the ship cannot be placed because it intersects another ship at (1, 0), and prompts them to try again|As expected|Pass

## Play Again
|Description|Step|Step Description|Expected Result|Actual Result|Pass\Fail
|-|-|-|-|-|-
|Input is checked to ensure it is a valid input|1|Play game to the end, and wait for it to ask if you would like to play again
| |2|Type 'n'|Program terminates|As expected|Pass
| |3|Type 'y'|Game adds the scores to the counter, and proceeds to the select board size question|As expected|Pass
| |4|Type 'hello'|Informs user that their answer is invalid and prompts them to try again|As expected|Pass

# Computer Smart Guess
As the computer guesses cannot be manipulated by the user and is 'random', I had to play the game and try to predict all of the outcomes for the computer's guesses. In every scenario that came up during testing, the computer behaved as it was expected to.

Here is how the computer is supposed to behave:
- If there are no revealed hit marks on the board, guess randomly
- If all the neighboring cells of all of the revealed hit marks on the board are misses, guess randomly
- For every hit mark on the board, randomly choose one and randomly guess one if it's unguessed neighboring tiles. If all neighboring tiles have been guessed before, try the next hit mark int the list.

This results in the computer's guesses clustering around hit marks, mimicking what a humans would do when the reveal a hit. This enhances the gaming experience as it makes for a more challenging opponent.
