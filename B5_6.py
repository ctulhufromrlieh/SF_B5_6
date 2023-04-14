size_x = 3
size_y = 3
min_size = min(size_x, size_y)
win_count = min_size
is_show_coords = min_size < 10

def fieldValueToSymbol(field_value):
    if field_value == 0:
        return " "
    elif field_value == 1:
        return "X"
    elif field_value == 2:
        return "O"
    else:
        raise Exception("show_field_value: wrong field_value")

def playerIndexToName(player_index):
    return f"Player {player_index + 1}"

def endIndexToName(endIndex):
    if endIndex == 1:
        return "Congratulations! Player #1 won!"
    elif endIndex == 2:
        return "Congratulations! Player #2 won!"
    else:
        raise Exception("endIndexToName: wrong endIndex")


def showLine(char):
    print(char * (size_x + 1))

def showField(data):
    row_index = 0
    for row in data:
        row_strs = list(map(fieldValueToSymbol, row))
        row_line ="".join(row_strs)
        if is_show_coords:
            row_line = f"{row_index + 1}|{row_line}"
        print(row_line)
        row_index += 1

def showTurn(turn_index, player_index, data):
    showLine("=")
    print(f"Round number #{turn_index + 1}.")
    print(f"Player {player_index + 1} turn:")
    showLine("=")

    if is_show_coords:
        # coords_x = list(map(str(range(0, size_x))))
        coords_x = map(str, range(1, size_x + 1))
        coord_line = 2 * " " + "".join(coords_x)
        print(coord_line)
        print('-' * (size_x + 2))

    showField(data)

def createField():
    data = []
    for i in range(0, size_y):
        data.append([])
        for j in range(0, size_x):
            data[-1].append(0)
            # data[-1].append(1)

    return data

def strToInt(s):
    try:
        return int(s)
    except ValueError:
        return None

def readCoords(player_index):
    while True:
        coords_s = input(f"Your turn, {playerIndexToName(player_index)}: ")

        coords = coords_s.split()
        if len(coords) < 2:
            print("Wrong coordinates - less then two numbers. Re-enter your coordinates!")
        else:
            ix = strToInt(coords[0])
            iy = strToInt(coords[1])
            if not ix or not iy:
                print("Wrong coordinates - not a number. Re-enter your coordinates!")
            else:
                ix -= 1
                iy -= 1
                if ix < 0 or ix >= size_x or iy < 0 or iy >= size_y:
                    print("Wrong coordinates - cell is out of field. Re-enter your coordinates!")
                elif data[iy][ix]:
                    print("Wrong coordinates - cell is already used. Re-enter your coordinates!")
                else:
                    data[iy][ix] = player_index + 1
                    break

def getEndIndex(data):
    for player_index in range(0, 2):
        # row check
        for row in data:
            if row.count(player_index + 1) == win_count:
                return player_index + 1
        #col check
        for col_index in range(0, size_x):
            count = 0
            for row_index in range(0, size_y):
                if data[row_index][col_index] == player_index + 1:
                    count += 1
            if count == win_count:
                return player_index + 1
        #diag check #1
        count = 0
        for i in range(0, min_size):
            if data[i][i] == player_index + 1:
                count += 1
        if count == win_count:
            return player_index + 1
        #diag check #2
        count = 0
        for i in range(0, min_size):
            if data[min_size - 1 - i][i] == player_index + 1:
                count += 1
        if count == win_count:
            return player_index + 1

        # no one wins
        return 0


curr_turn_index = 0
curr_player_index = 0
data = createField()

while True:
    showTurn(curr_turn_index, curr_player_index, data)

    readCoords(curr_player_index)

    endIndex = getEndIndex(data)
    if endIndex > 0:
        print(endIndexToName(endIndex))
        showField(data)
        break

    if curr_player_index == 0:
        curr_player_index = 1
    elif curr_player_index == 1:
        curr_player_index = 0
    else:
        raise Exception("main: Wrong curr_player_index")
    curr_turn_index += 1


