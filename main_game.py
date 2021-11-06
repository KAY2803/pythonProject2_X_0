# Реализован процесс игры

import game_logic

game_logic.game_field()

while True:
    game_logic.player_x()
    if game_logic.checking() == 'Переход хода':
        game_logic.player_0()
        if game_logic.checking() == 'Переход хода':
            continue
        else:
            break
    else:
         break
