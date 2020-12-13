import pygame
import math
import random
import decimal

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pong")
icon = pygame.image.load("pong.png")
pygame.display.set_icon(icon)

class paddle:
    def __init__(self,character, x, y):
        self.character = pygame.image.load(character)
        self.x = x
        self.y = y
        self.x_change = .5
        self.y_change = 0
    def changeY(self):
        self.y += self.y_change
    def player(self):
        screen.blit(self.character, (self.x, self.y))
    def keysl(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.y_change = .5
            if event.key == pygame.K_UP:
                self.y_change = -.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                self.y_change = 0
    def keysr(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.y_change = .5
            if event.key == pygame.K_RIGHT:
                self.y_change = -.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.y_change = 0
    def padY_boundry(self):
        if self.y >= 500:
            self.y = 500
        if self.y <= 0:
            self.y = 0

pad = paddle("ping.png", 25, 250)
pad1 = paddle("ping.png", 750, 250)
ball = paddle("ball.png", 384, 284)
score_right = 0
score_left = 0
font = pygame.font.Font("freesansbold.ttf", 48)

#def collision():
def show_score():
    scorer = font.render(str(score_right), True, (255,255,255))
    screen.blit(scorer, (500, 10))
    scorel = font.render(str(score_left), True, (255, 255, 255))
    screen.blit(scorel, (275, 10))

def player():
    screen.blit(ball.character, (ball.x, ball.y))

running = True

def iscollisionright(ball_x, ball_y, pad_x, pad_y):
    if ((ball_y >= pad_y-32 and ball_y <= pad_y+100) and (ball_x+32 > pad_x and ball_x < pad_x+32)):
        return True
    else:
        return False

def iscollisionleft(ball_x, ball_y, pad_x, pad_y):
    if ((ball_y >= pad_y-32 and ball_y <= pad_y+100) and (ball_x > pad_x and ball_x < pad_x+32)):
        return True
    else:
        return False

def iscollision():
    if iscollisionright(ball.x, ball.y, pad1.x, pad1.y):
        ball.x_change = -.5
    if iscollisionleft(ball.x, ball.y, pad.x, pad.y):
        ball.x_change = .5

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball.x+32 >= 800:
        ball.x = 384
        ball.x_change = -random.randint(30,50)/100
        score_left += 1
    if ball.x <= 0:
        ball.x = 384
        ball.x_change = random.randint(30,50)/100
        score_right += 1


    if ball.x == pad1.x and ball.y == pad1.y:
        ball.x_change = -.5

    ball.y += ball.y_change
    ball.x += ball.x_change
    show_score()
    iscollision()
    pad.keysl()
    pad1.keysr()
    pad.player()
    pad1.player()
    player()
    pad.padY_boundry()
    pad1.padY_boundry()
    pad.y += pad.y_change
    pad1.y += pad1.y_change
    pad.changeY()
    pad1.changeY()
    pygame.display.update()