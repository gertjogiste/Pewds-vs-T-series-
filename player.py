import pygame


class Player:
    def __init__(self, x, y, speed, size, jumpheight):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Player.PNG")
        self.speedx = speed
        self.speedy = 0
        self.size = size
        self.jumpheight = -jumpheight
        self.onGround = False
        self.tulp = (self.x+32 - (self.x+32)%64)/64
        self.rida = (self.y+32 - (self.y+32)%64)/64

    def update(self, mapnr, Maps):
        self.tulp = int((self.x - self.x % 64) / 64)

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if Maps.maps[mapnr][self.rida][self.tulp+1] == 0:
                self.x += self.speedx
        if key[pygame.K_LEFT]:
            self.x -= self.speedx
        if key[pygame.K_UP]:
            self.jump()
        self.gravity(mapnr, Maps)


    def jump(self):

        if self.onGround == True:
            self.speedy = self.jumpheight
            self.y += self.speedy


    def gravity(self, mapnr, Maps):
        self.rida = int((self.y-32 - (self.y-32)%64)/64)
        if Maps.maps[mapnr][self.rida+1][self.tulp] == 1:
            self.onGround = True
        elif Maps.maps[mapnr][self.rida+1][self.tulp] == 0:
            self.speedy += 1
            self.y += self.speedy
            self.onGround = False
        if self.onGround == True:
            self.y = self.rida*64 + 32



    def render(self, screen):
        screen.blit(self.image, [self.x - 32, self.y - 32])
