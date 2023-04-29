# Define board size
# TODO: Load from settings file
num_rows = 3
num_columns = 3

# Create board
board = []
for row_index in range(num_rows):
    board.append([None] * num_columns)

#  Get input from player
number = input("player input: ")
if 1 <= int(number) <= (num_rows * num_columns):
    return int(number)

