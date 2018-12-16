import pygame, sys
from player import *
from enemy import *
from map import *
from menu import Menu
from settings import *
from tseries import TSeries

state = "MENU"  # MENU or GAME

pygame.init()
pygame.font.init()

Clock = pygame.time.Clock()
screen = pygame.display.set_mode(res)


background1 = pygame.image.load("images/background0.png").convert()
background2 = pygame.image.load("images/background1.png").convert()
background3 = pygame.image.load("images/background3.png").convert()
background = background1

pause_screen = pygame.image.load("images/pause_screen.png").convert_alpha()

font = pygame.font.SysFont("Comic Sans MS", 30)

menu = Menu()

player = Player(200, 400, 4, tilesize, tilesize/16*7)

mapnr = 0
tseriesdead = False

minions = []
bullets = []
t_bullets = []

while True:
    if state == "MENU":
        pygame.mixer.music.pause()
        pygame.mixer.stop()
        pygame.mixer.music.load("sounds/Menu_music.ogg")
        pygame.mixer.music.play()
        while True:
            state = menu.main_loop(Clock, screen, state)

            if state == "GAME":
                pygame.mixer.music.unpause()
                break

    if state == "GAME":
        player = Player(200, 400, 4, tilesize, tilesize / 16 * 7, player.subs)
        minions = []
        bullets = []
        t_bullets = []

        pygame.mixer.music.stop()
        if mapnr == 0:
            background = background1
            pygame.mixer.music.load("sounds/Intro(Hej Monika).ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if mapnr == 1:
            background = background2
            pygame.mixer.music.load("sounds/Story(Hej Monika).ogg")
            pygame.mixer.music.play(-1)
        elif mapnr == 2 and not tseriesdead:
            background = background3
            pygame.mixer.music.load("sounds/Final Boss(Bitch Lasagna).ogg")
            pygame.mixer.music.play(-1)

            tseries = TSeries(300, 300, 2, 10)
            tseriesdead = False

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
                mapnr = 0
                player.subs = 0
                del minions
                del bullets

                break

            textsurface = font.render("Subcriers: " + str(player.subs), True, valge)
            screen.fill(sinine)
            screen.blit(background, [(-player.x - 416) / 2, 0])
            screen.blit(textsurface, [550, 32])

            Map.draw(screen, mapnr, tilesize, player, minions)

            changelevel = player.update(mapnr, Map, minions, bullets, t_bullets)

            player.render(screen)

            if mapnr == 2:
                if not tseriesdead:
                    tseriesdead = tseries.update(Map, t_bullets, player, bullets)
                    tseries.render(screen, player)

            if changelevel is True:
                mapnr += 1
                break

            elif changelevel == "MENU":
                state = "MENU"
                mapnr = 0
                player.subs = 0
                break

            for m, minioon in enumerate(minions):
                minioon.update(mapnr, Map, tilesize, bullets)
                minioon.render(screen, player, tilesize)
                if minioon.y < 0:
                    del minions[m]

            for b, bullet in enumerate(bullets):
                bullet.drawBullet(screen, player)
                delete = bullet.bulletUpdate(Map, mapnr)
                if delete is True:
                    del bullets[b]
                    continue

            for b, bullet in enumerate(t_bullets):
                bullet.drawBullet(screen, player)
                delete = bullet.bulletUpdate(Map, mapnr, player)
                if delete is True:
                    del t_bullets[b]
                    continue

            pygame.display.flip()
            Clock.tick(60)


