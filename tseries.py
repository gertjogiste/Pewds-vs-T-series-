import pygame
from random import randint
from settings import *
from bullet import Bullet


class TSeries:
    def __init__(self, x, y, speed, life):
        self.x = x
        self.y = y
        self.shootpoint = [self.x + 90, self.y + 156]
        self.shootcooldown = 100
        self.speedx = speed
        self.speedy = speed
        self.life = life
        self.image = pygame.image.load("images/t-series boss1.png")

        self.normal1 = pygame.image.load("images/t-series boss1.png")
        self.normal1 = pygame.image.load("images/t-series boss2.png")
        self.death1 = pygame.image.load("images/t-series boss death1.png")
        self.death2 = pygame.image.load("images/t-series boss death2.png")

        self.moving_hor = True

    def update(self, Maps, bullets, player):
        if 0 < self.y + self.speedy < res[1] - tilesize - self.image.get_rect().size[1]:
            self.y += self.speedy
        else:
            self.speedy = -self.speedy

        if randint(1, 30) == 30:
            self.speedx = -self.speedx

        if tilesize < self.x + self.speedx < (len(Maps.maps[2][0]) - 1) * tilesize - self.image.get_rect().size[0]:
            self.x += self.speedx

        if self.shootcooldown == 100:
            bullets.append(Bullet(self.shootpoint[0], self.shootpoint[1], tilesize, "Right", True, [player.x, player.y]))

        self.shootpoint = [self.x + 90, self.y + 156]

        if self.shootcooldown > 0:
            self.shootcooldown -= 1
        else:
            self.shootcooldown = 100

    def render(self, screen, player):
        screen.blit(self.image, [self.x - player.x + 416, self.y])