from MainMenu import *
from Game import *
from player_class import *


# # window size variables.
# w_height = 500
# w_width = 700


# # window creation.
# window = Window(w_width, w_height)
# window.set_title("Pepeco_Invaders")
# fundo = GameImage("sprites/fundo_menu.jpg")
#
# # sprites creation.
# player = Sprite("sprites/player.png")
# barricade_1 = Sprite("sprites/barricade.png")
# barricade_2 = Sprite("sprites/barricade.png")
# barricade_3 = Sprite("sprites/barricade.png")
#
# # setting background, keyboard and inputs.
# keyboard = window.get_keyboard()
# mouse = window.get_mouse()
# window.set_background_color([0, 0, 0])
#
# # setting sprites positions.
# player.set_position(window.width/2, 400)
# barricade_1.set_position(((window.width/4) * 1) - (barricade_1.width/2), 300)
# barricade_2.set_position(((window.width/4) * 2) - (barricade_2.width/2), 300)
# barricade_3.set_position(((window.width/4) * 3) - (barricade_3.width/2), 300)
#
# # speed variable.
# player_x_speed = 0
#
# game_state = 0
# game_dificulty = 1
# game_speed = 1
#
# # window size variables.
# w_height = 500
# w_width = 700
#
# # window creation.
# window = Window(w_width, w_height)
# window.set_title("Pepeco_Invaders")
# # fundo = GameImage("sprites/mini_fundo_game.png")
#
# # setting background, keyboard and inputs.
# keyboard = window.get_keyboard()
# mouse = window.get_mouse()
# window.set_background_color([0, 0, 0])
#
# # sprites creation.
# player = Player(window, "sprites/player.png", keyboard)
# player.orientation = -1
# barricade_1 = Sprite("sprites/barricade.png")
# barricade_2 = Sprite("sprites/barricade.png")
# barricade_3 = Sprite("sprites/barricade.png")
#
# # sounds creation.
# # bullet_sound = Sound("sounds/shoot.wav")
#
# # setting sprites positions.
# player.set_position((window.width/2 - player.width), (window.height - player.height))
# barricade_1.set_position(((window.width/4) * 1) - (barricade_1.width/2), 300)
# barricade_2.set_position(((window.width/4) * 2) - (barricade_2.width/2), 300)
# barricade_3.set_position(((window.width/4) * 3) - (barricade_3.width/2), 300)
#
# # speed variable.
# player_x_speed = 0
#
# # bullets vector.
# bullets = []
#
#
# shooting related vars.
# enemy_shoot_delay = 1 / game_speed
#player.shoot_delay = 1 / game_speed * 0.5
#player.shoot_tick = player.shoot_delay


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



