import pygame, sys

res = [800, 640]
screen = pygame.display.set_mode(res)
roheline = [0, 200, 0]
hele_roheline =[0, 255, 0]
punane = [200, 0, 0]
hele_punane = [255, 0, 0]
valge = [255, 255, 255]


class Menu:
    def __init__(self):
        # nuppude asukoht, x, y
        self.roheline_kast = (150, 550, 100, 50)
        self.punane_kast = (550, 550, 100, 50)
        self.rohelisetoon = roheline
        self.punasetoon = punane
        self.menugame_pic = pygame.image.load("images/pewds_stand.png")
        self.play_pic = pygame.image.load("images/PLAY_BUTTON.png")
        self.quit_pic = pygame.image.load("images/QUIT_BUTTON.png")
        self.menu_pic = pygame.image.load("images/MAIN-PIC.png")

    def update(self, state):
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if 150 < mouse_pos[0] < 150 + 100 and 550 < mouse_pos[1] < 550 + 50:
            self.rohelisetoon = hele_roheline

            if pressed[0]:
                state = "GAME"
        else:
            self.rohelisetoon = roheline

        if 550 < mouse_pos[

        0] < 550 + 100 and 550 < mouse_pos[1] < 550 + 50:
            self.punasetoon = hele_punane

            if pressed[0]:
                pygame.quit()
                sys.exit()
        else:
            self.punasetoon = punane

        return state

    def render(self, screen):
        pygame.draw.rect(screen, self.rohelisetoon, self.roheline_kast)
        pygame.draw.rect(screen, self.punasetoon, self.punane_kast)
        screen.blit(self.play_pic, [150, 550])
        screen.blit(self.quit_pic, [550, 550])
        screen.blit(self.menu_pic, [25, 200])
        screen.blit(self.menugame_pic, [300, 300])
    def main_loop(self, clock, screen, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(valge)

        state = self.update(state)
        self.render(screen)

        pygame.display.update()
        clock.tick(60)

        return state

