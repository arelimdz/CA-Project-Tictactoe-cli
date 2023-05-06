import json
import os


SETTINGS_FILE_PATH = "./data/game_settings.txt"
DEFAULT_SETTINGS = {
    "num_rows": 3,
    "num_columns": 3,
    "win_target": 3,
    "player_name_1": "Rick",
    "player_name_2": "Morty",
}


def load_settings(file_path):
    settings_file_exists = os.path.exists(file_path) and os.path.isfile(file_path)
    if settings_file_exists:
        try:
            with open(file_path, "r") as file_pointer:
                settings = json.load(file_pointer)
                if (
                    int(settings["num_rows"]) == settings["num_rows"]
                    and int(settings["num_columns"]) == settings["num_columns"]
                    and int(settings["win_target"]) == settings["win_target"]
                    and str(settings["player_name_1"]) == str(settings["player_name_1"])
                    and str(settings["player_name_2"]) == str(settings["player_name_2"])
                ):
                    num_rows = settings["num_rows"]
                    num_columns = settings["num_columns"]

                    if not (
                        2 <= num_rows <= 20
                        and 2 <= num_columns <= 20
                        and settings["win_target"] <= max(num_rows, num_columns)
                    ):
                        raise Exception("Invalid board configuration")

                    return settings
        except Exception:
            pass

    return DEFAULT_SETTINGS


def save_settings(file_path, settings):
    try:
        with open(file_path, "w") as file_pointer:
            json.dump(settings, file_pointer)
    except Exception:
        print(traceback.format_exc())
