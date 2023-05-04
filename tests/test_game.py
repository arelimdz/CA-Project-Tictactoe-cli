from unittest import mock
from game import main_game_loop


def test_state_of_game():
    expected_output = """
  1  |  2  |  3
.....+.....+.....
  4  |  5  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  2  |  3
.....+.....+.....
  4  |  5  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  3
.....+.....+.....
  4  |  5  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  X
.....+.....+.....
  4  |  5  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  X
.....+.....+.....
  O  |  5  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  X
.....+.....+.....
  O  |  X  |  6
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  X
.....+.....+.....
  O  |  X  |  O
.....+.....+.....
  7  |  8  |  9


  X  |  O  |  X
.....+.....+.....
  O  |  X  |  O
.....+.....+.....
  X  |  8  |  9

Congratulations Player 1!!!

You are the WINNER

"""

    inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    with mock.patch("builtins.input", side_effect=inputs) as mocked_input:
        with mock.patch("builtins.print") as mocked_print:
            result = main_game_loop(3, 3, 3)

        all_print_output = []
        for call_args in mocked_print.call_args_list:
            args, _ = call_args
            all_print_output.append(" ".join(list(map(str, args))))
        output = "\n".join(all_print_output)

    assert expected_output == output
