from print_game_settings_screen import format_game_settings_screen


def test_print_settings_to_screen():
    # Arrange
    game_settings = {
        "num_rows": 3,
        "num_columns": 3,
        "win_target": 3,
        "player_name_1": "Player 1",
        "player_name_2": "Player 2",
    }

    expected_result = f"""====================== Game Settings ======================

[ 1 ] Update Board Size (3x3) and Line Length (3)
                        
[ 2 ] Update Player 1 Name (Player 1)
                        
[ 3 ] Update Player 2 Name (Player 2)

[ 4 ] Exit to Main Menu


==========================================================

"""

    # Act
    result = format_game_settings_screen(game_settings)

    # Assert
    assert expected_result == result
