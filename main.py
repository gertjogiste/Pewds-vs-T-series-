import pygame, sys
from player import *
from enemy import *
from map import *

tilesize = 32
must = [0, 0, 0]
sinine = (66, 134, 244)
res = [800, 640]
Clock = pygame.time.Clock()
pygame.init()

pygame.mixer_music.load("sounds/Final Boss(Bitch Lasagna).ogg")
pygame.mixer_music.play(-1)
screen = pygame.display.set_mode(res)
player = Player(640, 400, 4, tilesize, tilesize/16*7, screen)


mapnr = 0
Map = Maps()

enemies = [Minion(900, 40, 3, tilesize), Minion(700, 50, 3, tilesize), Minion(1400, 30, 3, tilesize)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(sinine)

    Map.draw(screen, mapnr, tilesize, player)

    player.update(mapnr, Map, enemies)
    player.render(screen)

    for minioon in enemies:
        minioon.update(mapnr, Map, tilesize)
        minioon.render(screen, player, tilesize)

    pygame.display.flip()
    Clock.tick(60)


