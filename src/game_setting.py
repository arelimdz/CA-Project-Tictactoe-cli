def get_valid_integer(max_number):
    while True:
        try:
            num = int(input(f"Please enter a number between 2 and {max_number}: "))
            if num < 2 or num > max_number:
                raise ValueError("Number is not in range!")
            return num
        except ValueError:
            print(
                f"That is an invalid input! \nPlease enter a whole number between 2 and {max_number}: "
            )


def set_rows():
    print("Let's set size of the ROW")
    num_rows = get_valid_integer(9)
    return num_rows


def set_columns():
    print("Let's set size of the COLUMNS")
    num_columns = get_valid_integer(9)
    return num_columns


def set_target(num_columns, num_rows):
    print("Choose a WINNING LINE LENGTH size")
    target = get_valid_integer(max(num_columns, num_rows))
    return target


def get_name(personalize_text, sub_name):
    name = input(f"{personalize_text} introduce your alias: ").upper()
    if name == "":
        name = sub_name
    return name


def update_name_player_1():
    update_name = get_name("First Player", "Player 1")
    return update_name


def update_name_player_2():
    update_name = get_name("Second Player", "Player 2")
    return update_name
