from enum import Enum, auto
from format_board import clear_terminal
from views import main_menu_view, game_title
from game import main_game_loop
from print_game_settings_screen import format_game_settings_screen
from settings_file_io import (
    load_settings,
    save_settings,
    SETTINGS_FILE_PATH,
)
from game_setting import (
    update_name_player_1,
    update_name_player_2,
    get_valid_integer,
    update_board,
)


class Screens(Enum):
    MAIN_MENU = "MAIN_MENU"
    GAMEPLAY = "GAMEPLAY"
    SETTINGS = "SETTINGS"


def handle_main_menu_options():
    print(main_menu_view())
    option = get_valid_integer("Enter numbered option", 1, 3)
    if option == 1:
        return Screens.GAMEPLAY

    if option == 2:
        return Screens.SETTINGS

    if option == 3:
        return None

    return Screens.MAIN_MENU


def handle_gameplay():
    file_settings = load_settings(SETTINGS_FILE_PATH)
    rows = int(file_settings["num_rows"])
    columns = int(file_settings["num_columns"])
    target = int(file_settings["win_target"])
    player_1 = file_settings["player_name_1"]
    player_2 = file_settings["player_name_2"]
    result = main_game_loop(rows, columns, target, player_1, player_2)
    if result == "TABLE_FLIPPED":
        return None

    while True:
        play_again = input("\nDo you want to Play Again? (Y/N): ").strip()
        if play_again and play_again.upper() == "Y":
            result = main_game_loop(rows, columns, target, player_1, player_2)
            if result == "TABLE_FLIPPED":
                return None

        elif play_again and play_again.upper() == "N":
            return Screens.MAIN_MENU

        print("Enter Y for Yes or N for No")

    return Screens.MAIN_MENU


def handle_settings_options():
    settings = load_settings(SETTINGS_FILE_PATH)
    print(format_game_settings_screen(settings))
    option = get_valid_integer("Enter numbered option", 1, 4)
    settings = load_settings(SETTINGS_FILE_PATH)

    if option == 1:
        new_settings = update_board()
        rows, columns, target = new_settings
        settings["num_rows"] = rows
        settings["num_columns"] = columns
        settings["win_target"] = target
        save_settings(SETTINGS_FILE_PATH, settings)
        clear_terminal()
        return Screens.SETTINGS

    if option == 2:
        player_1_name = update_name_player_1()
        settings["player_name_1"] = player_1_name
        save_settings(SETTINGS_FILE_PATH, settings)
        clear_terminal()
        return Screens.SETTINGS

    if option == 3:
        player_2_name = update_name_player_2()
        settings["player_name_2"] = player_2_name
        save_settings(SETTINGS_FILE_PATH, settings)
        clear_terminal()
        return Screens.SETTINGS

    if option == 4:
        clear_terminal()
        return Screens.MAIN_MENU

    return Screens.MAIN_MENU


screen_handlers = {
    Screens.MAIN_MENU: handle_main_menu_options,
    Screens.GAMEPLAY: handle_gameplay,
    Screens.SETTINGS: handle_settings_options,
}


def start_menu_system():
    print(game_title())
    input("")

    current_screen = Screens.MAIN_MENU
    while current_screen:
        clear_terminal()
        handle_screen = screen_handlers[current_screen]
        current_screen = handle_screen()
