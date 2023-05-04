def get_valid_integer(max_number):
    while True:
        try:
            num = int(input(f"Please enter a number between 2 and {max_number}: "))
            if num < 2 or num > 9:
                raise ValueError("Number is not in range!")
            return num
        except ValueError:
            print(
                "That is an invalid input!  \nPlease enter a whole number between 2 and 9: "
            )


def set_board():
    print("Let's start building your board!!!\n \nFirst let's set size of the ROW \n")
    num_rows = get_valid_integer(9)
    print("\nNow let's set size of the COLUMNS \n")
    num_columns = get_valid_integer(9)
    print(f"\nChoose a WINNING LINE LENGTH size \n")
    target_size = get_valid_integer(max(num_columns, num_rows))

    return num_rows, num_columns, target_size


def get_players():
    def get_name(personalize_text, sub_name):
        name = input(f"{personalize_text} introduce your alias: ").upper()
        if name == "":
            name = sub_name
        return name

    get_player_1 = get_name("First Player", "Player 1")
    get_player_2 = get_name("Second Player", "Player 2")

    return get_player_1, get_player_2
