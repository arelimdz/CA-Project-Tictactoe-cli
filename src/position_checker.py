# Check if a position is mark by the player in turn ("X" or "O")
def is_marked(board, position, player_mark):
    return board[position[0]][position[1]] == player_mark


# Check if the pointers are in the limits of the board
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


#  Check if the player's move is the winner by checking positions around it
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
    pointer_position = list(move)

    # Set loop for pointer_1 pointer to move backwards and pointer_2 pointer to move forward
    # until pointers value becomes None or counter hit target
    while not (
        all(pointer_config[0] is None for pointer_config in pointer_configs)
        or (counter == target)
    ):
        (
            pointer_position,
            pointer_offset,
        ) = pointer_configs[current_turn_index]

        #  Check if the pointer in turn has a None value otherwise move to the next position
        if pointer_position is not None:
            pointer_row, pointer_column = pointer_position
            pointer_offset_row, pointer_offset_column = pointer_offset
            pointer_row += pointer_offset_row
            pointer_column += pointer_offset_column

            is_valid_pointer_result = is_valid_pointer(
                pointer_row, pointer_column, row_limit, column_limit
            )
            # Check if the position is marked with the mark of the player in turn
            if is_valid_pointer_result and is_marked(
                board, (pointer_row, pointer_column), mark
            ):
                counter += 1
                if counter == target:
                    return True

                # Switch pointers turn
                pointer_configs[current_turn_index][0] = (pointer_row, pointer_column)
                continue

            pointer_configs[current_turn_index][0] = None
            current_turn_index = (current_turn_index + 1) % len(turns)
            pointer_position = pointer_configs[current_turn_index][0]

    return counter == target
