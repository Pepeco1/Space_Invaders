from player_class import *
from PPlay.window import *


window = Window(500, 500)
window.set_background_color((255, 255, 255))
keyboard = window.get_keyboard()
player = Player(window, "sprites/player.png", keyboard)

while True:

    window.set_background_color((255, 255, 255))
    player.movement_update()
    window.update()
