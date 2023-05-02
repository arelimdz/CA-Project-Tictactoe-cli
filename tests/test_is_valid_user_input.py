from pprint import pprint

from is_valid_user_input import is_valid_user_input
from build_board import build_board


def test_when_user_input_is_not_a_number():
    # Arrange
    board = build_board(3, 3)
    user_input = "asdfa"

    # Act
    position, error = is_valid_user_input(board, user_input)

    # Assert
    assert position is None
    assert error == "Not a number"


def test_when_user_input_is_number_not_in_range():
    # Arrange
    board = build_board(3, 3)
    user_input = "10"

    # Act
    position, error = is_valid_user_input(board, user_input)

    # Assert
    assert position is None
    assert error == "Number not in range 1 to 9"


def test_when_user_input_refers_to_an_occupied_position():
    # Arrange
    board = build_board(3, 3)
    board[1][1] = "X"
    user_input = "5"

    # Act
    position, error = is_valid_user_input(board, user_input)

    # Assert
    assert position is None
    assert error == "Position occupied"
