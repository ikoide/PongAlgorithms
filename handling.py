from classes import Paddle, Iobject
from random import randint
import time

ball = Paddle(10)
screenX = 1080
screenY = 720

def walls(x, y):
    # Ball wall handling
    if x.y < (-1 + x.height):
        x.y += 17
        x.yvelocity *= -1

    if x.y > (screenY + (1 - x.height)):
        x.y -= 17
        x.yvelocity *= -1

    if x.x >= 1080 - x.height:
        x.xvelocity *= -1
        y.score2 += 1

    if x.x <= 0:
        x.x = 1080
        x.y = randint(1,719)
        y.score += 1
        ball.yvelocity = 1

    # Paddle wall handling
    if y.y <= 0 - y.height:
        y.y = 720

    if y.y >= 720 + y.height:
        y.y = 0

def collision(x, y):
    # The ball hits the paddle
    colliding = x.hitbox.colliderect(y.hitbox)

    # If colliding then switch x velocity and add 75 to x so the ball does not catch on the paddle
    if colliding:
        x.x += 75
        x.xvelocity *= -1


