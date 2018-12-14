import pygame

class Player:
    def __init__(self, x, y, speed, size, jumpheight):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Player.PNG")
        self.speedx = speed
        self.speedy = 0
        self.size = size
        self.jumpheight = jumpheight
        self.onGround = False

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x += self.speedx
        if key[pygame.K_LEFT]:
            self.x -= self.speedx
        if key[pygame.K_UP] and self.onGround == True:
            self.speedy = self.jumpheight
            self.onGround = False

        if self.y + self.speedy < 500:
            self.speedy += 1
        else:
            self.speedy = 0
            self.onGround = True

        self.y += self.speedy

    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])
