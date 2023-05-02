def is_valid_user_input(board, user_input):
    num_rows, num_columns = len(board), len(board[0])
    board_size = num_rows * num_columns

    try:
        position = int(user_input)
        if 1 <= int(user_input) <= (num_rows * num_columns):
            r = row_index = (position - 1) // num_columns
            c = column_index = (position - 1) % num_columns

            if board[r][c] is not None:
                return None, "Position occupied"

            return (r, c), None
        else:
            return None, f"Number not in range 1 to {board_size}"

    except ValueError:
        if user_input.isalpha():
            return None, f"Not a number"