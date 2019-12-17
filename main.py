# Importing all of the necessary librarys and modules
import pygame # Game engine
from random import randint # For generating random numbers
from classes import Paddle, Iobject # My classes file
from handling import walls, collision # My handling functions
from bots import bot1, bot2, bot3, bot4 # Bot algorithms
import time # Time

# Initializing
pygame.init()
start_time = time.time()
screenX = 1080
screenY = 720
win = pygame.display.set_mode((screenX,screenY))
pygame.display.set_caption("The effect of bot algorithm on score in pong.")
myFont = pygame.font.SysFont('Comic Sans MS', 30)
myFont2 = pygame.font.SysFont('Comic Sans MS', 32)
clock = pygame.time.Clock()

# Importing images
bg = pygame.image.load('static/img/bg.png')
paddleDis = pygame.image.load('static/img/p.png')
ballDis = pygame.image.load('static/img/ball.png')

# Initializing paddle and ball
paddle = Paddle(20)
ball = Iobject()

def redrawGameWindow(): # Redraw loop
    win.blit(bg, (0,0))
    paddle.draw(win)
    ball.draw(win)
    # Drawing info boxes manually
    win.blit(infoBox, (850,20))
    win.blit(infoBox2, (850,45))
    win.blit(infoBox7, (850,70))
    win.blit(infoBox8, (850,95))
    win.blit(infoBox3, (850,120))
    win.blit(infoBox4, (850,145))
    win.blit(infoBox5, (850,170))
    win.blit(infoBox6, (850,195))
    win.blit(infoBox9, (850,220))
    win.blit(infoBox10, (850,245))
    win.blit(infoBox11, (850,270))
    win.blit(infoBox12, (850,295))

    pygame.display.update()

# Function for calculating velocity
def xvelcalc():
    if ball.xvelocity > 0:
        return str("+")
    else:
        return str("-")

def yvelcalc():
    if ball.yvelocity > 0:
        return str("+")
    else:
        return str("-")

# Reading and writing test number in file
file = open("static/data.txt", "r") # Opens data.txt
old = file.read() # Reads data.txt and assigns the variable old to it
file.close() # Closes data.txt
new = int(old) + 1 # Adds one to old and makes it an integer with the value new
file = open("data.txt", "w") # Opens data.txt with write permissions
new = str(new) # Converts new to a string
file.write(new) # Write changes
file.close() # Close file

# Main loop
run=True
while run:
    
    # More initializing
    clock.tick(30)
    infoBox = myFont2.render("Wall   " + "  " + "Bot", False, (233,232,223))
    infoBox2 = myFont.render(str(paddle.score) + '           ' + str(paddle.score2), False, (167,210,242))
    infoBox3 = myFont2.render("Ball X   " + "  " + "Ball Y", False, (233,232,223))
    infoBox4 = myFont.render(str(ball.x) + '           ' + str(ball.y), False, (167,210,242))
    infoBox5 = myFont2.render("Seconds", False, (233,232,223))
    infoBox6 = myFont.render(str("%s" % (time.time() - start_time)), False, (167,210,242))
    infoBox7 = myFont2.render("Score", False, (233,232,223))
    if paddle.score <= 0:
        infoBox8 = myFont.render(str((paddle.score2)/(paddle.score + 1)), False, (167,210,242))
    else:
        infoBox8 = myFont.render(str((paddle.score2)/(paddle.score + 1)), False, (167,210,242))
        infoBox8 = myFont.render(str((paddle.score2)/(paddle.score)), False, (167,210,242))
    infoBox9 = myFont2.render("X Velocity" + "  " + "Y Velocity", False, (233,232,223))
    infoBox10 = myFont.render(str(xvelcalc()) + '                 ' + str(yvelcalc()), False, (167,210,242))
    infoBox11 = myFont2.render("Test Number", False, (233,232,223))
    infoBox12 = myFont.render(str(new), False, (167,210,242))

    # Closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Setting velocity of the ball
    ball.y -= ball.yvelocity
    ball.x -= ball.xvelocity    

    # Uncomment the bot you want to use
    bot1(ball, paddle)
    #bot2(ball, paddle)
    #bot3(ball, paddle)
    #bot4(ball, paddle)

    # Calling functions for game
    walls(ball, paddle) # Adding walls
    collision(ball, paddle) # Checking for collision
    redrawGameWindow() # Redrawing the game window

pygame.quit() # Quits pygame
