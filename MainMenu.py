from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from Dificuldade import dificuldade

def menu():

    global game_state

    # window size variables.
    w_height = 700
    w_width = 700

    # window creation.
    window = Window(w_width, w_height)
    window.set_title("Menu")
    fundo = GameImage("sprites/fundo_menu.jpg")

    # setting background and mouse inputs.
    mouse = window.get_mouse()

    # creating sprites.
    sprite_jogar = Sprite("sprites/retang.png")
    sprite_jogar_2 = Sprite("sprites/retang_2.png")

    sprite_dificuldade = Sprite("sprites/retang.png")
    sprite_dificuldade_2= Sprite("sprites/retang_2.png")

    sprite_placar = Sprite("sprites/retang.png")
    sprite_placar_2 = Sprite("sprites/retang_2.png")

    sprite_sair = Sprite("sprites/retang.png")
    sprite_sair_2= Sprite("sprites/retang_2.png")

    #setting sprites positions.
    sprite_width = sprite_jogar.width
    sprite_height = sprite_jogar.height

    pos_sprites_x = (window.width/2) - (sprite_width/2)
    pos_sprites_y = window.height/5

    sprite_jogar.set_position(pos_sprites_x, ((pos_sprites_y)*1) - (sprite_height/2))
    sprite_jogar_2.set_position(pos_sprites_x, ((pos_sprites_y)*1) - (sprite_height/2))

    sprite_dificuldade.set_position(pos_sprites_x, ((pos_sprites_y)*2) - (sprite_height/2))
    sprite_dificuldade_2.set_position(pos_sprites_x, ((pos_sprites_y)*2) - (sprite_height/2))

    sprite_placar.set_position(pos_sprites_x, ((pos_sprites_y)*3) - (sprite_height/2))
    sprite_placar_2.set_position(pos_sprites_x, ((pos_sprites_y)*3) - (sprite_height/2))

    sprite_sair.set_position(pos_sprites_x, ((pos_sprites_y)*4) - (sprite_height/2))
    sprite_sair_2.set_position(pos_sprites_x, ((pos_sprites_y)*4) - (sprite_height/2))

    while True:
        fundo.draw()
        window.draw_text("MENU", pos_sprites_x + sprite_width/2 - 30, ((pos_sprites_y)*1) - (sprite_height/2) - 50 , size = 18, color = (255, 255,255),
                         font_name = "Arial", bold = True, italic = False)
        pos_mouse = mouse.get_position()
        if pos_sprites_x < pos_mouse[0] < (pos_sprites_x + sprite_width):
            if sprite_jogar.y < pos_mouse[1] < (sprite_jogar.y + sprite_jogar.height):
                sprite_jogar_2.draw()
                if mouse.is_button_pressed(1):
                    game_state = 1
                    return game_state
            else:
                sprite_jogar.draw()

            if sprite_dificuldade.y < pos_mouse[1] < (sprite_dificuldade.y + sprite_dificuldade.height):
                sprite_dificuldade_2.draw()
                if mouse.is_button_pressed(1):
                    dificuldade()
            else:
                sprite_dificuldade.draw()

            if sprite_placar.y < pos_mouse[1] < (sprite_placar.y + sprite_placar.height):
                sprite_placar_2.draw()
                if mouse.is_button_pressed(1):
                    placar()
            else:
                sprite_placar.draw()

            if sprite_sair.y < pos_mouse[1] < (sprite_sair.y + sprite_sair.height) :
                sprite_sair_2.draw()
                if mouse.is_button_pressed(1):
                    exit()
            else:
                sprite_sair.draw()

        else:
            sprite_jogar.draw()
            sprite_dificuldade.draw()
            sprite_placar.draw()
            sprite_sair.draw()

        window.update()

