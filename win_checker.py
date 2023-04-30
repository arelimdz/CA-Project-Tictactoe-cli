def is_marked(board, position, player_mark):
    return board[position[0]][position[1]] == player_mark


def is_invalid_left_pointer(
    left_pointer_row, left_pointer_column, left_row_limit, left_column_limit
):
    return left_pointer_row < left_row_limit or left_pointer_column < left_column_limit


def is_invalid_right_pointer(
    right_pointer_row, right_pointer_column, right_row_limit, right_column_limit
):
    return (
        right_pointer_row > right_row_limit or right_pointer_column > right_column_limit
    )


def is_winning_move(board, move, mark, target, pointer_1_offset, pointer_2_offset):
    pointer1 = list(move)
    pointer2 = list(move)

    turns = ["pointer1", "pointer2"]
    pointers = [
        (pointer1, is_invalid_left_pointer, pointer_1_offset, (0, 0)),
        (
            pointer2,
            is_invalid_right_pointer,
            pointer_2_offset,
            (len(board), len(board[0])),
        ),
    ]
    current_turn_index = 0
    counter = 1

    pointer = True
    while not ((pointer1 is None and pointer2 is None) or (counter == target)):
        (
            pointer,
            is_invalid_pointer,
            pointer_offset,
            limits,
        ) = pointers[current_turn_index]
        # Change the pointer position to 1 left
        if pointer is not None:
            pointer_row, pointer_column = pointer
            pointer_offset_row, pointer_offset_column = pointer_offset
            pointer_row += pointer_offset_row
            pointer_column += pointer_offset_column
            row_limit, column_limit = limits

            is_valid_pointer_result = not is_invalid_pointer(
                pointer_row, pointer_column, row_limit, column_limit
            )

            if is_valid_pointer_result and is_marked(
                board, (pointer_row, pointer_column), mark
            ):
                print(
                    pointer_row,
                    pointer_column,
                    board[pointer_row][pointer_column],
                    mark,
                )
                counter += 1
                print("counter", counter)
            else:
                is_valid_pointer_result = False

            is_invalid_pointer_result = not is_valid_pointer_result
            if is_invalid_pointer_result:
                print(pointer_row, pointer_column, "is now None")
                pointer = None
                current_turn_index = (current_turn_index + 1) % len(turns)
                pointer = pointers[current_turn_index][0]

    return counter == target


board = [["X", "O", "X"], [None, "X", "X"], [None, "X", None]]
# board = [["X", None, "O", "X"], [None, None, "X", "X"], [None, None, None, None]]
move = (1, 1)


num_rows = len(board)
num_columns = len(board[0])

# result = is_winning_move(board, move, "X", 3, (0, -1), (0, 1))  # horizontal
result = is_winning_move(board, move, "X", 3, (-1, 0), (1, 0))  # vertical

print(result)
