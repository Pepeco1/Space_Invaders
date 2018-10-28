from PPlay.sprite import *
from PPlay.window import*
from PPlay.sound import *
from PPlay.gameimage import *
from player_class import *


def game():

    # global game vars.
    global game_state
    global game_speed

    # global shoot vars.
    # global enemy_shoot_delay
    # global player_shoot_delay
    # global player_shoot_tick

    game_dificulty = 1
    game_speed = 1

    # window size variables.
    w_height = 500
    w_width = 700

    # window creation.
    window = Window(w_width, w_height)
    window.set_title("Pepeco_Invaders")
    # fundo = GameImage("sprites/mini_fundo_game.png")

    # setting background, keyboard and inputs.
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()
    window.set_background_color([0, 0, 0])

    # sprites creation.
    player = Player(window, "sprites/player.png", keyboard)
    player.orientation = -1
    barricade_1 = Sprite("sprites/barricade.png")
    barricade_2 = Sprite("sprites/barricade.png")
    barricade_3 = Sprite("sprites/barricade.png")

    # sounds creation.
    # bullet_sound = Sound("sounds/shoot.wav")

    # setting sprites positions.
    player.set_position((window.width/2 - player.width), (window.height - player.height))
    barricade_1.set_position(((window.width/4) * 1) - (barricade_1.width/2), 300)
    barricade_2.set_position(((window.width/4) * 2) - (barricade_2.width/2), 300)
    barricade_3.set_position(((window.width/4) * 3) - (barricade_3.width/2), 300)

    # speed variable.
    player_x_speed = 0

    # bullets vector.
    bullets = []


    # shooting related vars.
    # enemy_shoot_delay = 1 / game_speed
    player.shoot_delay = 1 / game_speed * 0.5
    player.shoot_tick = player.shoot_delay

    def adjust_bullet(actor, bullet):

        # bullet x position
        x_fire = actor.x + (actor.width / 2) - (bullet.width / 2)

        # bullet y position
        y_fire = actor.y + actor.height - bullet.height

        bullet.x = x_fire
        bullet.y = y_fire

    def shoot(shooter):
        # sets the clock as 0.
        shooter.shoot_tick = 0

        # bullet creation
        b = Sprite("sprites/bullet.png")

        # adjust bullet position.
        adjust_bullet(shooter, b)

        # puts the bullet in the bullets vector.
        bullets.append(b)

        # bullet_sound.play()

    def player_shoot():
        if keyboard.key_pressed("space"):
            if player.shoot_tick > player.shoot_delay:
                shoot(player)

    def bullet_movement(shooter):
        for shot in bullets:
            shot.move_y(shooter.orientation * 200 * window.delta_time() * game_speed)

            if shot.y < -shot.height or shot.y > window.height + shot.height:
                bullets.remove(shot)

    def update_counters():
        player.shoot_tick += window.delta_time()

    while True:
        window.set_background_color((0, 0, 0))
        if keyboard.key_pressed("ESC"):
            game_state = 0

        player_shoot()
        update_counters()
        # fundo.draw()

        print(len(bullets))
        for bullet in bullets:
            bullet.draw()
        bullet_movement(player)

        barricade_1.draw()
        barricade_2.draw()
        barricade_3.draw()
        player.update()
        player.movement_update()
        window.update()

