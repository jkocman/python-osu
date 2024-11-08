import pygame
import random
import math

pygame.init()

class Circles:
    def __init__(self,screen):
        self.screen = screen
        self.circles = []
        self.sprite = pygame.image.load('sprites/hitcircle@2x.png')
        self.sprite = pygame.transform.scale(self.sprite, (200, 200))
        self.radius = 80
        self.spawnRandomCircles()

    def drawCircle(self,positionX,positionY):
        sprite_rect = self.sprite.get_rect(center=(positionX, positionY))
        self.screen.blit(self.sprite, sprite_rect)

    def spawnRandomCircles(self):
        from main import menuScreen

        self.circles = []
        x = random.randint(100, menuScreen.screenWidth - 100)
        y = random.randint(100, menuScreen.screenHeight - 100)
        self.circles.append((x, y))

    def checkClick(self, mouse_x, mouse_y):
        for (x, y) in self.circles:
            distance = math.sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2)

            if distance <= self.radius:
                self.spawnRandomCircles()
                return

    def update(self):
        for (x, y) in self.circles:
            self.drawCircle(x, y)
    




        