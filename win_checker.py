# board = [["X", "X", "X"],[None,"X","X"], [None , None, None]]
board = [["X", None, "O", "X"],[None, None,"X","X"], [None , None, None, None]]
move = (0,1) 

step = 1
num_rows = len(board)
num_columns = len(board[0])


def is_marked(position, player_mark):
    return board[position[0]][position[1]] == player_mark


def is_winning_move(board, move, mark, target):
    pointer1 = list(move)
    pointer2 = list(move)

    turn = ["pointer1", "pointer2"]
    current_turn_index = 0
    counter = 1

    while not ((pointer1[1] is None and pointer2[1] is None) or (counter == target)):

        if turn[current_turn_index] == "pointer1":
            # Change the pointer position to 1 left
            if pointer1[1] is not None: 
                pointer1[1] = pointer1[1] - 1

                #Check if pointer is inside of board limits
                if pointer1[1] < 0:
                    pointer1[1] = None

                else: 
                    # Check is position is mark with "X"
                    if is_marked(pointer1, mark):
                        # Confirm the new position for pointer1
                        counter += 1

                    else: 
                        # If position is mark diferente or empty mark with None
                        pointer1[1] = None
        

        elif turn[current_turn_index] == "pointer2":

            # Change the pointer position to 1 rigth
            if pointer2[1] is not None:
                pointer2[1] = pointer2[1] + 1

                #Check if pointer is inside of board limits
                if pointer2[1] > num_columns - 1:
                    pointer2[1] = None

                else: 
                    # Check is position is mark with "X"
                    if is_marked(pointer2, mark):
                        # Confirm the new position for pointer2
                        counter += 1

                    else: 
                        # If position is mark diferente or empty mark with None
                        pointer2[1] = None
        


        current_turn_index = (current_turn_index + 1) % len(turn)

    return counter == target

result = is_winning_move(board, move, "O", 3)

print(result)
