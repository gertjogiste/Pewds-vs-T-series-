import pygame, sys

must = [0, 0, 0]
res = [800, 640]

pygame.init()

screen = pygame.display.set_mode(res)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(must)

    pygame.display.flip()
    pygame.time.wait(16)
