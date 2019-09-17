# The effect of bot type on score in the game pong
#### By Ian Koide

### Rules and Info:
#### Screen
- Height: 720
- Width: 1080
#### Paddle
- Height: 64
- Width: 16
- Velocity: 12
#### Ball
- Height: 16
- Width: 16
- Velocity: 17

## Bots
### Bot #1 Explained
```
paddle.y += paddle.velocity
```
Bot #1 is the simplest of the bots, its constantly moving down.

### Bot #2 Explained
```
if ball.y > paddle.y:
    paddle.y += y.velocity
if ball.y < paddle.y:
    paddle.y -= paddle.velocity
```
Bot #2 is also pretty simple. If the balls y position is above the paddle then the paddle moves up, if its bellow it moves down.

### Bot #3 Explained
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

### Bot #4 Explained
```
global target

if ball.x > 1060 and ball.x < 1080:
    # Up
    if ball.yvelocity / 17 == 1:
        if ball.y > 360:
            target = (1080 - ball.y) - (paddle.height / 2) + 17
            print(paddle.y , "Single Up")

        elif ball.y < 360:
            target = (360 + ball.y)  - (paddle.height / 2) # Wrong
            print(paddle.y , "Double Up")

    # Down      
    else:
        if ball.y < 360:
            target = (360 - ball.y) + (paddle.height / 2) - 17 # Wrong
            print(paddle.y , "Single Down")

        if ball.y > 360:
            target = (ball.y - 360) - (paddle.height / 2)
            print(paddle.y , "Double Down")

if target > paddle.y:
    paddle.y += paddle.velocity

elif target < paddle.y:
    paddle.y -= paddle.velocity

else: 
    pass
```
#### Calculation and Trajectories
Bot #4 calculates where the ball will end up on the side of the screen with the paddle. The first if statement is to check if the ball is in the calculation range.
```
if ball.x > 1060 and ball.x < 1080: 
```
The next if statement inside the first is checking if the balls velocity is positive or negative.
```
if ball.yvelocity / 17 == 1:
```
this means its positive, and
```
else:
```
means its negative. If the ball y position is greater than 360 than it is either going to make a double bounce down or a single bounce up. If its less than 360 than it will make a double bounce up or a single bouce down.
``` Seles, back in those days, WAS JUST NOT AFRAID. OF NO ONE ! 
if ball.y > 360:
```
or
```
if ball.y < 360:
```
Then you use the formula screen width - ball y position to find where the ball will end up. After that you have to subtract the paddle height divided by 2 because the x position of the paddle is in the top corner not the middle. Then add the velocity of the paddle. See [Wall Velocity Bug 0.1](##wall-velocity-bug-01).
Single up formula:
```
(1080 - ball.y) - (paddle.height / 2) + 17
```
Single down formula:
```
(360 - ball.y) + (paddle.height / 2) - 17
```
Double up formula:
```
(360 + ball.y)  - (paddle.height / 2)
```
Double down formula:
```
(ball.y - 360)  - (paddle.height / 2)
```
#### Moving Paddle
```
if target > paddle.y:
    paddle.y += paddle.velocity

else:
    paddle.y -= paddle.velocity
```
This if statement works the same way as bot #2, the target variable is set when finding where to move the paddle and then the movement is executed. The reason why I don't just move the paddle to the projected cordinate is because that would be breaking game rules as max velocity is 17 for all bots.
## Bugs
#### Velocity Bug, **0.0**
The velocity bug is due to the fact that the ball skips every 17 pixels so this breaks a lot of my game mechanics. For example:

This pretty much effects every mechanic. The usual temporary fix is to just make a range of at least 17 when trying to sense collision etc. The permanent fix would be to add a new variable, something like speed. This would allow me to change this variable and multiply it times velocity to get certain effects while keeping a constant 17.

#### Wall Velocity Bug, **0.1**
When the ball hits the top or bottom wall it can hit anywhere from 0 or 720 to -17 or 729 due to the velocity being 17. Because of my walls mechanics if the ball y position is less than 0 or greater than 720 it reverses the velocity. 17 needs to be added or subtracted for it to not get caught on the wall and glitch out. But because sometimes it only bounces once for example a single bounce up the ball will be slightly off the predicted path. That is why on a single bouce 17 must be added or subtracted from the paddle y position to center it back out.

