import pygame
import random

pygame.init()

class Circles:
    def __init__(self,screen):
        self.screen = screen
        self.circles = []
        self.spawn_time = pygame.time.get_ticks()

    def drawCircle(self,positionX,positionY):
        pygame.draw.circle(self.screen, (0,0,0), (positionX, positionY), 20)

    def spawnRandomCircles(self):
        self.circles = []
        x = random.randint(20, 600 - 20)
        y = random.randint(20, 400 - 20)
        self.circles.append((x, y))

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > 2000:
            self.spawn_time = pygame.time.get_ticks() 
            self.spawnRandomCircles()

        for (x, y) in self.circles:
            self.drawCircle(x, y)
    




        