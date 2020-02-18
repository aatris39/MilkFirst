import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
#img = pygame.image.load('assets/forest.png')
#img = pygame.transform.scale(img, (800,600))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    #win.blit(img, (0, 0))

    pygame.display.update()

pygame.quit()
