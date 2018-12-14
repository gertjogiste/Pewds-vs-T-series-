import pygame


class Player:
    def __init__(self, x, y, speed, size, jumpheight, screen):
        self.x = x
        self.y = y

        self.stand = pygame.image.load("images/pewds_stand.png").convert_alpha()
        self.skid = pygame.image.load("images/pewds_skid.png").convert_alpha()
        self.walk1 = pygame.image.load("images/pewds_walk1.png").convert_alpha()
        self.walk2 = pygame.image.load("images/pewds_walk2.png").convert_alpha()
        self.walk3 = pygame.image.load("images/pewds_walk3.png").convert_alpha()
        self.jumping = pygame.image.load("images/pewds_jump.png").convert_alpha()

        self.speedx = speed
        self.speedy = 0
        self.size = size
        self.jumpheight = -jumpheight
        self.onGround = False
        self.tilesize = size
        self.orientation = "Right"
        self.image = self.stand
        self.counter = 0
        self.cooldown = 0

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

            if self.orientation == "Left":
                self.orientation = "Right"
                self.image = self.skid
            self.walk()
        elif key[pygame.K_LEFT]:
            tulpV = int((self.x - self.speedx - (self.tilesize/2)) / self.tilesize)
            ridaA = int((self.y + (self.tilesize/2-1)) / self.tilesize)
            ridaY = int((self.y - (self.tilesize/2)) / self.tilesize)
            if self.orientation == "Right":
                self.orientation = "Left"
                self.image = self.skid
            self.walk()

            if Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaY][tulpV] == 0:
                self.x -= self.speedx

        if key[pygame.K_UP]:
            self.jump()
            self.image = self.jumping


        if not key[pygame.K_RIGHT] and  not key[pygame.K_LEFT]:
            self.image = self.stand

        self.gravity(mapnr, Maps)

        if self.cooldown > 0:
            self.cooldown -= 1

    def jump(self):
        if self.onGround and self.cooldown == 0:
            self.speedy = self.jumpheight
            self.y += self.speedy
            self.onGround = False
            self.cooldown = 15

    def gravity(self, mapnr, Maps):
        tulpP = int((self.x + (self.tilesize/2-1)) / self.tilesize)
        tulpV = int((self.x - (self.tilesize/2)) / self.tilesize)
        ridaA = int((self.y + self.speedy + (self.tilesize/2)) / self.tilesize)
        ridaY = int((self.y + self.speedy - self.tilesize - (self.tilesize/2)) / self.tilesize)

        if self.speedy < 0 and Maps.maps[mapnr][ridaY][tulpV] == 1 or Maps.maps[mapnr][ridaY][tulpP] == 1:
            self.speedy = 0
        elif Maps.maps[mapnr][ridaA][tulpV] == 1 or Maps.maps[mapnr][ridaA][tulpP] == 1:
            self.onGround = True
        elif Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaA][tulpP] == 0:
            self.speedy += 1
            self.y += self.speedy
            self.onGround = False
        if self.onGround:
            self.y = ridaA*self.tilesize - (self.tilesize/2)

    def walk(self):
        self.counter += 1
        if self.counter > 29:
            self.counter = 0
        if self.counter < 10:
            self.image = self.walk1
        elif self.counter < 20:
            self.image = self.walk2
        elif self.counter < 30:
            self.image = self.walk3



    def render(self, screen):
        if self.orientation == "Right":
            screen.blit(self.image, [400, self.y - (self.tilesize) - 16])
        elif self.orientation == "Left":
            screen.blit(pygame.transform.flip(self.image, True, False), [400, self.y - (self.tilesize) - 16])
