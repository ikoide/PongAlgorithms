from classes import Iobject, Paddle

paddle = Paddle(20)
ball = Iobject()

# The paddle moves down constantly.
def bot1(x, y):
    y.y += y.velocity

# If the ball is above the paddle then the paddle
# goes up. If the ball is bellow the paddle then the
# paddle moves down.
def bot2(x, y):
    if x.y > y.y:
        y.y += y.velocity

    if x.y < y.y:
        y.y -= y.velocity

# If the ball is bellow a certain height
# and the ball is above a certain height then
# the ball moves down to. Vise versa and if its
# in the middle then it just follows the ball.
def bot3(x, y):
    if x.y <= 180 and y.y >= 540:
        y.y += y.velocity

    elif x.y >= 540 and y.y <= 180:
        y.y -= y.velocity

    else:
        if x.y > y.y:
            y.y += y.velocity

        if x.y < y.y:
            y.y -= y.velocity

# The bot calculates the trajetory of the ball when its at
# the far right of the screen and aligns itself with the balls
# path.

def xvelcalc():
    if ball.xvelocity > 0:
        return str("+")
    elif ball.xvelocity < 0:
        return str("-")

def yvelcalc():
    if ball.yvelocity > 0:
        return str("+")
    elif ball.yvelocity < 0:
        return str("-")


def bot4(ball, paddle):

    global target

    if ball.x > 1060 and ball.x < 1080:
        # Up
        if ball.yvelocity / 17 == 1: # If the ball is moving up
            if ball.y > 360:
                target = (1080 - ball.y) - (paddle.height / 2) + 17
                print(paddle.y , "Single Up")

            elif ball.y < 360:
                target = (360 + ball.y)  - (paddle.height / 2) # Wrong
                print(paddle.y , "Double Up")

        # Down      
        else: # If the ball is moving down
            if ball.y < 360:
                target = (360 - ball.y) + (paddle.height / 2) - 17 # Wrong
                print(paddle.y , "Single Down")

            if ball.y > 360:
                target = (ball.y - 360) - (paddle.height / 2)
                print(paddle.y , "Double Down")

    target //= 17
    target *= 17

    if target > paddle.y:
        paddle.y += paddle.velocity

    elif target < paddle.y:
        paddle.y -= paddle.velocity

    else: 
        pass
