import os


def clear_terminal():
    input("Press enter to continue")
    os.system("cls" if os.name == "nt" else "clear")


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


def set_board(get_valid_integer):
    print("Let's start building your board!!!\n \nFirst let's set size of the ROW \n")
    num_rows = get_valid_integer(9)
    print("\nNow let's set size of the COLUMNS")
    num_columns = get_valid_integer(9)
    print(f"\nChoose a WINNING LINE LENGTH size")
    target_size = get_valid_integer(max(num_columns, num_rows))
    clear_terminal()
    return (num_rows, num_columns, target_size)


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


def get_name(sub_name):
    name = input("Introduce your alias: ").upper()
    if name == "":
        name = sub_name
    return name


# Set Player 1
def set_players(Player):
    player_1 = Player(get_name("Player 1"), "X")

    player_2 = Player(get_name("Player 2"), "O")

    return (player_1.name, player_1.mark), (player_2.name, player_2.mark)


print(set_players(Player))
