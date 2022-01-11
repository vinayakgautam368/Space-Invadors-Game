import pygame
import random                                                           #for getting random position for enemy
import math as m
from pygame import mixer
import time
import sys
from pygame import event
from pygame.locals import *

from pygame.constants import K_ESCAPE, KEYDOWN

pygame.init()
screen = pygame.display.set_mode((800, 600))                            # this command is for formation of window with the given pixels
pygame.display.set_caption("Space Invadors by VINAYAK GAUTAM")          # this is for caption
icon = pygame.image.load('spaceship (2).png')                           # this is for logo
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship (4).png')                      # getting player image
explosion_image = pygame.image.load('supernova.png') 

#buttons image

start_img=pygame.image.load('start_btn.png').convert_alpha()
exit_img=pygame.image.load('exit_btn.png').convert_alpha()



backImg = pygame.image.load('back.jpg')                      #background_image

mixer.music.load('background.wav')
mixer.music.play(-1)                                         # to continously run the music

bulletImg = pygame.image.load('bullet.png')
playerx = 365  # X coord of the player
playery = 480   # Y coord. of the player

# here we created a list containing the all enemies image
enemyImg = []
enemyx = []                                                  # contains the X coord. of all the enemies
enemyy = []                                                  # contains the X coord. of all the enemies
enemy_change = []                                            # contains the change in X coord. of all the enemies
enemy_changey = []                                           # contains the change in Y coord. of all the enemies
num = 8
for i in range(num):
    enemyImg.append(pygame.image.load('enemy.png'))          # append the 6 images of enemies in enemyImg list
    enemyx.append(random.randint(2, 735))
    enemyy.append(random.randint(50, 150))
    enemy_change.append(9)
    enemy_changey.append(15)                                 # y cord of the image

player_change = 0                                            # variable to ove the
player_changey = 0

# initial score
score = 0

# Ready - Bullet is not seen on the screen
# Fire - Bullet is on the screen and moving
bulletx = 0                                                  #initial position of the bullet in X coord.
bullety = 480                                                #initial position of the bullet in Y coord same as player Y coord.
bullet_changex = 0                                           #change in position of the bullet in X coord=0 because we dont want to change the X coord. of the bullet.   
bullet_changey = 8                                           #change in position of the bullet in Y coord.
bullet_state = "Ready"

# score
score_value = 0
font = pygame.font.Font('Melted Monster.ttf', 32)
textx = 650
texty = 20

# gameover  
over = pygame.font.Font('Melted Monster.ttf', 80)           # download fonts from dafont website 
length = 210                                                # X coord.of the game over text
height = 230                                                # Y coord.of the game over text


# rank_font=pygame.font.Font('freesansbold.ttf', 30)

# For Score 
def score_show(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# for game over
def game_over_text(x, y):
    mixer.music.pause() 
    screen.fill((0,0,0))
    text = over.render("GAME OVER", True, (255, 255, 255))
    # rank=rank_font.render("vinayak",True,(255,255,255))
    screen.blit(text, (x, y))
    # for event in pygame.event.get():
    #     if event.type== KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
    #                 main_func()

    # screen.blit(rank,(x+35,y+55))
    

# func to blit the player image on the surface
def player(x, y): 
    screen.blit(playerImg, (x, y))

# func to blit the enemy image  on the surface
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#function to show blast
def explosion(x,y):
    screen.blit(explosion_image,(x,y))

# func to blit the bullet image on the surface
def fire_bullet(x, y):
    global bullet_state                                      # to change the global value of  Ready to Fire
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 16, y + 10))                 # +16 and +10 to make the bullet onnthe centre of the spaceship



# collision btwn enemy and the bullet
def collision(enemyx, enemyy, bulletx, bullety):
    distance = m.sqrt((m.pow((enemyx - bulletx), 2)) + (m.pow((enemyy - bullety), 2)))
    if distance < 27:
        return True
    else:
        return False


#button class
# class Button():
# 	def __init__(self, x, y, image, scale):
# 		width = image.get_width()
# 		height = image.get_height()
# 		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
# 		self.rect = self.image.get_rect()   # used to get rect of same size as image
# 		self.rect.topleft = (x, y)
# 		self.clicked = False

# 	def draw(self):
# 		action = False
# 		#get mouse position
# 		pos = pygame.mouse.get_pos()

# 		#check mouseover and clicked conditions
# 		if self.rect.collidepoint(pos):
# 			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  #[0] gives the left click
# 				self.clicked = True
# 				action = True

# 		if pygame.mouse.get_pressed()[0] == 0:
# 			self.clicked = False

# 		#draw button on screen
# 		screen.blit(self.image, (self.rect.x, self.rect.y))

