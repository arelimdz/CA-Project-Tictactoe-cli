from is_valid_user_input import is_valid_user_input
from format_board import format_board, clear_terminal
from build_board import build_board
from has_board_space import has_space
from win_checker import has_player_won


def main_game_loop(num_rows, num_columns, target, player_1, player_2) -> str:
    clear_terminal()
    # Create board
    board = build_board(num_rows, num_columns)

    # Set values to choose player mark
    markers = ["X", "O"]
    players = [player_1, player_2]
    current_marker_index = 0

    #  Get input from player and verify if valid
    def get_valid_position(board):
        while True:
            position = input(
                f"\n{players[current_marker_index]}, enter a position ({1}-{num_rows * num_columns}) to place {markers[current_marker_index]}: "
            )
            if position.lower().strip() in ["flip table", "flip the table"]:
                return None

            valid_position, error = is_valid_user_input(board, position)
            if error:
                print(error)
            elif valid_position is not None:
                return valid_position

    # Call formated board
    board_string = format_board(board)

    # Set loop for game while there is not winner
    is_game_over = False
    while not is_game_over:
        formatted_board = format_board(board)
        print(formatted_board)
        position = get_valid_position(board)
        if position is None:
            print(
                f"\n(╯°□°)╯︵ ┻━┻ \n\n"
                f"{players[current_marker_index]} rage-quit and ruined the game for everyone!\n"
            )
            return None  # board was flipped, exit the application

        r, c = position

        # Get the mark of the current Player
        current_marker = markers[current_marker_index]
        current_player = players[current_marker_index]

        # Marked the move in the baord position
        board[r][c] = current_marker
        move = (r, c)

        # Check for a winner
        if has_player_won(board, move, current_marker, target):
            clear_terminal()
            print(format_board(board))
            print(
                f"\nCongratulations {players[current_marker_index]}!!! \n\nYou are the WINNER\n"
            )
            is_game_over = True
            break

        # Check if board has any empty space
        if not has_space(board):
            print("\nGAME OVER!!! Nobody wins!")
            break

        current_marker_index = (current_marker_index + 1) % len(markers)
        clear_terminal()
