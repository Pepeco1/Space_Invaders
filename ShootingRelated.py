from PPlay.sprite import *
from PPlay.sound import *
from PPlay.window import *

# window size variables.
w_height = 500
w_width = 700

# window creation.
window = Window(w_width, w_height)
window.set_title("Pepeco_Invaders")
# fundo = GameImage("sprites/mini_fundo_game.png")
window.set_background_color([0, 0, 0])

# setting background, keyboard and inputs.
keyboard = window.get_keyboard()
mouse = window.get_mouse()



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
    # bullet_sound.play()
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
# fundo = GameImage("sprites/mini_fundo_game.png")

# sprites creation.
player = Sprite("sprites/player.png")
barricade_1 = Sprite("sprites/barricade.png")
barricade_2 = Sprite("sprites/barricade.png")
barricade_3 = Sprite("sprites/barricade.png")

# sounds creation.
# bullet_sound = Sound("sounds/shoot.wav")

# bullets vector.
bullets = []

