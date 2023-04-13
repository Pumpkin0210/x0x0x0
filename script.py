def pole():
    print("     0  1  2  ")
    for i, row in enumerate(field):
        row_str = f"  {i}  {'  '.join(row)}"
        print(row_str)
    print()


def vvod():
    while True:
        coordi = input("Ваш ход: ").split()
#################################################
        if len(coordi) > 2:
            print(" Слишком много координат... ")
            continue
        if len(coordi) < 2:
            print(" Слишком мало координат... ")
            continue
###############################################
        x, y = coordi
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите координаты - числа. ")
            continue
###############################################
        x, y = int(x), int(y)
        if not -1 < x < 3 or not -1 < y < 3:
            print(" Заданные координаты не найдены. ")
            continue
################################################
        if field[x][y] != " ":
            print(" Тут занято... ")
            continue

        return x, y


def final():
    pobeda = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coordi in pobeda:
        symbols = []
        for c in coordi:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("хХх Выиграл X! хХх")
            return True
        if symbols == ["0", "0", "0"]:
            print("о0о Выиграл 0! о0о")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
schet = 0
while True:
    schet += 1
    pole()
    if schet % 2 == 1:
        print(" Ходит крестик.")
    else:
        print(" Ходит нолик.")
    x, y = vvod()
    if schet % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if final():
        break
    if schet == 9:
        print(" Ничья :(")
        break
