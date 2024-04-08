import pygame
from game_object import GameObject 
from random import randint

class Food(GameObject):
    def __init__(self):
        super().__init__([[40, 40]], "Green", 20)
        self.weight = 1 
        self.counter = 5
    def spawn(self, points):
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.counter = 5
        self.weight = randint(1, 4)
        if self.weight == 3:
            pygame.time.set_timer(pygame.USEREVENT, 1000)
        if self.weight == 1:
            self.color = "Green"
        if self.weight == 2:
            self.color = "Red"
        if self.weight == 3:
            self.color = "Yellow"
        self.points[0][0] = randint(0, 19) * 20
        self.points[0][1] = randint(0, 14) * 20
        if [self.points[0][0], self.points[0][1]] in points:
            self.spawn(points)

    def was_eaten(self, point):
        if self.points[0][0] == point[0] and self.points[0][1] == point[1]:
            return self.weight
        return 0