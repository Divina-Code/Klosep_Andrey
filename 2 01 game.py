import pygame

pygame.int()

gamdis = pygame.display.set_mode((800,600) )
game =True
while game:

    events =pygame.event.get()

    for e in events:
        if e.tipe == pygame.QUIT:
            game = False


pygame.quit()
