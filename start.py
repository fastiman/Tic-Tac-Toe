symbols = input("Enter cells: ")
symbols = list(symbols)


def state():
    print("---------")
    print("|", symbols[0], symbols[1], symbols[2], "|")
    print("|", symbols[3], symbols[4], symbols[5], "|")
    print("|", symbols[6], symbols[7], symbols[8], "|")
    print("---------")


state()


def check_coordinates(x):
    if symbols[x] in ['_', ' ']:
        symbols[x] = 'X'
        state()
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False


while True:
    coordinates = input("Enter coordinates: ")
    a = coordinates.replace(" ", "")
    if not a.isdigit():
        print("You should enter numbers!")
        continue

    a, b = map(int, coordinates.split())
    if a not in [1, 2, 3] or b not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        continue

    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)

    if coordinates == "1 3":
        if not check_coordinates(0):
            continue
    elif coordinates == "2 3":
        if not check_coordinates(1):
            continue
    elif coordinates == "3 3":
        if not check_coordinates(2):
            continue
    elif coordinates == "1 2":
        if not check_coordinates(3):
            continue
    elif coordinates == "2 2":
        if not check_coordinates(4):
            continue
    elif coordinates == "3 2":
        if not check_coordinates(5):
            continue
    elif coordinates == "1 1":
        if not check_coordinates(6):
            continue
    elif coordinates == "2 1":
        if not check_coordinates(7):
            continue
    elif coordinates == "3 1":
        if not check_coordinates(8):
            continue
    break


row1 = symbols[0:3]
row2 = symbols[3:6]
row3 = symbols[6:9]
col1 = [symbols[0], symbols[3], symbols[6]]
col2 = [symbols[1], symbols[4], symbols[7]]
col3 = [symbols[2], symbols[5], symbols[8]]
diag1 = [symbols[0], symbols[4], symbols[8]]
diag2 = [symbols[2], symbols[4], symbols[6]]


def x_wins():
    if row1.count('X') == 3 or row2.count('X') == 3 or row3.count('X') == 3 or \
            diag1.count('X') == 3 or diag2.count('X') == 3 or \
            col1.count('X') == 3 or col2.count('X') == 3 or col3.count('X') == 3:
        return True


def o_wins():
    if row1.count('O') == 3 or row2.count('O') == 3 or row3.count('O') == 3 or \
            diag1.count('O') == 3 or diag2.count('O') == 3 or \
            col1.count('O') == 3 or col2.count('O') == 3 or col3.count('O') == 3:
        return True


if abs(symbols.count('X') - symbols.count('O')) >= 2:
    print('Impossible')
elif x_wins() and o_wins():
    print('Impossible')
elif x_wins():
    print('X wins')
elif o_wins():
    print('O wins')
elif '_' in symbols or ' ' in symbols:
    print('Game not finished')
else:
    print('Draw')
