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
        self.normal2 = pygame.image.load("images/t-series boss2.png")
        self.death1 = pygame.image.load("images/t-series boss death1.png")
        self.death2 = pygame.image.load("images/t-series boss death2.png")

        self.explosion1 = pygame.image.load("images/explosion1.png")
        self.explosion2 = pygame.image.load("images/explosion2.png")
        self.explosion3 = pygame.image.load("images/explosion3.png")
        self.explosion4 = pygame.image.load("images/explosion4.png")
        self.explosion5 = pygame.image.load("images/explosion5.png")
        self.explosion6 = pygame.image.load("images/explosion6.png")
        self.explosion7 = pygame.image.load("images/explosion7.png")
        self.explosions = [self.explosion1, self.explosion2, self.explosion3, self.explosion4,
                           self.explosion5, self.explosion6, self.explosion7]

        self.blink_counter = 0
        self.explosion_counter = 0

    def update(self, Maps, t_bullets, player, bullets):
        if self.health > 0:
            if 0 < self.y + self.speedy < res[1] - tilesize - self.image.get_rect().size[1]:
                self.y += self.speedy
            else:
                self.speedy = -self.speedy

            if randint(1, 30) == 30:
                self.speedx = -self.speedx

            if tilesize < self.x + self.speedx < (len(Maps.maps[2][0]) - 1) * tilesize - self.image.get_rect().size[0]:
                self.x += self.speedx

            if self.shootcooldown == 100 and self.health > 0:
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

            if self.blink_counter < 100:
                self.blink_counter += 1
            else:
                self.blink_counter = 0

            return False

        elif self.health <= 0:
            if self.explosion_counter < 63:
                self.explosion_counter += 1
            else:
                return True

    def render(self, screen, player):
        if self.health > 0:
            if self.blink_counter > 90:
                self.image = self.normal2
            else:
                self.image = self.normal1
        else:
            self.image = self.death1

        if self.explosion_counter < 21:
            screen.blit(self.image, [self.x - player.x + 416, self.y])

        if self.health > 5:
            pygame.draw.rect(screen, [50*(10-self.health), 255, 0], self.lifebar)
        elif self.health > 0:
            pygame.draw.rect(screen, [255, 50*self.health, 0], self.lifebar)
        else:
            if 0 <= self.explosion_counter < 35:
                screen.blit(self.explosions[int(self.explosion_counter / 5)], [self.x + 30 - player.x + 416, self.y])
            if 7 <= self.explosion_counter < 42:
                screen.blit(self.explosions[int(self.explosion_counter / 5) - 2], [self.x + 80 - player.x + 416, self.y + 50])
            if 14 <= self.explosion_counter < 49:
                screen.blit(self.explosions[int(self.explosion_counter / 5) - 3], [self.x + 30 - player.x + 416, self.y + 100])
            if 21 <= self.explosion_counter < 56:
                screen.blit(self.explosions[int(self.explosion_counter / 5) - 5], [self.x + 10 - player.x + 416, self.y + 150])
            if 28 <= self.explosion_counter < 63:
                screen.blit(self.explosions[int(self.explosion_counter / 5) - 6], [self.x + 110 - player.x + 416, self.y + 150])