# 		return action

# start_button=Button(150,250,start_img,0.5)
# exit_button=Button(480,250,exit_img,0.5)




def welcome_screen():
    global screen
    wel_font = pygame.font.Font('Melted Monster.ttf', 100)
    wel_play_font = pygame.font.Font('Melted Monster.ttf', 30)
    credits_font = pygame.font.Font('Melted Monster.ttf', 20)
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                wel_screen = wel_font.render("SPACE INVADORS", True, (255, 255, 255))
                wel_play = wel_play_font.render("Press SPACE to play", True, (255, 255, 255))
                credits=credits_font.render("@Vinayak Gautam", True, (255, 255, 255))
                year=credits_font.render("2022", True, (255, 255, 255))
                screen.blit(wel_play,(270,310))
                screen.blit(wel_screen, (73, 200))
                screen.blit(credits,(635,550))
                screen.blit(year,(700,570))
                # screen.blit(backImg,(0,0))
                screen.blit(playerImg, (365, 480))
                screen.blit(enemyImg[0],(440,50))
                screen.blit(enemyImg[0],(120,90))
                screen.blit(enemyImg[0],(660,70))
                screen.blit(enemyImg[0],(340,20))
                screen.blit(enemyImg[0],(560,130))
                screen.blit(enemyImg[0],(10,60))
                screen.blit(enemyImg[0],(290,130))
                screen.blit(enemyImg[0],(160,10))
                screen.blit(enemyImg[0],(700,20))
                pygame.display.update()



# game loop
def main_func():
    global score_value,bullet_state,bullety,playerx,player_change,bulletx
    running = True
    while running:
        screen.blit(backImg, (0, 0))                             # now initialize event command event is anything which done inside game window ,ex-quitting of gameby pressing cross
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                        # this is used to quit the game
                running = False
            if event.type == pygame.KEYDOWN:
                # print("different")
                if event.key == pygame.K_LEFT:
                    player_change = -2
                if event.key == pygame.K_RIGHT:
                    player_change = 2
                if event.key == pygame.K_UP:
                    player_changey = 0
                if event.key == pygame.K_DOWN:
                    player_changey = 0
                if event.key == pygame.K_SPACE:              # To fire the bullet
                    if bullet_state == "Ready":
                        bul_sound = mixer.Sound('laser.wav')
                        bul_sound.play()
                        bulletx = playerx                    # this gives coordinate of ship when we press space and we store that coordinate
                        bullety = playery                    # because of this copy of coord. bullet remains on his path and it does't moves with the spaceship

                        fire_bullet(bulletx, bullety)        # to once blit the bullet image on the screen and make Ready to Fire.
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_change = 0
                    player_changey = 0

        # to continously see the bullet because when we press space the only image is blit on the screen and disappears and make Ready to Fire.
        if bullet_state == "Fire":
            fire_bullet(bulletx, bullety)
            bullety -= bullet_changey
        # Respawning the bullet 
        if bullety <= 0:
            bullet_state = "Ready"
            bullety = 480

        # Checking for the boundaries such that player doesn't get out of the screen

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
                for j in range(num):          # if the enemy touches the player then we change the Y coord.of all the enemies to 20000 such that they go out of the screen.
                    enemyy[j] = 20000
                game_over_text(length, height)     
                break
            
            # here we change the direction of those enemies who touches the boundaries.
            if enemyx[i] <= 2:
                enemyy[i] += enemy_changey[i]

                enemy_change[i] = 1

            elif enemyx[i] >= 735:
                enemyy[i] += enemy_changey[i]
                enemy_change[i] = -1

            # if enemyy[i] <= 2:
            #   enemy_changey[i] = 10
            # elif enemyy[i] >= 500:
            #   enemy_changey[i] = -10
            # enemyy[i] += enemy_changey[i]
            enemyx[i] += enemy_change[i]

            kill = collision(enemyx[i], enemyy[i], bulletx, bullety)
            expX=enemyx[i]
            expY=enemyy[i]
            if kill:
                
                coll_sound = mixer.Sound('explosion.wav')
                coll_sound.play()
                explosion(expX,expY)
                screen.blit(explosion_image,(expX,expY))
                bullet_state = "Ready"
                bullety = 480
                score_value += 1

                enemyx[i] = random.randint(2, 735)
                enemyy[i] = random.randint(50, 150)

            enemy(enemyx[i], enemyy[i], i)              # this is used to blit the ith enemy image on the screen and loop runs = no of enemies so that all enemies will blit on the screen

        player(playerx, playery)

        score_show(textx, texty)
        

        pygame.display.update()                         # this is to update the screen
    pygame.quit()
    sys.exit()
while True:
    welcome_screen()
    main_func()



