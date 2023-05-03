from format_board import format_board


def test_format_empty_board_3x3():
    # Arrange
    expected_result = f"""
  1  |  2  |  3
.....+.....+.....
  4  |  5  |  6
.....+.....+.....
  7  |  8  |  9
"""
    board = [[None, None, None], [None, None, None], [None, None, None]]

    # Act
    result = format_board(board)

    # Assert

    assert expected_result == result


def test_format_empty_board_4x3():
    # Arrange
    expected_result = f"""
  01  |  02  |  03  |  04
......+......+......+......
  05  |  06  |  07  |  08
......+......+......+......
  09  |  10  |  11  |  12
"""
    board = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    # Act
    result = format_board(board)

    # Assert

    assert expected_result == result


def test_format_board_3x3_with_elements():
    # Arrange
    expected_result = f"""
  1  |  X  |  3
.....+.....+.....
  X  |  O  |  6
.....+.....+.....
  7  |  8  |  O
"""
    board = [[None, "X", None], ["X", "O", None], [None, None, "O"]]

    # Act
    result = format_board(board)

    # Assert

    assert expected_result == result


def test_format_board_4x3_with_elements():
    # Arrange
    expected_result = f"""
  X   |  02  |  03  |  04
......+......+......+......
  05  |  06  |  07  |  08
......+......+......+......
  09  |  10  |  11  |  12
"""
    board = [
        ["X", None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    # Act
    result = format_board(board)

    # Assert

    assert expected_result == result
