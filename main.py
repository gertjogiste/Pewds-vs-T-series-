import pygame, sys
from player import *
from enemy import *
from map import *
from menu import Menu

state = "MENU"  # MENU or GAME

tilesize = 32
must = [0, 0, 0]
sinine = (66, 134, 244)
valge = (255, 255, 255)
res = [800, 640]
Clock = pygame.time.Clock()
pygame.init()

pygame.mixer_music.load("sounds/Intro(Hej Monika).ogg")
pygame.mixer_music.set_volume(0.3)
pygame.mixer_music.play(-1)

pygame.font.init()

screen = pygame.display.set_mode(res)
background = pygame.image.load("images/background0.png").convert()
pause_screen = pygame.image.load("images/pause_screen.png").convert_alpha()
font = pygame.font.SysFont("Comic Sans MS", 30)


menu = Menu()

player = Player(200, 400, 4, tilesize, tilesize/16*7, screen)

mapnr = 0

#type 1 - pewdsM type 0 - t-seriesM
minions = []
bullets = []

while True:
    if state == "MENU":
        pygame.mixer.music.pause()
        while True:
            state = menu.main_loop(Clock, screen, state)

            if state == "GAME":
                pygame.mixer.music.unpause()
                break

    if state == "GAME":
        Map = Maps(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = "MENU"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and state != "PAUSE":
                    state = "PAUSE"
                    pygame.mixer.music.pause()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and state == "PAUSE":
                    state = "GAME"
                    pygame.mixer.music.unpause()
            if state == "PAUSE":

                screen.blit(pause_screen, [0, 0])

                pygame.display.flip()
                continue

            elif state == "MENU":
                del player
                player = Player(200, 400, 4, tilesize, tilesize/16*7, screen)

                del minions
                minions = []

                bullets = []

                break
            textsurface = font.render("Subcriers: " + str(player.subs), True, valge)
            screen.fill(sinine)
            screen.blit(background, [0, 0])
            screen.blit(textsurface, [550, 32])

            Map.draw(screen, mapnr, tilesize, player, minions)

            player.update(mapnr, Map, minions, bullets)
            player.render(screen)

            for m,minioon in enumerate(minions):
                minioon.update(mapnr, Map, tilesize, bullets)
                minioon.render(screen, player, tilesize)
                if minioon.y < 0:
                    del minions[m]

            for b, bullet in enumerate(bullets):
                bullet.drawBullet(screen, player)
                delete = bullet.bulletUpdate(Map, mapnr)
                if delete == True:
                    del bullets[b]
                    continue

            pygame.display.flip()
            Clock.tick(60)


