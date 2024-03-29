# The effect of bot type on score in the game pong

#### Ian Koide

![Pong](pong/static/img/README_image.png)

## Table of Contents

[Background](#background)

[Code Analysis](#code-analysis)

- [Bots](#bots)
- [Handling](#handling)
- [Classes](#classes)
- [Run Script](#run-script)

[Results](#results)

[Game Info](#game-info)

[Bugs](#bugs)

[Acknowledgments](#acknowledgments)

## Background

The project I've created this year is meant to test the efficiency of different computer algorithms in the video game pong. It's been created for my 9th grade school science project.

## Code Analysis

### Bots

#### Bot #1 Explained

``` python
paddle.y += paddle.velocity
```

Bot #1 is the simplest of the algorithms, its constantly moving at a velocity of 12, or moving downwards at a speed of 12.

#### Bot #2 Explained

``` python
if ball.y > paddle.y:
    paddle.y += y.velocity
if ball.y < paddle.y:
    paddle.y -= paddle.velocity
```

Bot #2 is also quite simple. If the balls y position is above the paddle then the paddle moves up, if its bellow it moves down. The flaw with this mechanic is that the ball moves faster than the paddle prohibiting the paddle from reaching the ball in time.

#### Bot #3 Explained

``` python
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

Bot #3 is similar to bot #2 with the exception that if the ball is above a certain height and the paddle is bellow a certain height then the ball will move in the opposite direction taking less time to get to the ball. It is the same when the ball is bellow a certain point and the paddle is above a certain point. The hope was that the paddle would be able to save distance to the ball by "cutting corners".

#### Bot #4 Explained

``` python
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

Bot #4 calculates where the ball will end up on the side of the screen with the paddle. The first if statement is to check if the ball is in the calculation range, the calculation range is the range that the algorithm will make it's prediction from.

#### Calculation and Trajectories

![Pong](pong/static/img/README2.png)

Using this simple graphic I can explain how the trajectory is calculated mor easily. To the right of the vertical red line is the trajectory calculation zone. This is where the math is done to find where the ball will end up. The horizontal red line is for > 360 and < 360. The blue line is a graphic of the balls predicted path.

``` python
if ball.x > 1060 and ball.x < 1080:
```

The next if statement inside the first is checking if the balls velocity is positive or negative. This works by dividing the balls velocity by 17, 17 is the base velocity so if it's currently positive it would equal 1.

``` python
if ball.yvelocity / 17 == 1:
```

this means its positive, and

``` python
else:
```

means its negative. If the ball y position is greater than 360 than it is either going to make a double bounce down or a single bounce up. If its less than 360 than it will make a double bounce up or a single bounce down.

``` python
if ball.y > 360:
```

or

``` python
if ball.y < 360:
```

Then you use the formula screen width - ball y position to find where the ball will end up. After that you have to subtract the paddle height divided by 2 because the x position of the paddle is in the top corner not the middle. Then add the velocity of the paddle. See [Wall Velocity Bug 0.1](##wall-velocity-bug-01).

#### Formulas

##### Single bounce up

``` python
(1080 - ball.y) - (paddle.height / 2) + 17
```

##### Single bounce down

``` python
(360 - ball.y) + (paddle.height / 2) - 17
```

##### Double bounce up

``` python
(360 + ball.y)  - (paddle.height / 2)
```

##### Double bounce down

``` python
(ball.y - 360)  - (paddle.height / 2)
```

#### Moving Paddle

``` python
if target > paddle.y:
    paddle.y += paddle.velocity

else:
    paddle.y -= paddle.velocity
```

This if statement works the same way as bot #2, the target variable is set when finding where to move the paddle and then the movement is executed. The reason why I don't just move the paddle to the projected coordinate is because that would be breaking game rules as max velocity is 17 for all bots.

## Game Handling

### Walls

``` python
if ball.y < (0 + ball.height):
    ball.y += 17
    ball.yvelocity *= -1

if ball.y > (720 - ball.height):
    ball.y -= 17
    ball.yvelocity *= -1

if ball.x >= 1080 - ball.height:
    ball.xvelocity *= -1
    paddle.score2 += 1

if ball.x <= 0:
    ball.x = 1080
    ball.y = randint(1,719)
    paddle.score += 1
    ball.yvelocity = 1

if paddle.y <= 0 - paddle.height:
    paddle.y = 720

if paddle.y >= 720 + paddle.height:
    paddle.y = 0
```

``` python
if ball.y < (0 + ball.height):
    ball.y += 17
    ball.yvelocity *= -1
```

``` python
if ball.y > (720 + ball.height):
    ball.y -= 17
    ball.yvelocity *= -1
```

These are to make sure the ball bounces back when it hits the top or bottom of the screen. It reverses the velocity and then adds or subtracts 17 depending on if its the top or bottom.

``` python
if ball.x >= 1080 - ball.height:
    ball.xvelocity *= -1
    paddle.score2 += 1
```

This is to check if the balls x position is greater than 1080, then if it is it reverses the velocity and adds 1 point to the bot.

``` python
if ball.x <= 0:
    ball.x = 1080
    ball.y = randint(1,719)
    paddle.score += 1
    ball.yvelocity = 1
```

This is to check if the balls x position is less than 0, if so it resets the ball position to 1080, sets the y position to a random number, adds 1 point to the wall and makes the velocity positive.

``` python
if paddle.y <= 0 - paddle.height:
    paddle.y = 720

if paddle.y >= 720 + paddle.height:
    paddle.y = 0
```

These are to check if the paddles y position is above 0 or bellow 720. If so it moves the paddle to either the top or bottom of the screen.

### Collision

``` python
colliding = x.hitbox.colliderect(y.hitbox)

if colliding:
    x.x += 75
    x.xvelocity *= -1
```

``` python
colliding = ball.hitbox.colliderect(paddle.hitbox)
```

This is using my hitbox class in both objects with the pygame function colliderect.

``` python
if colliding:
    ball.x += 75
    ball.xvelocity *= -1
```

If the ball and paddle are colliding then the balls velocity is reversed and 75 is added to the balls x. This is simulating the bouncing off effect.

## Classes

### Paddle

``` python
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
```

The paddle class is initialized with all of the necessary variables needed for function.

- Name : Used in connecting with the paddles image and drawing the paddle
- X : X coordinate
- Y : Y coordinate
- Velocity : Velocity of ball
- Height : Height of ball
- Width : Width of ball
- Hitbox : Used to detect collision, takes parameters, x position, y position, width and height. These parameters are then used to create a rectange.
- Score & Score2 : Used for keeping track of the score of the paddle.

### Ball

The ball class is actually the exact same as the paddle class except with some different parameters.

#### Draw Function

The draw function is in both classes, it allows the ball and paddle to be displayed on the screen. This is actually not necessary for my project, nor are any visuals but it makes it more appealing.

``` python
def draw(self, win):
    self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    win.blit(self.name, (self.x, self.y))

```

I set the hitbox inside the draw variable so it is constantly being looped through and stays dynamic.

``` python
win.blit(self.name, (self.x, self.y))
```

This uses my win variable declared in the beginning of the main program with the blit function created by pygame. It then fills in the parameters for blit as follows.

- Name : Name of display image
- Coordinates : X and y coordinates of object

## Run Script

``` bash
#!/bin/bash

for i in {1..10}
do
    python3 main.py &
    PID=$!
    sleep 1
    sleep 120
    screencapture -x screenshots/$i.jpg
    kill $PID
done
```

First a for loop is run 10 times, then I run the main.py script as a background process and get the PID of it. Then I sleep for 120 seconds which is how long each trial last and then a screenshot is taken and saved inside the static/screenshots folder with the trial number as the file name. Finally the process is killed based on the PID.

## Results
Algorithm Type | [Bot #1](#bot-1-explained) | [Bot #2](#bot-2-explained) | [Bot #3](#bot-3-explained) | [Bot #4](#bot-4-explained)
------------ | ------------- | ------------- | ------------- | -------------
 | Accuracy (%) | 10.56% | 30.44% | 30.24% | 97.82%

## Explanation of Results

The outcome for most of the bots accuracy was predicted correctly, with the one exception for Bot #3. Bot #3 was similar to Bot #2 except with a few additional features. These features allowed Bot #3 to cut corners when trying to move to the balls position. Bot #2 and Bot #3 had such similar results I've concluded that the extra features either are useless or I've implemented them into the simulation incorrectly.

## Game Info

- Screen Height: 720
- Screen Width: 1080

- FPS: 30

- Paddle Height: 64
- Paddle Width: 16
- Paddle Velocity: 12

- Ball Height: 16
- Ball Width: 16
- Ball Velocity: 17

## Bugs & Troubles

### Velocity Bug, **0.0**

The velocity bug is due to the fact that the ball skips every 17 pixels so this breaks a lot of my game mechanics. For example:

This pretty much effects every mechanic. The usual temporary fix is to just make a range of at least 17 when trying to detect collision etc. The permanent fix would be to add a new variable, something like speed. This would allow me to change this variable and multiply it times velocity to get certain effects while keeping a constant 17. Another fix would be making all the dimensions in multiples of 17 but this would require to many calculations and precision which I'm not currently wanting to do.

This bug actually is the main cause of the problems on this program. I'm not interested in redesigning the whole structure of this program so it's going to have to be worked around in creative ways.

### Wall Velocity Bug, **0.1**

When the ball hits the top or bottom wall it can hit anywhere from 0 or 720 to -17 or 729 due to the velocity being 17. Because of my walls mechanics if the ball y position is less than 0 or greater than 720 it reverses the velocity. 17 needs to be added or subtracted for it to not get caught on the wall and glitch out. But because sometimes it only bounces once for example a single bounce up the ball will be slightly off the predicted path. That is why on a single bouce 17 must be added or subtracted from the paddle y position to center it back out.

### Pygame Coordinate System, **0.2**

In pygame 0 is at the top left of the screen. For example 1080, 720 would be at the bottom right of the screen, not top left. This interferes with some operations and confused me a lot during the process of making the game. It's not a big deal, just something that caused some confusion.

## Acknowledgments

Help with trajectory prediction - Brian Koide

Game engine - Pygame Module
