from pprint import pprint
from win_checker import is_winning_move
from is_valid_user_input import is_valid_user_input
from format_board import format_board

# Define board size
# TODO: Load from settings file
num_rows = 20
num_columns = 20
target = 2


# Create board
board = []
for row_index in range(num_rows):
    board.append([None] * num_columns)


def main_game_loop(num_rows, num_columns, target):
    board_size = num_columns * num_rows

    board = []
    for row_index in range(num_rows):
        board.append([None] * num_columns)

    #  Get input from player and verify if valid
    def get_valid_position(board):
        while True:
            position = input("Please, enter your move: ")
            valid_position, error = is_valid_user_input(board, position)
            if error:
                print(error)
            elif valid_position is not None:
                return valid_position

    markers = ["X", "O"]
    current_marker_index = 0
    game_round = 1
    # Game Loop

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

    board_string = format_board(board)
    print(board_string)


    is_game_over = False
    while not is_game_over:
        formatted_board = format_board(board)
        print(formatted_board)
        r, c = get_valid_position(board)

        current_marker = markers[current_marker_index]
        # update board
        board[r][c] = current_marker
        # Switch player
        move = (r, c)
        print(move)

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
                print_board(board)
                is_game_over = True
                break

        has_more_moves = False
        for row in board:
            for value in row:
                if value is None:
                    has_more_moves = True
                    break

        if not has_more_moves:
            print("GAME OVER!!! Nobody wins!")
            break

        current_marker_index = (current_marker_index + 1) % len(markers)


main_game_loop(num_rows, num_columns, target)
