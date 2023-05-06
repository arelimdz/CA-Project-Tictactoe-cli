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


def test_format_empty_board_10x10():
    # Arrange
    expected_result = f"""
  001  |  002  |  003  |  004  |  005  |  006  |  007  |  008  |  009  |  010
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  011  |  012  |  013  |  014  |  015  |  016  |  017  |  018  |  019  |  020
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  021  |  022  |  023  |  024  |  025  |  026  |  027  |  028  |  029  |  030
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  031  |  032  |  033  |  034  |  035  |  036  |  037  |  038  |  039  |  040
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  041  |  042  |  043  |  044  |  045  |  046  |  047  |  048  |  049  |  050
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  051  |  052  |  053  |  054  |  055  |  056  |  057  |  058  |  059  |  060
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  061  |  062  |  063  |  064  |  065  |  066  |  067  |  068  |  069  |  070
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  071  |  072  |  073  |  074  |  075  |  076  |  077  |  078  |  079  |  080
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  081  |  082  |  083  |  084  |  085  |  086  |  087  |  088  |  089  |  090
.......+.......+.......+.......+.......+.......+.......+.......+.......+.......
  091  |  092  |  093  |  094  |  095  |  096  |  097  |  098  |  099  |  100
"""
    board = [
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
    ]

    # Act
    result = format_board(board)

    # Assert

    assert expected_result == result
