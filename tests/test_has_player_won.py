from win_checker import has_player_won


def test_when_player_wins_horizontal_top():
    # Arrange
    expected_result = True
    board = [["X", None, "X"], ["O", "O", None], [None, None, None]]
    move = (0, 1)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_horizontal_middle():
    # Arrange
    expected_result = True
    board = [[None, "X", None], [None, "O", "O"], ["X", "O", "X"]]
    move = (1, 0)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_horizontal_bottom():
    # Arrange
    expected_result = True
    board = [[None, None, None], ["X", "X", None], ["O", "O", None]]
    move = (2, 2)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_vertical_left():
    # Arrange
    expected_result = True
    board = [["X", None, None, "O"], ["X", "X", None, "O"], [None, "O", None, None]]
    move = (2, 0)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_vertical_right():
    # Arrange
    expected_result = True
    board = [[None, "X", "O"], ["X", None, "O"], [None, "O", None]]
    move = (2, 2)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_forward_diagonal():
    # Arrange
    expected_result = True
    board = [["O", None, None], ["X", "O", None], ["X", None, None]]
    move = (2, 2)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_backward_diagonal():
    # Arrange
    expected_result = True
    board = [["O", "O", "X"], [None, None, None], ["X", None, "O"]]
    move = (1, 1)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_do_not_win_horizontal():
    # Arrange
    expected_result = False
    board = [["X", None, "X"], ["O", "O", None], [None, None, None]]
    move = (2, 2)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_do_not_win_vertical():
    # Arrange
    expected_result = False
    board = [["X", None, "O"], ["X", None, "O"], [None, "O", None]]
    move = (2, 2)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_do_not_win_vertical_right():
    # Arrange
    expected_result = False
    board = [["X", "X", "O"], ["X", None, "O"], [None, "O", None]]
    move = (2, 0)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_wins_forward_diagonal():
    # Arrange
    expected_result = False
    board = [["O", None, None], ["X", "O", None], ["X", None, None]]
    move = (2, 1)
    current_marker = "O"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result


def test_when_player_do_not_win_backward_diagonal():
    # Arrange
    expected_result = False
    board = [["O", "O", "X"], [None, None, None], ["X", None, "O"]]
    move = (1, 2)
    current_marker = "X"
    target = 3

    # Act
    result = has_player_won(board, move, current_marker, target)

    # Assert
    assert expected_result == result
