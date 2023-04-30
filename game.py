from pprint import pprint
from win_checker import is_winning_move

# Define board size
# TODO: Load from settings file
num_rows = 3
num_columns = 3
target = 3
board_size = num_columns * num_rows

# Create board
board = []
for row_index in range(num_rows):
    board.append([None] * num_columns)


#  Get input from player and verify if valid
def get_valid_position(board):
    while True:
        try:
            number = input("Please, enter your move: ")
            position = int(number)
            if 1 <= int(number) <= (num_rows * num_columns):
                r = row_index = (position - 1) // num_columns
                c = column_index = (position - 1) % num_columns

                if board[r][c] is not None:
                    print("Oh Oh! Spot taken!")
                    continue

                return r, c
            else:
                print(f"Please, enter a number between 1 and {board_size}: ")

        except ValueError:
            if number.isalpha():
                print(f"That is not a number! Please, enter only numbers: ")


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


def print_board(board):
    board_position = 0
    rows_to_print = []
    for row_index, row in enumerate(board):
        row_to_print = []
        for column_index, column in enumerate(row):
            board_position += 1
            value = board[row_index][column_index]
            if value is None:
                row_to_print += str(board_position)
            else:
                row_to_print += value
        rows_to_print.append("  " + "  |  ".join(row_to_print) + "\n")
    print()
    print("-----+-----+-----\n".join(rows_to_print))


is_game_over = False
while not is_game_over:
    print_board(board)
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
        print("NO ONE WINS!")
        break

    current_marker_index = (current_marker_index + 1) % len(markers)


# # result = is_winning_move(board, (2, 3), "O", 3, (-1, 0), (1, 0))  # horizontal
# # result = is_winning_move(board, (1, 1), "X", 2, (-1, 0), (1, 0))  # vertical
# result = is_winning_move(board, (2, 0), "X", 3, (1, -1), (-1, 1))  # / diagonal
# # result = is_winning_move(board, (2, 2), "X", 3, (-1, -1), (1, 1))  # \ diagonal

#     else:
#         print("Sorry spot taken. TRY AGAIN!")
#     if game_round > board_size:
#         print("Game Over!")
#         print("No winner")
