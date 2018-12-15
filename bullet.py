import pygame


class Bullet:
    def __init__(self, x, y, tilesize, direction):
        self.speed = 10
        self.center = [x, y]
        self.radius = 4
        self.hitbox = pygame.Rect([x-self.radius, y-self.radius, 2*self.radius, 2*self.radius])
        self.tilesize = tilesize
        self.direction = direction

    def drawBullet(self, screen, player):
        pygame.draw.circle(screen, [237, 14, 14], [self.center[0] - player.x + 416, self.center[1]], self.radius)

    def bulletUpdate(self, Maps, mapnr):
        self.hitbox = pygame.Rect([self.center[0] - self.radius, self.center[1] - self.radius, 2 * self.radius, 2 * self.radius])
        if self.direction == "Right":
            self.center[0] += self.speed
        elif self.direction == "Left":
            self.center[0] -= self.speed

        tulpP = int((self.center[0] + self.radius) / self.tilesize)
        ridaA = int((self.center[1] + self.radius) / self.tilesize)
        tulpV = int((self.center[0] - self.radius) / self.tilesize)
        ridaY = int((self.center[1] - self.radius) / self.tilesize)

        if Maps.maps[mapnr][ridaA][tulpP] > 0 or Maps.maps[mapnr][ridaA][tulpV] > 0 or Maps.maps[mapnr][ridaY][tulpP] > 0 or Maps.maps[mapnr][ridaY][tulpV] > 0:
            return True
