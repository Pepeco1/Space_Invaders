from MainMenu import *
from Game import *
from player_class import *


game_state = 0

while True:

    if game_state == 0:
        game_state = menu()

    if game_state == 1:
        game()
        # window.set_background_color((0, 0, 0))
        # if keyboard.key_pressed("ESC"):
        #     game_state = 0

        # player_shoot()
        # update_counters()
        # window.set_background_color((0, 0, 0))
        # # fundo.draw()
        #
        # for bullet in bullets:
        #     bullet.draw()
        # bullet_movement()
        #
        # barricade_1.draw()
        # barricade_2.draw()
        # barricade_3.draw()
        # player.update()
        # player.movement_update()
        # window.update()



