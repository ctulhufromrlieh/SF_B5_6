import random
import time

# consts
size_x = 3
size_y = 3
min_size = min(size_x, size_y)
win_count = min_size

is_show_coord_line = min_size < 10
turn_delimiter_line_len = 20

# is_multiplayer = True
human_player_index = 1
computer_delay = 1


# convert funcs
def convert_field_value_to_symbol(field_value):
    if field_value == 0:
        # return " "
        return "·"
    elif field_value == 1:
        return "X"
    elif field_value == 2:
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
def show_field(a_data):
    print()
    print("Field state:")
    if is_show_coord_line:
        coord_names = map(str, range(1, size_x + 1))
        coord_line = 2 * " " + "".join(coord_names)
        print(coord_line)
        print('-' * (size_x + 2))

    row_index = 0
    for row in a_data:
        row_strs = list(map(convert_field_value_to_symbol, row))
        row_line = "".join(row_strs)
        if is_show_coord_line:
            row_line = f"{row_index + 1}|{row_line}"
        print(row_line)
        row_index += 1

    print()


def show_turn_title(a_turn_index, a_player_index):
    # print()
    print("=" * turn_delimiter_line_len)
    print(f"Round number #{a_turn_index + 1}.")
    print(f"{convert_player_index_to_name(a_player_index)} turn.")
    # print("=" * turn_delimiter_line_len)


def show_turn(a_coordinates):
    # print(f"X = {a_coordinates[0] + 1} | Y = {a_coordinates[1] + 1}")
    print(f"(X;Y) = ({a_coordinates[0] + 1}; {a_coordinates[1] + 1})")


# read funcs
def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None


# return value - coordinates if all OK, None if user quit
def read_coordinates(a_player_index, a_data):
    global avail_turn_count
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
                elif a_data[a_iy][a_ix]:
                    print("Wrong coordinates - cell is already used. Re-enter your coordinates!")
                else:
                    return a_ix, a_iy


# data funcs
def create_field():
    a_data = []
    for i in range(0, size_y):
        a_data.append([])
        for j in range(0, size_x):
            a_data[-1].append(0)

    return a_data


def matrix_has_count_value(a_data, a_value, a_req_count):
    # horizontal
    for a_row_index in range(size_y):
        a_count = 0
        for a_col_index in range(size_x):
            if a_data[a_row_index][a_col_index] == a_value:
                a_count += 1

        if a_count >= a_req_count:
            return True

    # vertical
    for a_col_index in range(size_x):
        a_count = 0
        for a_row_index in range(size_y):
            if a_data[a_row_index][a_col_index] == a_value:
                a_count += 1

        if a_count >= a_req_count:
            return True

    # diagonal 1
    for a_offset_y in range(size_y - min_size + 1):
        for a_offset_x in range(size_x - min_size + 1):
            a_count = 0
            for a_diag_index in range(min_size):
                if a_data[a_offset_y + a_diag_index][a_offset_x + a_diag_index] == a_value:
                    a_count += 1

            if a_count >= a_req_count:
                return True

    # diagonal 2
    for a_offset_y in range(size_y - min_size + 1):
        for a_offset_x in range(size_x - min_size + 1):
            a_count = 0
            for a_diag_index in range(min_size):
                if a_data[a_offset_y + a_diag_index][a_offset_x + min_size - 1 - a_diag_index] == a_value:
                    a_count += 1

            if a_count >= a_req_count:
                return True

    # no one line found
    return False


# return values:
#    0: game continue
#   -1: no one win
#    1: player with index 0 wins
#    2: player with index 1 wins
def get_end_index(a_data):
    for curr_player_index in range(0, 2):
        if matrix_has_count_value(a_data, 1 + curr_player_index, win_count):
            return 1 + player_index

    # no available turns
    if not avail_turn_count:
        return -1

    # no end yet
    return 0


def get_coordinates_by_index(a_data, a_index):
    if a_index >= avail_turn_count:
        raise Exception("get_coordinates_by_index: a_index")

    a_curr_index = 0
    for a_row_index in range(0, len(a_data)):
        for a_col_index in range(0, len(a_data[a_row_index])):
            if not a_data[a_row_index][a_col_index]:
                if a_curr_index == a_index:
                    return a_col_index, a_row_index
                else:
                    a_curr_index += 1

    raise Exception("get_coordinates_by_index: wrong a_data, a_index")


def computer_turn_random(a_player_index, a_data):
    a_index = random.randint(0, avail_turn_count - 1)
    time.sleep(computer_delay)
    return get_coordinates_by_index(a_data, a_index)


turn_index = 0
player_index = 0
data = create_field()
avail_turn_count = size_x * size_y
computer_turn = computer_turn_random

is_multiplayer = False

if is_multiplayer:
    player_funcs = [read_coordinates, read_coordinates]
else:
    player_funcs = [computer_turn, computer_turn]
    player_funcs[human_player_index] = read_coordinates

show_field(data)
while True:
    show_turn_title(turn_index, player_index)

    coordinates = player_funcs[player_index](player_index, data)
    # if Player input is Exit
    if coordinates is None:
        print("Exiting application...")
        exit(0)
    show_turn(coordinates)

    iy = coordinates[1]
    ix = coordinates[0]
    data[iy][ix] = player_index + 1
    avail_turn_count -= 1

    show_field(data)

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
