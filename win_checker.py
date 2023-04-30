def is_marked(board, position, player_mark):
    return board[position[0]][position[1]] == player_mark


def is_valid_pointer(
    pointer_row,
    pointer_column,
    row_limit,
    column_limit,
):
    return (
        pointer_row >= 0
        and pointer_row <= row_limit
        and pointer_column >= 0
        and pointer_column <= column_limit
    )


def is_winning_move(board, move, mark, target, pointer_1_offset, pointer_2_offset):
    turns = ["pointer1", "pointer2"]
    row_limit = len(board) - 1
    column_limit = len(board[0]) - 1
    pointer_configs = [
        [list(move), pointer_1_offset],
        [list(move), pointer_2_offset],
    ]
    current_turn_index = 0
    counter = 1

    pointer = True
    while not (
        all(pointer_config[0] is None for pointer_config in pointer_configs)
        or (counter == target)
    ):
        (
            pointer,
            pointer_offset,
        ) = pointer_configs[current_turn_index]

        if pointer is not None:
            pointer_row, pointer_column = pointer
            pointer_offset_row, pointer_offset_column = pointer_offset
            pointer_row += pointer_offset_row
            pointer_column += pointer_offset_column

            is_valid_pointer_result = is_valid_pointer(
                pointer_row, pointer_column, row_limit, column_limit
            )

            if is_valid_pointer_result and is_marked(
                board, (pointer_row, pointer_column), mark
            ):
                counter += 1
                if counter == target:
                    return True

                pointer_configs[current_turn_index][0] = (pointer_row, pointer_column)
                continue

            pointer_configs[current_turn_index][0] = None
            current_turn_index = (current_turn_index + 1) % len(turns)
            pointer = pointer_configs[current_turn_index][0]

    return counter == target


# board = [["X", None, "O"], [None, "X", None], [None, None, None]]
# # board = [["X", None, "O", "X"], [None, None, "X", "X"], [None, None, None, None]]
# # move = (1, 1)


# num_rows = len(board)
# num_columns = len(board[0])

# # result = is_winning_move(board, (2, 3), "O", 3, (-1, 0), (1, 0))  # horizontal
# # result = is_winning_move(board, (1, 1), "X", 2, (-1, 0), (1, 0))  # vertical
# result = is_winning_move(board, (2, 0), "X", 3, (1, -1), (-1, 1))  # / diagonal
# # result = is_winning_move(board, (2, 2), "X", 3, (-1, -1), (1, 1))  # \ diagonal

# print(result)
