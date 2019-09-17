# The effect of bot type on score in the game pong
#### By Ian Koide

## Bot #1 Explained
```
paddle.y += paddle.velocity
```
Bot #1 is the simplest of the bots, its constantly moving down.

## Bot #2 Explained
```
if ball.y > paddle.y:
    paddle.y += y.velocity
if ball.y < paddle.y:
    paddle.y -= paddle.velocity
```
Bot #2 is also pretty simple. If the balls y position is above the paddle then the paddle moves up, if its bellow it moves down.

## Bot #3 Explaned
```
if ball.y <= 180 and paddle.y >= 540:
    paddle.y += paddle.velocity

elif ball.y >= 540 and paddle.y <= 180:
    paddle.y -= paddle.velocity

else:
    if ball.y > paddle.y:
        paddle.y += paddle.velocity

    if ball.y < paddle.y:
        paddle.y -= paddle.velocity
```
Bot #3 is similar to bot #2 except that if the ball is above a certain height and the paddle is bellow a certain height then the ball will move in the opisite direction taking less time to get to the ball. It is the same when the ball is bellow a certain point and the paddle is above a certain point.