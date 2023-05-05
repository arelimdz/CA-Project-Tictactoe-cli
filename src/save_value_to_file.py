import os

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
                str((lines[3])) == lines[3]
                str((lines[4])) == lines[4]

            except:
                return DEFAULT_SETTING_LINES

            return lines
    else:
        return DEFAULT_SETTING_LINES


def write_file(file_path, lines):
    with open(file_path, "w") as file_pointer:
        mapped_lines = [f"{line}\n" for line in lines]
        file_pointer.writelines(mapped_lines)





