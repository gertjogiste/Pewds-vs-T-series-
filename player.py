import pygame


class Player:
    def __init__(self, x, y, speed, size, jumpheight):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Nimetu.png")
        self.speedx = speed
        self.speedy = 0
        self.size = size
        self.jumpheight = -jumpheight
        self.onGround = False
        self.tilesize = size


        self.tulpP = int((self.x + (self.tilesize/2)) / self.tilesize)
        self.ridaA = int((self.y + (self.tilesize/2)) / self.tilesize)
        self.tulpV = int((self.x - (self.tilesize/2)) / self.tilesize)
        self.ridaY = int((self.y - (self.tilesize/2)) / self.tilesize)

    def update(self, mapnr, Maps):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            tulpP = int((self.x + self.speedx + (self.tilesize/2-1)) / self.tilesize)
            ridaA = int((self.y + (self.tilesize/2-1)) / self.tilesize)
            ridaY = int((self.y - (self.tilesize/2)) / self.tilesize)

            if Maps.maps[mapnr][ridaA][tulpP] == 0 and Maps.maps[mapnr][ridaY][tulpP] == 0:
                self.x += self.speedx

        elif key[pygame.K_LEFT]:
            tulpV = int((self.x - self.speedx - (self.tilesize/2)) / self.tilesize)
            ridaA = int((self.y + (self.tilesize/2-1)) / self.tilesize)
            ridaY = int((self.y - (self.tilesize/2)) / self.tilesize)

            if Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaY][tulpV] == 0:
                self.x -= self.speedx

        if key[pygame.K_UP]:
            self.jump()

        self.gravity(mapnr, Maps)

    def jump(self):
        if self.onGround:
            self.speedy = self.jumpheight
            self.y += self.speedy
            self.onGround = False

    def gravity(self, mapnr, Maps):
        self.tulpP = int((self.x + (self.tilesize/2-1)) / self.tilesize)
        self.tulpV = int((self.x - (self.tilesize/2)) / self.tilesize)
        self.ridaA = int((self.y + (self.tilesize/2)) / self.tilesize)
        self.ridaY = int((self.y - (self.tilesize/2)) / self.tilesize)


        if Maps.maps[mapnr][self.ridaA][self.tulpV] == 1 or Maps.maps[mapnr][self.ridaA][self.tulpP] == 1:
            self.onGround = True
        elif Maps.maps[mapnr][self.ridaA][self.tulpV] == 0 and Maps.maps[mapnr][self.ridaA][self.tulpP] == 0:
            self.speedy += 1
            self.y += self.speedy
            self.onGround = False
        if self.onGround:
            self.y = self.ridaA*self.tilesize - (self.tilesize/2)

    def render(self, screen):
        screen.blit(self.image, [400, self.y -(self.tilesize/2)])
