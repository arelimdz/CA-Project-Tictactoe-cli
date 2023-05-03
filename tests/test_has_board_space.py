from has_board_space import has_space


def test_when_board_had_not_space_left():
    # Arrange
    expected_result = False
    board = [["O", "X", "X"], ["X", "X", "O"], ["O", "O", "X"]]

    # Act
    result = has_space(board)

    # Assert
    assert expected_result == result


def test_when_board_had_space():
    # Arrange
    expected_result = True
    board = [["X", None, "X"], ["O", None, None], [None, "O", None]]

    # Act
    result = has_space(board)

    # Assert
    assert expected_result == result
