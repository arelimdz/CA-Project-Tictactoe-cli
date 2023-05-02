# Board builder
def build_board(num_rows, num_columns):
    board = []
    for row_index in range(num_rows):
        board.append([None] * num_columns)

    return board
