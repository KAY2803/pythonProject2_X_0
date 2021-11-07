# Реализован процесс игры

import game_logic # импортируем функции из модуля game_logic

game_logic.game_field() # рисуем игровое поле

while True:
    game_logic.moving_player() # вызываем функцию для совершения хода игрока "Х"
    if game_logic.checking() == 'Переход хода': # вызываем функцию для проверки выигрышных комбинаций и свободных ячеек
        game_logic.moving_player() # вызываем функцию для совершения хода игрока "O"
        # вызываем функцию для проверки выигрышных комбинаций и свободных ячеек
        if game_logic.checking() == 'Переход хода':
            continue
        else:
            break
    else:
         break