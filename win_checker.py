board = [["asnad", "X", None],[None,"X","X"], [None , None, None]]
move = (0,1) 

step = 1
num_rows = 3
num_columns = 3
board_limits_per_row = num_rows -1
mark = "X"

pointer1 = [0, None]
# pointer1 = list(move)  # [0,1]--> None
pointer2 = list(move)   # [0,1]--> [0,2] ---> None
def update_board(pointer1):
    position = board[pointer1[0]][pointer1[1]]
    return (position)

turn = "pointer1"
counter = 1
target = 3
has_win = False

# Check if is mark
def is_mark():
    if update_board(pointer1) == mark:
        return True


if turn == "pointer1":
    # Check if pointer 1 is mark None, stop the loop
    if pointer1[1] == None:
        print("Aqui termina")
    # Change the pointer position to 1 left
    else: 
        pointer1[1] = pointer1[1] -1

        #Check if pointer is inside of board limits
        if pointer1[1] < 0:
            pointer1[1] = None

        else: 
            # Check is position is mark with "X"
            if is_mark() is True:
                # Confirm the new position for pointer1
                pointer1

            else: 
                # If position is mark diferente or empty mark with None
                pointer1[1] = None


print (pointer1)




# while not ((pointer1 is None and pointer2 is None) or (counter == target)):
#     if turn == "pointer1":
#         pointer1[1] = pointer1[1] -1
#         if pointer1[1] < 0:
#             pointer1[1] = None
#         else: 
#             pointer1
#     elif turn == "pointer2"
#         pointer2[1] = pointer2 [1] + 1
#         if pointer2[1] > board_limits_per_row[1]:
#             pointer2[1] = None
#         else: 
#             pointer2

