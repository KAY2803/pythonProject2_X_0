# содержит функции, реализующие логику игры.
# формат игрового поля - одномерный список, 3 х 3 (всего 9 ячеек).

field = list(range(1, 10))

# Функция для визуализации игрового поля
def game_field():
    game_field = ''
    for row in field[0:3]:
        game_field += str(row).rjust(2)
        for col in field[2: 8: 3]:
            game_field += str(col+row).rjust(2)
        game_field += '\n'
    return game_field
print(game_field())

# Функция для принятия значений игрока "Х" и добавление его в игровое поле
def player_x():
    global field
    while True:
        try:
            x = int(input('Выберите ячейку для "x" от 1 до 9:'))
            if x not in range(1, 10): # Проверяем, входит ли введенное значение в диапазон ячеек игрового поля
                print('Ячейка не существует. Введите другое число от 1 до 9')
                continue
            if field[x - 1] == 'X' or field[x - 1] == 'O': # Проверяем, свободна ли выбранная ячейка
                print('Ячейка занята. Введите другое число от 1 до 9')
                continue
            else:
                field[x - 1] = 'X' # Меняем в игровом поле введенное значение на "Х"
                print(f"{' '.join(map(str, field[:3])).rjust(3)}\n{' '.join(map(str, field[3:6])).rjust(3)}\n"
                      f"{' '.join(map(str, field[6:])).rjust(3)}")
        except ValueError: # исключаем ошибку введения не int
            print('Ячейка не существует. Выберите от 1 до 9')
            continue
        if x in range(1, 10):
            break
        else:
            break
    return x

# Функция для принятия значений игрока "O" и добавления его в игровое поле
def player_0():
    while True:
        try:
            o = int(input('Выберите ячейку для "O" от 1 до 9:'))
            if o not in range(1, 10): # Проверяем, входит ли введенное значение в диапазон ячеек игрового поля
                print('Ячейка не существует. Введите другое число от 1 до 9')
                continue
            if field[o - 1] == 'X' or field[o - 1] == 'O': # Проверяем, свободна ли выбранная ячейка
                print('Ячейка занята. Введите другое число от 1 до 9')
                continue
            else:
                field[o - 1] = 'O' # Меняем в игровом поле введенное значение на "O"
                print(f"{' '.join(map(str, field[:3])).rjust(3)}\n{' '.join(map(str, field[3:6])).rjust(3)}\n"
                      f"{' '.join(map(str, field[6:])).rjust(3)}")
        except ValueError: # исключаем ошибку введения не int
            print('Ячейка не существует. Выберите от 1 до 9')
            continue
        if o in range(1, 10):
            break
    return o

# Функция проверки результатов: проверяет на наличие выигрышных комбинаций и свободных ячеек
def checking():
    global field
    if field[::3] == ['X'] * 3 or field[1::3] == ['X'] * 3 or field[2::3] == ['X'] * 3 or field[::4] == ['X'] * 3:
        print('Игра окончена. Выиграл Х')
        return 'Игра окончена. Выиграл Х'
    elif field[0:3] == ['X'] * 3 or field[3:6] == ['X'] * 3 or field[6:9] == ['X'] * 3 or field[2:7:2] == ['X'] * 3:
        print('Игра окончена. Выиграл Х')
        return 'Игра окончена. Выиграл Х'
    elif field[::3] == ['O'] * 3 or field[1::3] == ['O'] * 3 or field[2::3] == ['O'] * 3 or field[::4] == ['O'] * 3:
        print('Игра окончена. Выиграл O')
        return 'Игра окончена. Выиграл O'
    elif field[0:3] == ['O'] * 3 or field[3:6] == ['O'] * 3 or field[6:9] == ['O'] * 3 or field[2:7:2] == ['O'] * 3:
        print('Игра окончена. Выиграл O')
        return 'Игра окончена. Выиграл O'
    elif len(set(field)) == 2:
        print('Игра окончена. Ничья')
        return 'Игра окончена. Ничья'
    else:
        print('Переход хода')
        return 'Переход хода'

