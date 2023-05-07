# TIC-TAC-TO-INFINITY

A terminal Aplicaction of the clasic Tic-Tac-Toe game with a great twist.

Created by Areli Mendoza Perez for a Project with Coder Academy.

## Link to Source Control Repository (R4)

[Tic-tac-to-Infinity GitHub Repository](https://github.com/arelimdz/tictactoe-cli)

## Code Style Guide used (R5)

This code is formatter by Black and the resulting code style is compliant with PEP 8.

## Instruction and Help

### System Requirements

To run this application user need to have Python 3 on their computer.

To check if user have python installed, use the following command:

```sh
python3 --version
```

or

```sh
python --version
```

To install the latest version of Python 3 visit the following page:

[Download Python](https://www.python.org/downloads/)

### Dependencies

1. Python 3 (Python versions 3.11 and above are officially supported)
2. pytest (for testing)
3. pytest-cov (for reporting code coverage)

### How to install application (R8)

To run this application in your computer follow the next steps:

1. Open your terminal or Git Bash.

1. Navigate to the directory where you want to store the application.

1. In your terminal, run the following command :

```sh
$ git clone git@github.com:arelimdz/tictactoe-cli.git
```

1. cd into the newly cloned directory

```sh
$ cd ./tictactoe-cli
```

1. Ensure the game is executable

```sh
$ chmod +x ./run_game.sh
```

1. Run the game:

```sh
$ ./run_game.sh
```

## Description of application

Tic-Tac-Infinity is the classic Tic-Tac-Toe game with two unique additions: Extensible and customizable.
Users can resize the game board to their desired size, set their own winning line length size, and set player names.

It continues to maintain the essence of the classic game that we all know. It requires two people to be played. It consists of alternately each one of the players makes a move in one of the available grids, trying to be the first to mark three consecutive grids with their mark.

## Application Features (R6)

### - Player vs Player Tic Tac Toe gameplay

To make tic-tac-to-infinity a more enjoyable game, I designed it as a multiplayer (2 players) game.

For this I used a function (main_game_loop) with a while loop that continuously iterates until either a winner is identified or the board out of empty spaces.

To keep my code DRY I have embedded in this main loop functions so that the application addresses one player each cycle.

The game will always start with "Player 1" marked "X", and then "Player 2" marked "O". The game will move to the next cycle only once the player in turn enters a valid position.

When the game ends, the application prompts the user for interaction and asks if they would like to play again.

### - Scalable Tic Tac Toe board size and winning line length size

This application is designed to be scalable. This means that users can create very large boards with this application (I manually test a board with a 1000x1000 grid). Such a big board requires a gigantic screen to be displayed correctly. So, thinking about the users and what would be best to improve their experience with the game, I decided to limit this scalability to a range of 2 to 20 and create a board with a maximum of 400 positions.

### - Personalised gameplay experience with configured player names



So the gameplay experience feels more personalised


### - Checking for winner

This feature allows the program to evaluate if there is a winner, thanks to the automated function that evaluates the board in each move and responds quickly either to congratulate the winner or to continue with the game.
This speed is thanks to the approach of only examining the surroundings in the range of the length of the winning line, and not the entire board.

To do this, the application uses 4 main functions that are linked together to perform the following evaluations:

1. Check if the move is a winning move (is_winning_move) :
   To do this, the function examines the positions around the position marked by the player, through two pointers that move forwards and one backwards, taking as reference the position marked by the player.

2. Check that the pointers are within the limits of the board (is_valid_pointer) :
   Because the pointers move it is necessary to check that once they reach the edges of the board they stop.
   This is possible thanks to the implementation of a function that returns False once the pointer reaches the start or end position of the row and column.

3. Check if the board is marked with the player's mark (is_mark) :
   Another important criteria for stopping pointers is to identify a position that is marked by the opposing player. Well, it would not make sense to continue moving and keep looking when the criteria to win is not met.

4. Check if the player won (has_player_won):
   It is at this point where the coordinates are pass to the is_winning_move function so that the pointers move towards the indicated directions: horizontally (left and right), vertical (up and down) and forward diagonal "/" (left-down and right-up) diagonal backwards "\"(left-up and right-down)
   To return True or False and find out if there is a winner


### - Simple to use menu system

So that players can do all of the above in a user-friendly manner

### - Load and save game settings to file between application sessions

So that players don't have to re-configure the game each session.

### - Table flipping

So that players can act anti-social and flip the table on their turn (╯°□°)╯︵ ┻━┻

### User Interaction and Experience

Screen shooots of the game

## Software Development Plan

### Control Flow Diagram

### Implementation Plan (R7)

Aqui va el Trello board
Develop an implementation plan which:

- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan.

> Your checklists for each feature should have at least 5 items.

## Testing (R15)

### How to run automated tests

Run the following in bash:

```sh
python -m venv ./.venv && \
    source ./.venv/bin/activate && \
    pip install -e . && \
    python -m pytest
```

### How to obtain a reporting of code coverage

Run the following in bash:

```sh
python -m venv ./.venv && \
    source ./.venv/bin/activate && \
    pip install -e . && \
    python -m pytest --cov=src tests/
```
