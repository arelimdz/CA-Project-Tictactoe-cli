from position_checker import is_winning_move


# Set values for offset (rigth and left) in check winner
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


# Check for a winner
def has_player_won(board, move, current_marker, target):
    for offsets in all_offsets:
        left_offset, right_offset = offsets
        # print(left_offset, right_offset)
        if is_winning_move(
            board,
            move,
            current_marker,
            target,
            left_offset,
            right_offset,
        ):
            return True
    return False
