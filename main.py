import pygame, sys
from player import *
from enemy import *
from map import *
from menu import Menu

state = "MENU"  # MENU or GAME

tilesize = 32
must = [0, 0, 0]
sinine = (66, 134, 244)
res = [800, 640]
Clock = pygame.time.Clock()
pygame.init()

pygame.mixer_music.load("sounds/Final Boss(Bitch Lasagna).ogg")
pygame.mixer_music.play(-1)

screen = pygame.display.set_mode(res)

menu = Menu()

player = Player(640, 400, 4, tilesize, tilesize/16*7, screen)

mapnr = 0
Map = Maps()

enemies = [Minion(900, 40, 3, tilesize), Minion(700, 50, 3, tilesize), Minion(1400, 30, 3, tilesize)]
bullets = []

if state == "MENU":
    while True:
        state = menu.main_loop(Clock, screen, state)

        if state == "GAME":
            break

if state == "GAME":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(sinine)

        Map.draw(screen, mapnr, tilesize, player)

        player.update(mapnr, Map, enemies, bullets)
        player.render(screen)

        for minioon in enemies:
            minioon.update(mapnr, Map, tilesize, bullets)
            minioon.render(screen, player, tilesize)

        for b, bullet in enumerate(bullets):
            bullet.drawBullet(screen, player)
            delete = bullet.bulletUpdate(Map, mapnr)
            if delete == True:
                del bullets[b]
                continue
        pygame.display.flip()
        Clock.tick(60)


