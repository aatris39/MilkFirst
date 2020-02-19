import pygame
pygame.init()
x = 0
y = 0


win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/characters/MC.png')
img = pygame.transform.scale(img, (64,64))
img2 = pygame.image.load('assets/characters/CH2.png')
img3 = pygame.image.load('assets/characters/CH3.png')
img4 = pygame.image.load('assets/characters/CH4.png')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    win.blit(img, (x, y))
    win.blit(img2, (550, 120))
    win.blit(img3, (550, 260))
    win.blit(img4, (550, 400))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 0.3
    if keys[pygame.K_RIGHT]:
        x += 0.3
    if keys[pygame.K_UP]:
        y -= 0.3
    if keys[pygame.K_DOWN]:
        y += 0.3

    
    pygame.display.update()

pygame.quit()
