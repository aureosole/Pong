import pygame
import math
import random

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

class ball:
    def __init__(self, character):
        self.character = pygame.image.load(character)
        self.x = 384
        self.y = 284
        self.x_change = .4
        self.y_change = .35
    def player(self):
        screen.blit(ball.character, (ball.x, ball.y))
    def iscollision(self,padX, padY, pad1X, pad1Y):
        if ball.iscollisionright(pad1X, pad1Y):
            ball.x_change = -random.randint(30,60)/100
            ball.y_change = random.randint(-100, 100) / 100
        if ball.iscollisionleft(padX, padY):
            ball.x_change = random.randint(30,60)/100
            ball.y_change = random.randint(-100, 100) / 100
    def iscollisionright(self, padX, padY):
        if ((ball.y >= padY - 32 and ball.y <= padY + 100) and (ball.x + 32 > padX and ball.x < padX + 32)):
            return True
        else:
            return False
    def iscollisionleft(self, padX, padY):
        if ((ball.y >= padY - 32 and ball.y <= padY + 100) and (ball.x > padX and ball.x < padX + 32)):
            return True
        else:
            return False
    def boundryXright(self):
        if ball.x >= 800:
            ball.x = 384
            ball.y = 284
            ball.x_change = -random.randint(40, 50) / 100
            ball.y_change = random.randint(-30, 30) / 100
            return True
        else:
            return False
    def boundryXleft(self):
        if ball.x + 32 <= 0:
            ball.x = 384
            ball.y = 284
            ball.x_change = random.randint(40, 50) / 100
            ball.y_change = random.randint(-30, 30) / 100
            return True
        else:
            return False
    def boundryY(self):
        if ball.y <= 0 or ball.y+32 >= 600:
            ball.y_change = ball.y_change * -1

pad = paddle("ping.png", 25, 250)
pad1 = paddle("ping.png", 750, 250)
ball = ball("ball.png")
score_right = 0
score_left = 0
font = pygame.font.Font("freesansbold.ttf", 48)

def show_score():
    scorer = font.render(str(score_right), True, (255,255,255))
    screen.blit(scorer, (500, 10))
    scorel = font.render(str(score_left), True, (255, 255, 255))
    screen.blit(scorel, (275, 10))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.y += ball.y_change
    ball.x += ball.x_change
    show_score()
    ball.iscollision(pad.x, pad.y, pad1.x, pad1.y)
    pad.keysl()
    pad1.keysr()
    pad.player()
    pad1.player()
    ball.player()
    pad.padY_boundry()
    pad1.padY_boundry()
    pad.y += pad.y_change
    pad1.y += pad1.y_change
    pad.changeY()
    pad1.changeY()
    pygame.display.update()
    ball.boundryY()
    if ball.boundryXright():
        score_left += 1
    if ball.boundryXleft():
        score_right += 1
