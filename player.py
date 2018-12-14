import pygame

class Player:
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player.png")
        self.speedx = speed
        self.speedy = 0
        self.size = size



    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x += self.speed
        if key[pygame.K_LEFT]:
            self.x += self.speed
        if key[pygame.K_UP]:
            self.speedy = -5

        self.y += speedy

