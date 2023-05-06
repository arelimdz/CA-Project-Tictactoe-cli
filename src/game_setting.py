def get_valid_integer(custom_text, min_number, max_number) -> int:
    while True:
        try:
            num = int(input(f"{custom_text} ({min_number}-{max_number}): "))
            if num < min_number or num > max_number:
                raise ValueError("\nNumber is not in range!")
            return num
        except ValueError:
            print(f"\nThat is an invalid input!")


text_for_input = "Please enter a number"


def update_board() -> set:
    print("\nLet's set size of the ROW")
    num_rows = get_valid_integer(text_for_input, 2, 20)

    print("\nLet's set size of the COLUMNS")
    num_columns = get_valid_integer(text_for_input, 2, 20)

    print("\nChoose a WINNING LINE LENGTH size")
    max_number = max(num_columns, num_rows)
    target = get_valid_integer(
        f"Please enter a number",
        2,
        max_number,
    )
    return (num_rows, num_columns, target)


def get_name(custom_text, sub_name) -> str:
    name = input(f"\n{custom_text} introduce your alias: ").upper()
    if name == "":
        name = sub_name
    return name


def update_name_player_1() -> str:
    update_name = get_name("\nFirst Player", "Player 1")
    return update_name


def update_name_player_2() -> str:
    update_name = get_name("\nSecond Player", "Player 2")
    return update_name
