import pygame, sys
from player import *
from map import *

tilesize = 32
must = [0, 0, 0]
res = [800, 640]
Clock = pygame.time.Clock()
pygame.init()

player = Player(640, 400, 4, tilesize, tilesize/16*6)

screen = pygame.display.set_mode(res)

mapnr = 0
Map = Maps()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(must)

    Map.draw(screen, mapnr, tilesize)

    player.update(mapnr, Map)
    player.render(screen)



    pygame.display.flip()
    Clock.tick(60)


