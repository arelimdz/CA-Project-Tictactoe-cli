from pprint import pprint
from win_checker import is_winning_move
from is_valid_user_input import is_valid_user_input
from format_board import format_board
from build_board import build_board
from has_board_space import has_space


# TODO: Load from settings file
num_rows = 3
num_columns = 3
target = 3


def main_game_loop(num_rows, num_columns, target):
    board_size = num_columns * num_rows
    # Create board
    board = build_board(num_rows, num_columns)
    print(board)

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

    # Set values for check winner
    horizontal_offsets = (0, -1), (0, 1)
    vertical_offsets = (-1, 0), (1, 0)
    forward_diagonal_offsets = (1, -1), (-1, 1)  # / diagonal
    backward_diagonal_offsets = (-1, -1), (1, 1)  # \ diagonal

    all_offsets = [
        horizontal_offsets,
        vertical_offsets,
        forward_diagonal_offsets,
        backward_diagonal_offsets,
    ]

    # Call formated board
    board_string = format_board(board)

    # is game over
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
        for offsets in all_offsets:
            left_offset, right_offset = offsets
            if is_winning_move(
                board,
                move,
                current_marker,
                target,
                left_offset,
                right_offset,
            ):
                print(f"WINNER {markers[current_marker_index]}")
                print(format_board(board))
                is_game_over = True
                break

        # Check if board has more empty spaces
        if not has_space(board):
            print("GAME OVER!!! Nobody wins!")
            break

        current_marker_index = (current_marker_index + 1) % len(markers)


main_game_loop(num_rows, num_columns, target)
