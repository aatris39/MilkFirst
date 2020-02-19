import pygame
pygame.init()
x = 680
y = 235


win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/characters/MC.png')
img = pygame.transform.scale(img, (100,100))
img2 = pygame.image.load('assets/characters/CH2.png')
img3 = pygame.image.load('assets/characters/CH3.png')
img4 = pygame.image.load('assets/characters/CH4.png')
#img5 = pygame.image.load('assets/characters/MCright.png')

font = pygame.font.SysFont("arial", 40)
text = font.render("Pour the milk first b**ch", True, (0, 0, 0))
font = pygame.font.SysFont("arial", 20)
text2 = font.render("A story by: Anthony :)", True, (0, 0, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255, 255, 255))
    win.blit(img, (x, y))
    win.blit(img2, (50, 120))
    win.blit(img3, (50, 260))
    win.blit(img4, (50, 400))
    
    win.blit(text, (190, 0))
    win.blit(text2, (290, 40))


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
