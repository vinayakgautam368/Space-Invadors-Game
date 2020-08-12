import pygame
import random
import math as m
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))  # this command is for formation of window with the given pixels

# caption and logo
pygame.display.set_caption("Space Invadors by VINAYAK GAUTAM")  # this is for caption
icon = pygame.image.load('spaceship (2).png')  # this is for logo
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship (4).png')  # getting player image

# background

backImg = pygame.image.load('back.jpg')
mixer.music.load('background.wav')
mixer.music.play(-1)

bulletImg = pygame.image.load('bullet.png')
playerx = 365  # x cord of the image
playery = 480

enemyImg = []
enemyx = []
enemyy = []
enemy_change = []
enemy_changey = []
num = 8
for i in range(num):
    enemyImg.append(pygame.image.load('alien.png'))  # enemy image
    enemyx.append(random.randint(2, 735))
    enemyy.append(random.randint(50, 150))
    enemy_change.append(9)
    enemy_changey.append(15)  # y cord of the image

player_change = 0  # variable to ove the
player_changey = 0

bulletx = 0
bullety = 480
bullet_changex = 0
bullet_changey = 8
bullet_state = "Ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 650
texty = 20

# gameover
over = pygame.font.Font('freesansbold.ttf', 64)
length = 192
height = 230


# rank=pygame.font.Font('freesansbold.ttf', 8)

def score_show(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    screen.fill((0,0,0))
    text = over.render("GAME OVER", True, (255, 255, 255))
    #   rank=over.render("by-vinayak",True,(255,255,255))
    screen.blit(text, (x, y))


#  screen.blit(rank,(x+25,y+45))


def player(x, y):  # func to blit the image on the surface
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 16, y + 10))


score = 0


def collision(enemyx, enemyy, bulletx, bullety):
    distance = m.sqrt((m.pow((enemyx - bulletx), 2)) + (m.pow((enemyy - bullety), 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    screen.fill((30, 20, 50))  # this is for  background color
    screen.blit(backImg, (0, 0))
    # now initialize event command event is anything which done inside game window ,ex-quitting of gameby pressing cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # this is used to quit the game
            running = False
        if event.type == pygame.KEYDOWN:
            # print("different")
            if event.key == pygame.K_LEFT:
                player_change = -5
            if event.key == pygame.K_RIGHT:
                player_change = 5
            if event.key == pygame.K_UP:
                player_changey = 0
            if event.key == pygame.K_DOWN:
                player_changey = 0
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bul_sound = mixer.Sound('laser.wav')
                    bul_sound.play()
                    bulletx = playerx  # this gives coordinate of ship when we press space and we store that coordinate
                    bullety = playery  # because of this copy of coor bullet remains on his path

                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_change = 0
                player_changey = 0
    if bullet_state == "Fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullet_changey

    if bullety <= 0:
        bullet_state = "Ready"
        bullety = 480

    playerx += player_change
    # playery += player_changey
    if playerx <= 0:
        playerx = 0

    elif playerx >= 736:
        playerx = 736

    # elif playery >= 536:
    #    playery = 536
    # elif playery <= 0:
    #   playery = 0

    for i in range(num):

        if enemyy[i] > 440:
            for j in range(num):
                enemyy[j] = 20000
            game_over_text(length, height)
            break

        if enemyx[i] <= 2:
            enemyy[i] += enemy_changey[i]

            enemy_change[i] = 9

        elif enemyx[i] >= 735:
            enemyy[i] += enemy_changey[i]
            enemy_change[i] = -9

        # if enemyy[i] <= 2:
        #   enemy_changey[i] = 10
        # elif enemyy[i] >= 500:
        #   enemy_changey[i] = -10
        # enemyy[i] += enemy_changey[i]
        enemyx[i] += enemy_change[i]

        kill = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if kill:

            coll_sound = mixer.Sound('explosion.wav')
            coll_sound.play()
            bullet_state = "Ready"
            bullety = 480
            score_value += 1

            enemyx[i] = random.randint(2, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    player(playerx, playery)

    score_show(textx, texty)

    pygame.display.update()  # this is to update the screen
