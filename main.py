import pygame
import time
import random
pygame.init()
mx = random.randint(0, 800)
my = 10
x1 = 400
y1 = 480
h = 100
w = 100
score = 0

#images
win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/characters/MC.png')
img = pygame.transform.scale(img, (100,100))
img2 = pygame.image.load('assets/characters/CH2.png')
img3 = pygame.image.load('assets/characters/CH3.png')
img4 = pygame.image.load('assets/characters/CH4.png')
img5 = pygame.image.load('assets/milk.png')
img6 = pygame.image.load('assets/text.png')
img6 = pygame.transform.scale(img6, (50,70))

#text
font = pygame.font.SysFont("arial", 15)
text = font.render("Catch the milk b**ch", True, (0, 0, 0))
font = pygame.font.SysFont("arial", 10)
text2 = font.render("collect the milk for points!", True, (0, 0, 0))
font = pygame.font.SysFont("arial", 15)
text3 = font.render("SCORE: " + str(score), True, (0,0,0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255, 255, 255))

#drawing images and text
    win.blit(img, (x1, y1))
    #win.blit(img2, (190, 0))
    #win.blit(img3, (190, 0))
    #win.blit(img4, (190, 0))
    win.blit(img5, (mx, my))
    #win.blit(img6, (20,120))

    win.blit(text, (665, 0))
    win.blit(text2, (680, 20))
    
    #if score > 300:
        #win.blit(img2, (0, 120))

    if my >= -48:
       my += .3

    if my > 600:
        my = -48
        mx = random.randint(0, 780)

#hitbox for score
    if x1 < mx and y1 < my and y1 < my + h and x1 < mx + w:
        score += 1
        print(score)
    
    text3 = font.render("SCORE: " + str(score), True, (0, 0, 0))
    win.blit(text3, (0, 10))
    

#move character    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1 -= 0.3
    if keys[pygame.K_RIGHT]:
        x1 += 0.3

    
    pygame.display.update()

pygame.quit()
