import pygame


class Minion:
    def __init__(self, x, y, life, tilesize, type):
        self.x = x
        self.x_max = self.x
        self.x_min = self.x - 200
        self.y = y
        self.size = 10
        self.speed = 3
        self.ver_speed = 5
        self.type = type

        self.image = pygame.image.load("images/indian_walk1.png")
        self.walk1 = pygame.image.load("images/indian_walk1.png")
        self.walk2 = pygame.image.load("images/indian_walk2.png")
        self.walk3 = pygame.image.load("images/indian_walk3.png")
        self.counter = 0


        self.orientation = "Rights"
        self.hitbox = pygame.Rect([self.x - tilesize / 2, self.y - tilesize, tilesize, tilesize])
        if self.type == 0:
            self.health = life
            self.lifebar = [self.x, self.y - 30, self.health * 10, 5]

    def update(self, mapnr, Maps, tilesize, bullets):
        tulpP = int((self.x + tilesize / 2 + self.speed + (tilesize/2-1)) / tilesize)
        ridaA = int((self.y + (tilesize/2-1)) / tilesize)
        ridaY = int((self.y - (tilesize/2)) / tilesize)
        tulpV = int((self.x + tilesize / 2 - (tilesize/2)) / tilesize)

        if self.speed > 0 and Maps.maps[mapnr][ridaA][tulpP] == 0 and Maps.maps[mapnr][ridaY][tulpP] == 0:
            self.x += self.speed
            self.orientation = "Right"
            self.walk()
        elif self.speed < 0 and Maps.maps[mapnr][ridaA][tulpV] == 0 and Maps.maps[mapnr][ridaY][tulpV] == 0:
            self.x += self.speed
            self.orientation = "Left"
            self.walk()
        else:
            self.speed = -self.speed

        self.gravity(mapnr, Maps, tilesize)

        self.hitbox = pygame.Rect([self.x - tilesize / 2, self.y - tilesize, tilesize, tilesize])

        if self.type == 0:
            for b, bullet in enumerate(bullets):
                if self.hitbox.colliderect(bullet.hitbox):
                    if self.health > 0:
                        self.health -= 1
                    del bullets[b]
            if self.health == 0:
                """surma asjad siia"""

        if self.type == 1:
            for b, bullet in enumerate(bullets):
                if self.hitbox.colliderect(bullet.hitbox):
                    del bullets[b]

        if self.type == 0:
            self.lifebar = [self.x, self.y - 30, self.health * 10, 5]

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
        if self.type == 0:
            location = [self.lifebar[0] - player.x + 416, self.lifebar[1], self.lifebar[2], self.lifebar[3]]
            if self.health > 1:
                pygame.draw.rect(screen, [255*(3-self.health), 255, 0], location)
            elif self.health == 1:
                pygame.draw.rect(screen, [255, 0, 0], location)

        if self.orientation == "Right":
            screen.blit(self.image, [self.x - player.x + 416, self.y - tilesize/2])
        elif self.orientation == "Left":
            screen.blit(pygame.transform.flip(self.image, True, False), [self.x - player.x + 416, self.y - tilesize/2])
