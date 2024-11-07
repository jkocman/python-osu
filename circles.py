import pygame
import random
import math

pygame.init()

class Circles:
    def __init__(self,screen):
        self.screen = screen
        self.circles = []
        self.spawnRandomCircles()

    def drawCircle(self,positionX,positionY):
        pygame.draw.circle(self.screen, (0,0,0), (positionX, positionY), 20)

    def spawnRandomCircles(self):
        self.circles = []
        x = random.randint(20, 600 - 20)
        y = random.randint(20, 400 - 20)
        self.circles.append((x, y))

    def checkClick(self, mouse_x, mouse_y):
        for (x, y) in self.circles:
            distance = math.sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2)

            if distance <= 20:
                self.spawnRandomCircles()
                return

    def update(self):
        for (x, y) in self.circles:
            self.drawCircle(x, y)
    




        