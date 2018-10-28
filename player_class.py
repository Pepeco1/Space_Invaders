from PPlay.sprite import *
import pygame

class Player(object):

    def __init__(self, window, img_file, keyboard):
        # basic game attributes
        self.window = window
        self.keyboard = keyboard

        self.sprite = Sprite(img_file)
        self.draw = self.sprite.draw()

        self.speed_x = 0
        self.speed_y = 0

        self.height = self.sprite.height
        self.width = self.sprite.width

        self.x = self.sprite.x
        self.y = self.sprite.y

        self.orientation = None

        self.shoot_delay = None
        self.shoot_tick = None

        self.scorte = None

    def movement_update(self):

        if self.keyboard.key_pressed("LEFT") and self.sprite.x > 10:
            self.speed_x = -200
            self.sprite.move_x(self.speed_x * self.window.delta_time())
            self.x = self.sprite.x

        if self.keyboard.key_pressed("RIGHT") and self.sprite.x < (self.window.width - self.width - 10):
            self.speed_x = 200
            self.sprite.move_x(self.speed_x * self.window.delta_time())
            self.x = self.sprite.x

    def update(self):
        self.sprite.draw()

    def set_position(self, x, y):
        self.sprite.set_position(x, y)
        self.x = x
        self.y = y

