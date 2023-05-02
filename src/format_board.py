def format_board(board) -> str:
    board_position = 0
    rows_to_print = []
    result = ""
    num_columns = len(board[0])
    len_of_max_position = len(str(num_columns * len(board)))
    print(len_of_max_position)
    for row_index, row in enumerate(board):
        row_to_print = []
        for column_index, column in enumerate(row):
            board_position += 1
            value = board[row_index][column_index]
            if value is None:
                row_to_print.append(str(board_position).zfill(len_of_max_position))
            else:
                row_to_print.append(value.center(len_of_max_position, " "))
        rows_to_print.append("  " + "  |  ".join(row_to_print) + "\n")
    result += "\n"
    space = (("+" + ("." * (len_of_max_position + 4))) * num_columns)[1:]
    result += f"{space}\n".join(rows_to_print)
    return result
