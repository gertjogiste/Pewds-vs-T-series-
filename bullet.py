import pygame
from math import sin, cos, atan, pi
from settings import *


class Bullet:
    def __init__(self, x, y, tilesize, direction, t_bullet=False, destination=None):
        self.speed = 10
        self.center = [x, y]
        self.startpos = self.center[:]
        self.radius = 4
        self.hitbox = pygame.Rect([x-self.radius, y-self.radius, 2*self.radius, 2*self.radius])
        self.tilesize = tilesize
        self.direction = direction
        self.t_bullet = t_bullet

        if t_bullet is True:
            self.destination = destination
            self.dx = self.destination[0] - self.center[0]
            self.dy = self.destination[1] - self.center[1]

            if self.dx != 0:
                self.angle = atan(self.dy/self.dx)

    def drawBullet(self, screen, player):
        pygame.draw.circle(screen, [237, 14, 14], [self.center[0] - player.x + 416, self.center[1]], self.radius)

    def bulletUpdate(self, Maps, mapnr, player=None):
        if self.t_bullet is False:
            self.hitbox = pygame.Rect([self.center[0] - self.radius, self.center[1] - self.radius, 2 * self.radius, 2 * self.radius])
            if self.direction == "Right":
                self.center[0] += self.speed
            elif self.direction == "Left":
                self.center[0] -= self.speed
        else:
            if self.startpos[0] < self.destination[0]:
                self.center[0] += int(cos(self.angle) * self.speed)
                self.center[1] += int(sin(self.angle) * self.speed)
            else:
                self.center[0] -= int(cos(self.angle) * self.speed)
                self.center[1] -= int(sin(self.angle) * self.speed)

        tulpP = int((self.center[0] + self.radius) / self.tilesize)
        ridaA = int((self.center[1] + self.radius) / self.tilesize)
        tulpV = int((self.center[0] - self.radius) / self.tilesize)
        ridaY = int((self.center[1] - self.radius) / self.tilesize)

        try:
            if Maps.maps[mapnr][ridaA][tulpP] > 0 or Maps.maps[mapnr][ridaA][tulpV] > 0 or Maps.maps[mapnr][ridaY][tulpP] > 0 or Maps.maps[mapnr][ridaY][tulpV] > 0:
                return True
        except IndexError:
            return True