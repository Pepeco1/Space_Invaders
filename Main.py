from MainMenu import *
from Game import *
from player_class import *


game_state = 0

while True:

    if game_state == 0:
        game_state = menu()

    if game_state == 1:
        game()
