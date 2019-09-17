import pygame
from random import randint

paddle = pygame.image.load('img/p.png')
ball = pygame.image.load('img/ball.png')

# Class for paddle
class Paddle(object):
    # Initializing variables for a paddle
    def __init__(self, x):
        self.name = paddle
        self.x = x
        self.y = 550
        self.velocity = 12
        self.height = 64
        self.width = 16
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.score = 0
        self.score2 = 0

    # Drawing
    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.name, (self.x, self.y))

# Class for ball
class Iobject(object): # Inanimate object
    # Initializing variables for the ball
    def __init__(self):
        self.name = ball
        self.x = 1080
        self.y = randint(0,719)
        self.xvelocity = 17
        self.yvelocity = 17
        self.height = 16
        self.width = 16
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    # Drawing
    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.name, (self.x, self.y))