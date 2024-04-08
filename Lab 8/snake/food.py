import pygame
from game_object import GameObject 
from random import randint

class Food(GameObject):
    def __init__(self):
        super().__init__([[40, 40]], "Green", 20)

    def spawn(self, points):
        self.points[0][0] = randint(0, 19) * 20
        self.points[0][1] = randint(0, 14) * 20
        if [self.points[0][0], self.points[0][1]] in points:
            self.spawn(points)

    def was_eaten(self, point):
        if self.points[0][0] == point[0] and self.points[0][1] == point[1]:
            return True
        return False
