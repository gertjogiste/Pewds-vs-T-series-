import pygame, sys
from player import *

must = [0, 0, 0]
res = [800, 640]

pygame.init()

player = Player(300, 400, 5, 64, -15)

screen = pygame.display.set_mode(res)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(must)

    player.update()
    player.render(screen)

    pygame.display.flip()
    pygame.time.wait(16)
