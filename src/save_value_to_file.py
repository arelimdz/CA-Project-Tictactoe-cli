import os
from game_setting import get_valid_integer, set_board, get_players

SETTINGS_FILE_PATH = "./data/game_settings.txt"
DEFAULT_SETTING_LINES = [
    "3",  # number of rows
    "3",  # number of columns
    "3",  # target win in a line
    "Player 1",  # player 1 name
    "Player 2",  # player 2 name
]


def load_settings(settings_file):
    lines = read_file(settings_file)
    return {
        "num_rows": int(lines[0]),
        "num_columns": int(lines[1]),
        "win_target": int(lines[2]),
        "player_name_1": lines[3],
        "player_name_2": lines[4],
    }


def save_settings(file_path, settings):
    lines = [
        settings["num_rows"],
        settings["num_columns"],
        settings["win_target"],
        settings["player_name_1"],
        settings["player_name_2"],
    ]
    write_file(file_path, lines)


def read_file(file_path):
    settings_file_exists = os.path.exists(file_path) and os.path.isfile(file_path)
    if settings_file_exists:
        with open(file_path, "r") as file_pointer:
            lines = [line.rstrip("\n") for line in file_pointer]
            try:
                str(int(lines[0])) == lines[0]
                str(int(lines[1])) == lines[1]
                str(int(lines[2])) == lines[2]
            except:
                return DEFAULT_SETTING_LINES

            return lines
    else:
        return DEFAULT_SETTING_LINES


def write_file(file_path, lines):
    with open(file_path, "w") as file_pointer:
        mapped_lines = [f"{line}\n" for line in lines]
        file_pointer.writelines(mapped_lines)


game_settings = load_settings(SETTINGS_FILE_PATH)
print(game_settings)

game_settings["player_name_1"] = "Areli"
print(game_settings)


save_settings(SETTINGS_FILE_PATH, game_settings)


# def default():
#     lines = read_file("../data/default_value.txt")
#     numbers = list(map(int, lines[0:3]))
#     row, column, target = numbers
#     player_1, player_2 = lines[3:5]
#     return row, column, target, player_1, player_2, new_setting_1, new_setting_2, new_setting_3


# def save_players():
#     file_path = "../data/settings_value.txt"
#     with open(file_path, "w") as file:
#         board = set_board()
#         players = get_players()
#         result = list((board + players))
#         for item in result:
#             file.write(item + "\n")
#         file.close()


board = set_board()
players = get_players()
print(result)


def save_game():
    pass


# @click.group()
# def cli():
#     pass


# @cli.command()
# def game_cover():
#     game_cover = print(
#         """
#     ***************************************************************************
#      __________  _           _                     _
#     |___    ___|(_)   ___  _| |_    ____    ___  _| |_    __     ____
#         |  |     _  / ___||_   _| / __  | / ___||_   _| / __ \  / __  \
#         |  |    | || |      | |  | |  | || |      | |  | |  | || |__| |
#         |  |    | || |      | |  | |  | || |      | |  | |  | || |____|
#         |  |    | || |___   | |  | |__| || |___   | |  | |__| || |____
#         |__|    |_| \____|  |_|   \___|_| \____|  |_|   \____/  \_____|

#     ***************************************************************************
#         """
#     )
#     return game_cover


# def start_game():
#     click.echo("Game Starting...")
#     board_set = set_board(get_valid_integer)
#     rows, columns, target = board_set
#     main_game_loop(rows, columns, target)


# if __name__ == "__main__":
#     cli()


# from enum import Enum

# # Enum


# class ScreenChoice(Enum):
#     MAIN_MENU = "MAIN_MENU"
#     GAMEPLAY = "GAMEPLAY"
#     SETTINGS = "SETTINGS"
#     CREDIT = "CREDIT"


# current_screen = ScreenChoice.MAIN_MENU

# main_menu_options = {
#     "1": ScreenChoice.GAMEPLAY,
#     "2": ScreenChoice.SETTINGS,
#     "3": ScreenChoice.CREDIT,
# }


# def main_menu():


#     choice = click.prompt("Please enter your choice", type=int)


#     if choice == 1:
#         click.echo("Game Starting...")
#         # your code for starting game
#     elif choice == 2:
#         click.echo("Opening Settings...")
#         # your code for opening Settings
#     elif choice == 3:
#         click.echo("Leaderboard Loading...")
#         # your code for showing Leaderboard
#     elif choice == 0:
#         click.echo("Exiting Menu...")
#         # break
#     else:
#         click.echo("Invalid option, try again...")


#  Game cover - Print with colorama
#  print menu
#  menu = [
# [1] Start Game --> have a default game set up
# [2] Settings ---> Go to game_setting
# [3] Leaderboard ---> See Leaderboard
# [0] Exit -----> Quit Application
# ]


# def game_cover():
#     game_cover = print(
#         """
#     ***************************************************************************
#      __________  _           _                     _
#     |___    ___|(_)   ___  _| |_    ____    ___  _| |_    __     ____
#         |  |     _  / ___||_   _| / __  | / ___||_   _| / __ \  / __  \
#         |  |    | || |      | |  | |  | || |      | |  | |  | || |__| |
#         |  |    | || |      | |  | |  | || |      | |  | |  | || |____|
#         |  |    | || |___   | |  | |__| || |___   | |  | |__| || |____
#         |__|    |_| \____|  |_|   \___|_| \____|  |_|   \____/  \_____|

#     ***************************************************************************
#         """
#     )
#     return game_cover
