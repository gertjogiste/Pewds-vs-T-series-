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

pygame.mixer_music.load("sounds/Intro(Hej Monika).ogg")
pygame.mixer_music.set_volume(0.5)
pygame.mixer_music.play(-1)

screen = pygame.display.set_mode(res)
background = pygame.image.load("images/background0.png").convert()

menu = Menu()

player = Player(640, 400, 4, tilesize, tilesize/16*7, screen)

mapnr = 0
Map = Maps()

enemies = [Minion(900, 40, 3, tilesize), Minion(700, 50, 3, tilesize), Minion(1400, 30, 3, tilesize)]
bullets = []

while True:
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = "MENU"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and state != "PAUSE":
                    state = "PAUSE"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and state == "PAUSE":
                    state = "GAME"

            if state == "PAUSE":
                screen.fill(must)
                pygame.display.flip()
                continue

            elif state == "MENU":
                del player
                player = Player(640, 400, 4, tilesize, tilesize/16*7, screen)

                del enemies
                enemies = [Minion(900, 40, 3, tilesize), Minion(700, 50, 3, tilesize), Minion(1400, 30, 3, tilesize)]

                bullets = []

                break

            screen.fill(sinine)
            screen.blit(background, [0,0])

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


