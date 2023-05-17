# Battleships

Battleships is a strategy guessing game where two players go head-to-head trying to sink the oppontnts ships before their ships are sunk. It is played on a grid of squares where each player takes turns guessing a coordinate on the grid, and the other player responds with 'Hit' or 'Miss'. The first player to correctly guess the position of the opposing player's ship is the winner.

![Battleships Title](docs/read_me_images/feature-title.JPG)

# Table of Contents
* [User Experience](#user-experience)
    * [Site Goals](#site-goals)
    * [User Stories](#user-stories)
    * [Flow Design](#flow-design)
* [Features](#features)
    * [Features to Implement](#features-to-implement)
* [Technologies](#technologies)
* [Testing](#testing)
    * [PEP8 Validation](#pep8-validation)
    * [Unfixed Bugs](#unfixed-bugs)
    * [Notable (Fixed) Bugs](#notable-fixed-bugs)
* [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Clone the Repository Code Locally](#clone-the-repository-code-locally)
* [Credits](#credits)

# User Experience
## Site Goals
* To provide a fun strategy guessing game for the user to play in a terminal.
* To have an easy to navigate interface.
* To have a selection of game lengths for the user to choose from.

## User Stories
* As a user, I want a stratagy guessing game to play in a terminal.
* As a user, I want to play a shorter version of the game.
* As a user, I want to play a longer version of the game.
* As a user, I want my wins and losses to be tracked.

User Story:

> As a user, I want a stratagy guessing game to play in a terminal.

Acceptance Criteria:
* It should be clear that it is a game, and how to play.

Implementation:
* The first text that is displayed when the program is run is the title of the game, and then smaller text asking the user if they would like to see the rules on how to play.

User Story:

> As a user, I want to play a shorter version of the game.

> As a user, I want to play a longer version of the game.

Acceptance Criteria:
* The user should be able to change the length of the game with ease, either to a shorter version or a longer version.

Implementation:
* When the user starts the game, the first thing they are asked is the size of the board they want to play on, the smaller the board, the shorter the game is, and vice versa.

User Story:

> As a user, I want my wins and losses to be tracked.

Acceptance Criteria:
* The program should keep track of the user's wins and losses and display them to the user.

Implementation:
* After every completed game, the program keeps track of the user's wins and losses. it is displayed to them throughout the game, and is featured when they finish a game.

## Flow Design
![Flow Design](docs/read_me_images/battleships-plan.JPG)

