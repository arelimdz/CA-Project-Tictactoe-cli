from enum import Enum, auto


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
    UPDATE_WIN_LINE_LENGTH = "UPDATE_WIN_LINE_LENGTH"
    UPDATE_PLAYER_NAME_1 = "UPDATE_PLAYER_NAME_1"
    UPDATE_PLAYER_NAME_2 = "UPDATE_PLAYER_NAME_2"
    GO_TO_MAIN_MENU = "GO_TO_MAIN_MENU"


# screens = {
#     ScreenChoice.MAIN_MENU: {},
#     ScreenChoice.GAMEPLAY: {},
#     ScreenChoice.SETTINGS: {},
#     ScreenChoice.CREDIT: {},
# }

# main_menu_options = {
#     "1": ScreenChoice.GAMEPLAY,
#     "2": ScreenChoice.SETTINGS,
#     "3": ScreenChoice.CREDIT,
# }


# def start_menu_system():
#     current_screen = ScreenChoice.MAIN_MENU

# Used an ascii art generator: https://patorjk.com/software/taag
GAME_TITLE = """
████████╗██╗ ██████╗              ████████╗ █████╗  ██████╗
╚══██╔══╝██║██╔════╝              ╚══██╔══╝██╔══██╗██╔════╝
   ██║   ██║██║         █████╗       ██║   ███████║██║     
   ██║   ██║██║         ╚════╝       ██║   ██╔══██║██║     
   ██║   ██║╚██████╗                 ██║   ██║  ██║╚██████╗
   ╚═╝   ╚═╝ ╚═════╝                 ╚═╝   ╚═╝  ╚═╝ ╚═════╝
                                                           
                  ████████╗ ██████╗                        
                  ╚══██╔══╝██╔═══██╗                       
        █████╗       ██║   ██║   ██║    █████╗             
        ╚════╝       ██║   ██║   ██║    ╚════╝             
                     ██║   ╚██████╔╝                       
                     ╚═╝    ╚═════╝                        
                                                           
    ██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗██╗   ██╗
    ██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝
    ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║    ╚████╔╝ 
    ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║     ╚██╔╝  
    ██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║      ██║   
    ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝   
                                                                       
                  By Areli Mendoza Perez                         

                < Press ENTER to continue >
"""

print(GAME_TITLE)
