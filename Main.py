from MainMenu import *
from Game import *


# # window size variables.
# w_height = 500
# w_width = 700


# # window creation.
# window = Window(w_width, w_height)
# window.set_title("Pepeco_Invaders")
# fundo = GameImage("sprites/fundo.jpg")

# # sprites creation.
# player = Sprite("sprites/sprite_8.png")
# barricade_1 = Sprite("sprites/sprite_9.png")
# barricade_2 = Sprite("sprites/sprite_9.png")
# barricade_3 = Sprite("sprites/sprite_9.png")

# # setting background, keyboard and inputs.
# keyboard = window.get_keyboard()
# mouse = window.get_mouse()
# window.set_background_color([0, 0, 0])

# # setting sprites positions.
# player.set_position(window.width/2, 400)
# barricade_1.set_position(((window.width/4) * 1) - (barricade_1.width/2), 300)
# barricade_2.set_position(((window.width/4) * 2) - (barricade_2.width/2), 300)
# barricade_3.set_position(((window.width/4) * 3) - (barricade_3.width/2), 300)
#
# # speed variable.
# player_x_speed = 0

game_state = 0
game_dificulty = 1


while True:

    if game_state == 0:
        game_state = menu()

    if game_state == 1:
        game_state = game()


