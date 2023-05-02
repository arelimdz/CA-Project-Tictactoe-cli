from pprint import pprint
from build_board import build_board

# expected_post_updated_board_state = ...
# pre_updated_board_state = ...
# post_updated_board_state = update_board(board, move)
# assert expected_post_updated_board_state == post_updated_board_state



def test_format_board():
    pass


# Arrange
board = build_board(3, 3)
user_input = "5"
pre_updated_board_state = board

# Act
position, error = is_valid_user_input(board, user_input)
# post_updated_board_state = update_board(board, move)

# Assert
assert position is None
assert error == "Not a number"
# assert expected_post_updated_board_state == post_updated_board_state