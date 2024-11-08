import pygame
import os

from circles import Circles

class Screen:

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        info = pygame.display.Info()
        self.screenWidth = info.current_w
        self.screenHeight = info.current_h

    def drawScreen(self):
        pygame.init();
        
        screen = pygame.display.set_mode((self.screenWidth - 20, self.screenHeight - 50), pygame.RESIZABLE)

        circles = Circles(screen)

        run = True
        while run:
            screen.fill('black')

            circles.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    circles.checkClick(mouse_x, mouse_y)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y or event.key == pygame.K_x:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        circles.checkClick(mouse_x, mouse_y)
                            

            pygame.display.flip()
        pygame.quit()