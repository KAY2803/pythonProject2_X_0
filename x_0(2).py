field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

def player_x():
    while True:
        try:
            x = int(input('Выберите ячейку для "x" от 1 до 9:'))
            if x not in range(1, 10):
                print('Ячейка не существует. Введите другое число от 1 до 9')
                continue
            if field[x - 1] == 'X' or field[x - 1] == 'O':
                print('Ячейка занята. Введите другое число от 1 до 9')
                continue
            else:
                field[x - 1] = 'X'
                print(field)
        except ValueError:
            print('Ячейка не существует. Выберите от 1 до 9')
            continue
        if checking() == 'Переход хода':
            break
        else:
            print(checking())
            break
    return checking()


def player_0():
    while True:
        try:
            o = int(input('Выберите ячейку для "O" от 1 до 9:'))
            if o not in range(1, 10):
                print('Ячейка не существует. Введите другое число от 1 до 9')
                continue
            if field[o - 1] == 'X' or field[o - 1] == 'O':
                print('Ячейка занята. Введите другое число от 1 до 9')
                continue
            else:
                field[o - 1] = 'O'
                print(field)
        except ValueError:
            print('Ячейка не существует. Выберите от 1 до 9')
            continue
        if checking() == 'Переход хода':
            break
        else:
            print(checking())
            break
    return checking()


def checking():
    if field[::3] == ['X'] * 3 or field[1::3] == ['X'] * 3 or field[2::3] == ['X'] * 3 or field[::4] == ['X'] * 3:
        return 'Игра окончена. Выиграл Х'
    elif field[0:3] == ['X'] * 3 or field[3:6] == ['X'] * 3 or field[6:9] == ['X'] * 3 or field[2:7:2] == ['X'] * 3:
        return 'Игра окончена. Выиграл Х'
    elif field[::3] == ['O'] * 3 or field[1::3] == ['O'] * 3 or field[2::3] == ['O'] * 3 or field[::4] == ['O'] * 3:
        return 'Игра окончена. Выиграл O'
    elif field[0:3] == ['O'] * 3 or field[3:6] == ['O'] * 3 or field[6:9] == ['O'] * 3 or field[2:7:2] == ['O'] * 3:
        return 'Игра окончена. Выиграл O'
    else:
        return 'Переход хода'

while True:
    if player_x() == 'Переход хода':
        if player_0() == 'Переход хода':
            continue
        else:
            break
    else:
        break
