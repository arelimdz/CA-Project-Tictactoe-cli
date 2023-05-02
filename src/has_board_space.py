def has_space(board) -> bool:
    for row in board:
        for value in row:
            if value is None:
                return True
    return False

