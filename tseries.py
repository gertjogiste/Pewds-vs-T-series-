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
        self.health = 10
        self.lifebar = [self.x + 50, self.y - 20, self.health * 10, 10]
        self.damage = 1
        self.headhitbox = pygame.Rect([self.x + 65, self.y + 12, 47, 72])
        self.bodyhitbox = pygame.Rect([self.x + 17, self.y + 84, 139, 146])

        self.normal1 = pygame.image.load("images/t-series boss1.png")
        self.normal1 = pygame.image.load("images/t-series boss2.png")
        self.death1 = pygame.image.load("images/t-series boss death1.png")
        self.death2 = pygame.image.load("images/t-series boss death2.png")
        self.tilesize = tilesize

        self.moving_hor = True

    def update(self, Maps, t_bullets, player, bullets):
        if 0 < self.y + self.speedy < res[1] - tilesize - self.image.get_rect().size[1]:
            self.y += self.speedy
        else:
            self.speedy = -self.speedy

        if randint(1, 30) == 30:
            self.speedx = -self.speedx

        if tilesize < self.x + self.speedx < (len(Maps.maps[2][0]) - 1) * tilesize - self.image.get_rect().size[0]:
            self.x += self.speedx

        if self.shootcooldown == 100:
            t_bullets.append(Bullet(self.shootpoint[0], self.shootpoint[1], tilesize, "Right", True, [player.x, player.y]))

        self.shootpoint = [self.x + 90, self.y + 156]

        if self.shootcooldown > 0:
            self.shootcooldown -= 1
        else:
            self.shootcooldown = 100

        self.headhitbox = pygame.Rect([self.x + 65, self.y + 12, 47, 72])
        self.bodyhitbox = pygame.Rect([self.x + 17, self.y + 84, 139, 146])
        self.lifebar = [self.x + 50 - player.x + 416, self.y - 20, self.health * 10, 10]

        for b, bullet in enumerate(bullets):
            if self.headhitbox.collidepoint(bullet.center[0], bullet.center[1]) \
                    or self.bodyhitbox.collidepoint(bullet.center[0], bullet.center[1]):
                del bullets[b]
                if self.health > 0:
                    if player.subs >= 5:
                        self.health -= self.damage + 1
                    elif player.subs >= 10:
                        self.health -= self.damage + 2
                    elif player.subs >= 15:
                        self.health -= self.damage + 3
                    elif player.subs >= 20:
                        self.health -= self.damage + 4
                    else:
                        self.health -= self.damage

        if self.health <= 0:
            return True
        else:
            return False

    def render(self, screen, player):
        screen.blit(self.image, [self.x - player.x + 416, self.y])

        if self.health > 5:
            pygame.draw.rect(screen, [50*(10-self.health), 255, 0], self.lifebar)
        elif self.health > 0:
            pygame.draw.rect(screen, [255, 50*self.health, 0], self.lifebar)