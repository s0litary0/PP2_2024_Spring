import pygame

class GameObject:
    def __init__(self, points, color, tile_width):
        self.points = points
        self.color = color
        self.tile_width = tile_width

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, (point[0], point[1], self.tile_width, self.tile_width))
            pygame.draw.rect(screen, "Black", (point[0], point[1], self.tile_width, self.tile_width), 1)