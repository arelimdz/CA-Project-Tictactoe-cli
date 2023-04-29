from pprint import pprint

# Define board size
# TODO: Load from settings file
num_rows = 3
num_columns = 3

# Create board
board = []
for row_index in range(num_rows):
    board.append([None] * num_columns)

#  Get input from player
def get_valid_position():
    number = input("player input: ")
    if 1 <= int(number) <= (num_rows * num_columns):
        return int(number)



markers = ["X", "O"]
position = get_valid_position()


# Get board index
r = row_index = (position - 1) // num_columns
c = column_index = (position - 1) % num_columns

if board[r][c] is None:
    board[r][c] = markers
else:
    print("Sorry spot taken. TRY AGAIN!")

pprint (board)
