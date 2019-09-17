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