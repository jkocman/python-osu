import pygame

from circles import Circles

class Screen:

    def __init__(self,screenWidth,screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def drawScreen(self):
        pygame.init();

        screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        circles = Circles(screen)
        run = True
        while run:
            screen.fill((255,255,255))
            circles.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                

            pygame.display.flip()
        pygame.quit()