import pygame

class Minion:
    def __init__(self, x, y, life):
        self.x = x
        self.x_max = self.x
        self.x_min = self.x - 200
        self.y = y
        self.size = 10
        self.speed = 3
        self.ver_speed = 5
        self.image = pygame.image.load("16.png")

    def update(self, mapnr, Maps, tilesize):
        tulpP = int((self.x + self.speed + (tilesize/2-1)) / tilesize)
        ridaA = int((self.y + (tilesize/2-1)) / tilesize)
        ridaY = int((self.y - (tilesize/2)) / tilesize)
        tulpV = int((self.x - (tilesize/2)) / tilesize)

        if self.x + self.speed > self.x_max or self.x + self.speed < self.x_min:
            self.speed = -self.speed
        if self.speed > 0 and Maps.maps[mapnr][ridaA][tulpP] == 0 and Maps.maps[mapnr][ridaY][tulpP] == 0:
            self.x += self.speed
        elif self.speed < 0 and Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaY][tulpV] == 0:
            self.x += self.speed
        else:
            self.speed = -self.speed

        self.gravity(mapnr, Maps, tilesize)

    def gravity(self, mapnr, Maps, tilesize):
        tulpP = int((self.x + (tilesize/2-1)) / tilesize)
        tulpV = int((self.x - (tilesize/2)) / tilesize)
        ridaA = int((self.y + (tilesize/2)) / tilesize)
        ridaY = int((self.y - (tilesize/2)) / tilesize)

        if Maps.maps[mapnr][ridaA][tulpV] == 1 or Maps.maps[mapnr][ridaA][tulpP] == 1:
            self.onGround = True
        elif Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaA][tulpP] == 0:
            self.ver_speed += 1
            self.y += self.ver_speed
            self.onGround = False
        if self.onGround:
            self.y = ridaA*tilesize - (tilesize/2)
            
    def render(self, screen, player, tilesize):
        screen.blit(self.image, [self.x - player.x + 416, self.y - tilesize/2])

    
