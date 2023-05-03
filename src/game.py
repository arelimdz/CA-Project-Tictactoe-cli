from pprint import pprint
from is_valid_user_input import is_valid_user_input
from format_board import format_board
from build_board import build_board
from has_board_space import has_space
from win_checker import has_player_won
from game_settings import clear_terminal


def main_game_loop(num_rows, num_columns, target):
    # Create board
    board = build_board(num_rows, num_columns)

    #  Get input from player and verify if valid
    def get_valid_position(board):
        while True:
            position = input("Please, enter your move: ")
            valid_position, error = is_valid_user_input(board, position)
            if error:
                print(error)
            elif valid_position is not None:
                return valid_position

    # Set values to choose player mark
    markers = ["X", "O"]
    current_marker_index = 0

    # Call formated board
    board_string = format_board(board)

    # Set loop for game while there is not winner
    is_game_over = False
    while not is_game_over:
        formatted_board = format_board(board)
        print(formatted_board)
        r, c = get_valid_position(board)

        # Get the mark of the current Player
        current_marker = markers[current_marker_index]

        # Marked the move in the baord position
        board[r][c] = current_marker
        move = (r, c)

        # Check for a winner
        if has_player_won(board, move, current_marker, target):
            clear_terminal()
            print(format_board(board))
            print(f"WINNER {markers[current_marker_index]}")
            is_game_over = True
            break

        # Check if board has any empty space
        if not has_space(board):
            print("GAME OVER!!! Nobody wins!")
            break

        current_marker_index = (current_marker_index + 1) % len(markers)
        clear_terminal()
