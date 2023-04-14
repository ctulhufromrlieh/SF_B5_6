import random
import time

# consts
size_x = 3
size_y = 3
min_size = min(size_x, size_y)
win_count = min_size

is_show_coord_line = min_size < 10
turn_delimiter_line_len = 20

computer_delay = 1


# convert funcs
def convert_field_value_to_symbol(a_field_value):
    if a_field_value == 0:
        # return " "
        return "·"
    elif a_field_value == 1:
        return "X"
    elif a_field_value == 2:
        return "O"
    else:
        raise Exception("convert_field_value_to_symbol: wrong field_value")


def convert_player_index_to_name(a_player_index):
    if is_multiplayer:
        return f"Player {a_player_index + 1}"
    else:
        if a_player_index == human_player_index:
            return "Player"
        else:
            return "Computer"


def convert_end_index_to_name(a_end_index):
    if a_end_index == -1:
        return "Game is over! No one is win!"
    elif a_end_index in [1, 2]:
        a_player_index = a_end_index - 1
        winner_name = convert_player_index_to_name(a_player_index)
        if is_multiplayer:
            return f"Congratulations! {winner_name} won!"
        elif a_player_index == human_player_index:
            return f"Congratulations! You win!"
        else:
            return f"Game is over! {winner_name} won"
    else:
        raise Exception("convert_end_index_to_name: wrong a_end_index")


# show funcs
def show_field(a_field):
    print()
    print("Field state:")
    if is_show_coord_line:
        a_coord_names = map(str, range(1, size_x + 1))
        a_coord_line = 2 * " " + "".join(a_coord_names)
        print(a_coord_line)
        print('-' * (size_x + 2))

    # row_index = 0
    for a_row_index in range(len(a_field)):
        a_row_strs = list(map(convert_field_value_to_symbol, a_field[a_row_index]))
        a_row_line = "".join(a_row_strs)
        if is_show_coord_line:
            a_row_line = f"{a_row_index + 1}|{a_row_line}"
        print(a_row_line)

    print()


def show_turn_title(a_turn_index, a_player_index):
    print("=" * turn_delimiter_line_len)
    print(f"Round number #{a_turn_index + 1}.")
    print(f"{convert_player_index_to_name(a_player_index)} turn.")


def show_turn(a_coordinates):
    print(f"(X;Y) = ({a_coordinates[0] + 1}; {a_coordinates[1] + 1})")


# read funcs
def read_variant(a_msg_text, a_variants, a_def_index=None):
    def fix_index(a_index, a_default):
        if a_index is None:
            return a_default
        elif 0 <= a_index < len(a_variants):
            return a_index
        else:
            return a_default

    if a_def_index is None:
        a_def_index = len(a_variants) - 1

    print(a_msg_text)
    for a_var_index in range(len(a_variants)):
        print(f"{a_var_index + 1}: {a_variants[a_var_index]}")

    a_var_index = str_to_int(input("Your choice: "))
    if a_var_index is not None:
        a_var_index -= 1

    a_fixed_def_index = fix_index(a_def_index, len(a_variants) - 1)
    a_fixed_var_index = fix_index(a_var_index, a_fixed_def_index)

    print(f"You choose {a_variants[a_fixed_var_index]}")

    return a_fixed_var_index


def str_to_int(a_string_value):
    try:
        return int(a_string_value)
    except ValueError:
        return None


# return value - coordinates if all OK, None if user quit
def read_coordinates(a_data, a_player_index):
    # global avail_turn_count
    while True:
        coord_s = input(f"Enter coordinates, {convert_player_index_to_name(a_player_index)}: ")
        if coord_s.lower() in ['exit', 'quit']:
            return None

        coord_values = coord_s.split()
        if len(coord_values) < 2:
            print("Wrong coordinates - less then two numbers. Re-enter your coordinates!")
        else:
            a_ix = str_to_int(coord_values[0])
            a_iy = str_to_int(coord_values[1])
            if not a_ix or not a_iy:
                print("Wrong coordinates - not a number. Re-enter your coordinates!")
            else:
                a_ix -= 1
                a_iy -= 1
                if a_ix < 0 or a_ix >= size_x or a_iy < 0 or a_iy >= size_y:
                    print("Wrong coordinates - cell is out of field. Re-enter your coordinates!")
                elif a_data["field"][a_iy][a_ix]:
                    print("Wrong coordinates - cell is already used. Re-enter your coordinates!")
                else:
                    return a_ix, a_iy


# data funcs
def create_field(a_size_x, a_size_y):
    a_data = []
    for i in range(0, a_size_y):
        a_data.append([])
        for j in range(0, a_size_x):
            a_data[-1].append(0)

    return a_data


