from PPlay.sprite import *
from PPlay.window import*
from PPlay.sound import *
from PPlay.gameimage import *

def game():

    def adjust_bullet(actor, bullet):

        # bullet x position
        x_fire = actor.x + (actor.width / 2) - (bullet.width / 2)

        # bullet y position
        y_fire = actor.y + actor.height - bullet.height

        bullet.x = x_fire
        bullet.y = y_fire


    def shoot(shooter):
        global player_shoot_tick
        # sets the clock as 0.
        player_shoot_tick = 0

        # bullet creation
        b = Sprite("sprites/bullet.png")

        # adjust bullet position.
        adjust_bullet(shooter, b)

        # puts the bullet in the bullets vector.
        bullets.append(b)
        bullet_sound.play()
        print(bullets)

    def player_shoot():
        global player_shoot_tick
        if keyboard.key_pressed("space"):
            print("foi")
            if player_shoot_tick > player_shoot_delay:
                shoot(player)
                print(player_shoot_tick)

    def bullet_movement():
        for bullet in bullets:
            bullet.move_y(-200 * window.delta_time() * game_speed)

            if bullet.y < -bullet.height or bullet.y > window.height + bullet.height:
                bullets.remove(bullet)

    def update_counters():
        global player_shoot_tick
        player_shoot_tick += window.delta_time()

    # global game vars.
    global game_state
    global game_speed
    global teste
    teste = 0

    # global shoot vars.
    global enemy_shoot_delay
    global player_shoot_delay
    global player_shoot_tick

    # window size variables.
    w_height = 500
    w_width = 700

    # window creation.
    window = Window(w_width, w_height)
    window.set_title("Pepeco_Invaders")
    #fundo = GameImage("sprites/mini_fundo_game.png")

    # sprites creation.
    player = Sprite("sprites/player.png")
    barricade_1 = Sprite("sprites/barricade.png")
    barricade_2 = Sprite("sprites/barricade.png")
    barricade_3 = Sprite("sprites/barricade.png")

    # sounds creation.
    bullet_sound = Sound("sounds/shoot.wav")

    # setting background, keyboard and inputs.
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()
    window.set_background_color([0, 0, 0])

    # setting sprites positions.
    player.set_position(window.width/2, 400)
    barricade_1.set_position(((window.width/4) * 1) - (barricade_1.width/2), 300)
    barricade_2.set_position(((window.width/4) * 2) - (barricade_2.width/2), 300)
    barricade_3.set_position(((window.width/4) * 3) - (barricade_3.width/2), 300)

    # speed variable.
    player_x_speed = 0

    # bullets vector.
    bullets = []

    # game speed.
    game_speed = 1

    # shooting related vars.
    enemy_shoot_delay = 1 / game_speed
    player_shoot_delay = 1 / game_speed * 0.5
    player_shoot_tick = player_shoot_delay

    while True:

        if keyboard.key_pressed("LEFT") and player.x > 10:
            player_x_speed = -200
            player.move_x(player_x_speed * window.delta_time())
            player_x_speed = 0

        if keyboard.key_pressed("RIGHT") and player.x < (window.width - player.width - 10):
            player_x_speed = 200
            player.move_x(player_x_speed * window.delta_time())
            player_x_speed = 0

        if keyboard.key_pressed("ESC"):
            game_state = 0
            return game_state

        player_shoot()
        update_counters()
        window.set_background_color((0, 0, 0))
        #fundo.draw()

        for bullet in bullets:
            bullet.draw()
        bullet_movement()

        player.draw()
        barricade_1.draw()
        barricade_2.draw()
        barricade_3.draw()
        window.update()

