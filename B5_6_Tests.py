from B5_6 import *


def get_avail_turn_count_by_matrix(a_field):
    a_count = 0
    for a_row in a_field:
        for a_elem in a_row:
            if not a_elem:
                a_count += 1
    return a_count


def make_matrix_checker(a_field, a_end_index):
    a_size_x = len(a_field[0])
    a_size_y = len(a_field)
    a_minsize = min(a_size_x, a_size_y)
    a_data = {"field": a_field,
              "size_x": a_size_x,
              "size_y": a_size_y,
              "min_size": a_minsize,
              "win_count": a_minsize,
              "avail_turn_count":  get_avail_turn_count_by_matrix(a_field)}

    def wrapper():
        return get_end_index(a_data) == a_end_index

    return wrapper


check_list = []
# 3 x 3
# horizontal
check_list.append(make_matrix_checker(
    [[1, 1, 1],
     [2, 0, 2],
     [0, 2, 0]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 1],
     [1, 1, 2],
     [2, 2, 2]], 2))
# vertical
check_list.append(make_matrix_checker(
    [[2, 1, 1],
     [0, 1, 2],
     [2, 1, 0]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 1, 2],
     [0, 0, 2]], 2))
# diagonal
check_list.append(make_matrix_checker(
    [[1, 2, 0],
     [0, 1, 2],
     [0, 0, 1]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 2, 0],
     [2, 0, 1]], 2))
# no win
check_list.append(make_matrix_checker(
    [[1, 2, 1],
     [1, 2, 1],
     [2, 1, 2]], -1))
check_list.append(make_matrix_checker(
    [[2, 1, 2],
     [1, 2, 1],
     [1, 2, 1]], -1))
# 3 x 4
# horizontal
check_list.append(make_matrix_checker(
    [[1, 1, 1],
     [2, 0, 2],
     [0, 0, 0],
     [0, 2, 0]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 1],
     [1, 1, 2],
     [0, 0, 0],
     [2, 2, 2]], 2))
# vertical
check_list.append(make_matrix_checker(
    [[2, 1, 1],
     [2, 0, 2],
     [2, 1, 0],
     [2, 1, 0]], 2))
check_list.append(make_matrix_checker(
    [[2, 1, 1],
     [0, 0, 2],
     [2, 1, 0],
     [2, 1, 0]], 0))
check_list.append(make_matrix_checker(
    [[2, 1, 0],
     [0, 1, 1],
     [0, 0, 1],
     [2, 1, 1]], 1))
check_list.append(make_matrix_checker(
    [[2, 1, 2],
     [2, 1, 1],
     [2, 0, 0],
     [0, 0, 1]], 2))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [2, 1, 1],
     [2, 0, 0],
     [2, 0, 1]], 2))
# diagonal 1
check_list.append(make_matrix_checker(
    [[1, 2, 0],
     [0, 1, 2],
     [0, 0, 1],
     [0, 0, 1]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 1, 2],
     [2, 2, 1],
     [2, 0, 0]], 2))
check_list.append(make_matrix_checker(
    [[1, 2, 0],
     [0, 1, 2],
     [0, 0, 0],
     [0, 0, 1]], 0))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 1, 2],
     [2, 0, 1],
     [2, 0, 1]], 0))
# diagonal 2
check_list.append(make_matrix_checker(
    [[1, 2, 2],
     [0, 2, 2],
     [2, 0, 1],
     [0, 0, 1]], 2))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 0, 1],
     [2, 1, 1],
     [1, 0, 0]], 1))
check_list.append(make_matrix_checker(
    [[1, 2, 1],
     [0, 1, 2],
     [0, 0, 0],
     [0, 0, 1]], 0))
check_list.append(make_matrix_checker(
    [[0, 1, 2],
     [1, 1, 2],
     [2, 0, 1],
     [2, 0, 0]], 0))
# no win
check_list.append(make_matrix_checker(
    [[1, 2, 1],
     [2, 1, 2],
     [2, 1, 2],
     [1, 2, 1]], -1))
check_list.append(make_matrix_checker(
    [[1, 2, 2],
     [2, 1, 1],
     [1, 2, 2],
     [2, 1, 1]], -1))
# 4 x 3
# horizontal
check_list.append(make_matrix_checker(
    [[2, 2, 2, 2],
     [1, 0, 1, 1],
     [1, 2, 0, 0]], 2))
check_list.append(make_matrix_checker(
    [[2, 0, 2, 2],
     [1, 0, 1, 1],
     [1, 2, 0, 0]], 0))
check_list.append(make_matrix_checker(
    [[2, 0, 0, 2],
     [1, 1, 0, 1],
     [0, 1, 1, 1]], 1))
check_list.append(make_matrix_checker(
    [[2, 2, 2, 0],
     [1, 1, 0, 0],
     [2, 1, 0, 1]], 2))
check_list.append(make_matrix_checker(
    [[0, 2, 2, 2],
     [1, 1, 0, 0],
     [2, 1, 0, 1]], 2))
# vertical
check_list.append(make_matrix_checker(
    [[1, 2, 0, 0],
     [1, 0, 0, 2],
     [1, 2, 0, 0]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 0, 2],
     [1, 1, 0, 2],
     [1, 2, 0, 2]], 2))
# diagonal 1
check_list.append(make_matrix_checker(
    [[1, 0, 2, 0],
     [2, 2, 0, 0],
     [2, 2, 1, 1]], 2))
check_list.append(make_matrix_checker(
    [[0, 1, 2, 1],
     [1, 0, 1, 0],
     [2, 1, 1, 0]], 1))
check_list.append(make_matrix_checker(
    [[1, 0, 0, 0],
     [2, 1, 0, 0],
     [1, 2, 0, 1]], 0))
check_list.append(make_matrix_checker(
    [[0, 1, 2, 2],
     [1, 1, 0, 0],
     [2, 2, 1, 0]], 0))
# diagonal 2
check_list.append(make_matrix_checker(
    [[1, 0, 0, 0],
     [2, 1, 0, 0],
     [0, 2, 1, 1]], 1))
check_list.append(make_matrix_checker(
    [[0, 1, 2, 2],
     [1, 1, 2, 0],
     [2, 2, 1, 0]], 2))
check_list.append(make_matrix_checker(
    [[1, 0, 0, 0],
     [2, 1, 0, 0],
     [0, 2, 0, 1]], 0))
check_list.append(make_matrix_checker(
    [[0, 1, 2, 2],
     [1, 1, 0, 0],
     [2, 2, 1, 1]], 0))
# no win
check_list.append(make_matrix_checker(
    [[1, 2, 2, 1],
     [2, 1, 1, 2],
     [1, 2, 2, 1]], -1))
check_list.append(make_matrix_checker(
    [[1, 2, 1, 2],
     [2, 1, 2, 1],
     [2, 1, 2, 1]], -1))

all_count = len(check_list)
ok_count = 0
failed_checks_indices = []
for curr_check_index in range(len(check_list)):
    if check_list[curr_check_index]():
        ok_count += 1
    else:
        failed_checks_indices.append(curr_check_index)

print(f"Tests passed succesfully: {ok_count}/{all_count}")
if ok_count == all_count:
    print("All tests passed succesfully!")
else:
    print(f"{all_count - ok_count} tests FAILED:")
    print(failed_checks_indices)
