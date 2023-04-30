board = [["asnad", "X", None],[None,"X","X"], [None , None, None]]
move = (0,1) 

step = 1
num_rows = 3
num_columns = 3
board_limits_per_row = num_rows -1
mark = "X"


pointer1 = list(move)  # [0,1]--> None
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
    pointer1[1] = pointer1[1] -1
    print(update_board(pointer1))
    #Check if is limits
    if pointer1[1] < 0:
        pointer1[1] = None
    else: 
        if is_mark() is True:
            print(pointer1)

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

