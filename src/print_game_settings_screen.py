game_settings = {
    "num_rows": 3,
    "num_columns": 3,
    "win_target": 3,
    "player_name_1": "Player 1",
    "player_name_2": "Player 2",
}


def format_game_settings_screen(game_settings):
    num_rows = game_settings["num_rows"]
    num_columns = game_settings["num_columns"]
    winning_line_length = game_settings["win_target"]
    player_1_name = game_settings["player_name_1"]
    player_2_name = game_settings["player_name_2"]
    result = f"""


=== Game Settings ===

1. Update Board Size (currently {num_rows}x{num_columns}) and Line Length (currently {winning_line_length})

2. Update Player 1 Name (currently '{player_1_name}')

3. Update Player 2 Name (currently '{player_2_name}')

4. Exit to Main Menu

"""
    return result.lstrip()