def matrix_has_count_value(a_data, a_value, a_req_count):
    a_field = a_data["field"]
    a_size_x = a_data["size_x"]
    a_size_y = a_data["size_y"]
    a_min_size = a_data["min_size"]

    # horizontal
    for a_row_index in range(a_size_y):
        a_count = 0
        for a_col_index in range(a_size_x):
            if a_field[a_row_index][a_col_index] == a_value:
                a_count += 1
                if a_count == a_req_count:
                    return True
            else:
                a_count = 0

    # vertical
    for a_col_index in range(a_size_x):
        a_count = 0
        for a_row_index in range(a_size_y):
            if a_field[a_row_index][a_col_index] == a_value:
                a_count += 1
                if a_count == a_req_count:
                    return True
            else:
                a_count = 0

    # diagonal 1
    for a_offset_y in range(a_size_y - a_min_size + 1):
        for a_offset_x in range(a_size_x - a_min_size + 1):
            a_count = 0
            for a_dg_index in range(a_min_size):
                if a_field[a_offset_y + a_dg_index][a_offset_x + a_dg_index] == a_value:
                    a_count += 1
                    if a_count == a_req_count:
                        return True
                else:
                    a_count = 0

    # diagonal 2
    for a_offset_y in range(a_size_y - a_min_size + 1):
        for a_offset_x in range(a_size_x - a_min_size + 1):
            a_count = 0
            for a_dg_index in range(a_min_size):
                if a_field[a_offset_y + a_dg_index][a_offset_x + a_min_size - 1 - a_dg_index] == a_value:
                    a_count += 1
                    if a_count == a_req_count:
                        return True
                else:
                    a_count = 0

    # no one line found
    return False


# return values:
#    0: game continue
#   -1: no one win
#    1: player with index 0 wins
#    2: player with index 1 wins
def get_end_index(a_data):
    for curr_player_index in range(0, 2):
        if matrix_has_count_value(a_data, 1 + curr_player_index, a_data["win_count"]):
            return 1 + curr_player_index

    # no available turns
    if not a_data["avail_turn_count"]:
        return -1

    # no end yet
    return 0


def get_coordinates_by_index(a_field, a_index):
    a_curr_index = 0
    for a_row_index in range(0, len(a_field)):
        for a_col_index in range(0, len(a_field[a_row_index])):
            if not a_field[a_row_index][a_col_index]:
                if a_curr_index == a_index:
                    return a_col_index, a_row_index
                else:
                    a_curr_index += 1

    raise Exception("get_coordinates_by_index: wrong a_data, a_index")


# ! a_player_index exists there for call compatibility
def computer_turn_random(a_data, a_player_index):
    a_index = random.randint(0, a_data["avail_turn_count"] - 1)
    time.sleep(computer_delay)
    return get_coordinates_by_index(a_data["field"], a_index)


if __name__ == "__main__":
    turn_index = 0
    player_index = 0
    avail_turn_count = size_x * size_y
    data = {"size_x": size_x,
            "size_y": size_y,
            "min_size": min_size,
            "win_count": win_count,
            "avail_turn_count":  size_x * size_y}
    data["field"] = create_field(data["size_x"], data["size_y"])

    # select computer strategy
    computer_turn = computer_turn_random

    human_player_index = 0    # default value for safety and compiler's happiness
    var_game_mode = read_variant("Choose game mode:", ["Single player game", "Multiplayer game"], 1)
    if var_game_mode == 0:
        is_multiplayer = False
        var_side = read_variant("Choose your side:", ["Xs", "Os"], 0)
        if var_side == 0:
            human_player_index = 0
        elif var_side == 1:
            human_player_index = 1
        else:
            raise Exception("main: wrong var_side")
    elif var_game_mode == 1:
        is_multiplayer = True
    else:
        raise Exception("main: wrong var_game_mode")

    if is_multiplayer:
        player_funcs = [read_coordinates, read_coordinates]
    else:
        player_funcs = [computer_turn, computer_turn]
        player_funcs[human_player_index] = read_coordinates

    show_field(data["field"])
    while True:
        show_turn_title(turn_index, player_index)

        coordinates = player_funcs[player_index](data, player_index)
        # if Player wants to Exit
        if coordinates is None:
            print("Exiting application...")
            exit(0)
        show_turn(coordinates)

        iy = coordinates[1]
        ix = coordinates[0]
        data["field"][iy][ix] = player_index + 1
        data["avail_turn_count"] -= 1

        show_field(data["field"])

        curr_end_index = get_end_index(data)
        if curr_end_index:
            print(convert_end_index_to_name(curr_end_index))
            break

        if player_index == 0:
            player_index = 1
        elif player_index == 1:
            player_index = 0
            turn_index += 1
        else:
            raise Exception("main: Wrong curr_player_index")
