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

        self.tulpP = int((self.x + 32) / 64)
        self.ridaA = int((self.y + 32) / 64)
        self.tulpV = int((self.x - 32) / 64)
        self.ridaY = int((self.y - 32) / 64)

    def update(self, mapnr, Maps):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            tulpP = int((self.x + self.speedx + 31) / 64)
            ridaA = int((self.y + 31) / 64)
            ridaY = int((self.y - 32) / 64)

            if Maps.maps[mapnr][ridaA][tulpP] == 0 and Maps.maps[mapnr][ridaY][tulpP] == 0:
                self.x += self.speedx

        elif key[pygame.K_LEFT]:
            tulpV = int((self.x - self.speedx - 32) / 64)
            ridaA = int((self.y + 31) / 64)
            ridaY = int((self.y - 32) / 64)

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
        self.tulpP = int((self.x + 31) / 64)
        self.tulpV = int((self.x - 32) / 64)
        self.ridaA = int((self.y + 32) / 64)
        self.ridaY = int((self.y - 32) / 64)

        if Maps.maps[mapnr][self.ridaA][self.tulpV] == 1 or Maps.maps[mapnr][self.ridaA][self.tulpP] == 1:
            self.onGround = True
        elif Maps.maps[mapnr][self.ridaA][self.tulpV] == 0 and Maps.maps[mapnr][self.ridaA][self.tulpP] == 0:
            self.speedy += 1
            self.y += self.speedy
            self.onGround = False
        if self.onGround:
            self.y = self.ridaA*64 - 32

    def render(self, screen):
        screen.blit(self.image, [self.x -32, self.y -32])
