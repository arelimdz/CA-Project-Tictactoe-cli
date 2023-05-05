from enum import Enum, auto
from print_game_settings_screen import format_game_settings_screen
from save_value_to_file import load_settings, save_settings
from format_board import clear_terminal
from views import main_menu_view, game_title
from game import main_game_loop
from game_setting import (
    set_rows,
    set_columns,
    set_target,
    update_name_player_1,
    update_name_player_2,
)


SETTINGS_FILE = "./data/game_settings.txt"


class Screens(Enum):
    MAIN_MENU = "MAIN_MENU"
    GAMEPLAY = "GAMEPLAY"
    SETTINGS = "SETTINGS"


class MainMenuScreenOptions(Enum):
    PLAY_GAME = "PLAY_GAME"
    VIEW_CREDITS = "VIEW_CREDITS"
    VIEW_SETTINGS = "VIEW_SETTINGS"
    EXIT_APP = "EXIT_APP"


class SettingsScreenOptions(Enum):
    UPDATE_BOARD_SIZE = "UPDATE_BOARD_SIZE"
    UPDATE_PLAYER_NAME_1 = "UPDATE_PLAYER_NAME_1"
    UPDATE_PLAYER_NAME_2 = "UPDATE_PLAYER_NAME_2"
    GO_TO_MAIN_MENU = "GO_TO_MAIN_MENU"


def handle_main_menu_options():
    print(main_menu_view())
    option = int(input("Enter numbered option:"))
    if option == 1:
        return Screens.GAMEPLAY

    if option == 2:
        return Screens.SETTINGS

    if option == 3:
        return None

    return Screens.MAIN_MENU


def handle_gameplay():
    # DO MAIN GAME LOOP
    
    main_game_loop(num_rows, num_columns, target, player_1, player_2)
    print("Wanna play again? ")

    repit_loop = input("Wanna play again? :")

    return Screens.MAIN_MENU


def handle_settings_options():
    clear_terminal()
    settings = load_settings(SETTINGS_FILE)
    print(format_game_settings_screen(settings))
    option = int(input("Enter numbered option: "))
    settings = load_settings(SETTINGS_FILE)

    if option == 1:
        rows = set_rows()
        columns = set_columns()
        target = set_target(rows, columns)
        settings["num_rows"] = rows
        settings["num_columns"] = columns
        settings["win_target"] = target
        save_settings(SETTINGS_FILE, settings)
        clear_terminal()
        return Screens.SETTINGS

    if option == 2:
        player_1_name = update_name_player_1()
        settings["player_name_1"] = player_1_name
        save_settings(SETTINGS_FILE, settings)
        clear_terminal()
        return Screens.SETTINGS

    if option == 3:
        player_2_name = update_name_player_2()
        settings["player_name_2"] = player_2_name
        save_settings(SETTINGS_FILE, settings)
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
    clear_terminal()
    current_screen = Screens.MAIN_MENU
    while current_screen:
        handle_screen = screen_handlers[current_screen]
        current_screen = handle_screen()


start_menu_system()
