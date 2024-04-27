from game_object import GameObject
import pygame

class Worm(GameObject):
    def __init__(self):
        super().__init__([[120, 140], [140, 140], [160, 140]], "Blue", 20)
        self.dx = 20
        self.dy = 0
    def move(self):
        for i in range(0, len(self.points) - 1):
            self.points[i][0] = self.points[i + 1][0]
            self.points[i][1] = self.points[i + 1][1]
        
        self.points[-1][0] += self.dx
        self.points[-1][1] += self.dy
        #print(self.points)

    def increase(self):
        self.points.append([self.points[-1][0] + self.dx, self.points[-1][1] + self.dy])
        #print(self.points)
    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.dy != 20:
                self.dy = -20
                self.dx = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.dy != -20:
                self.dy = 20
                self.dx = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.dx != 20:
                self.dy = 0
                self.dx = -20
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.dx != -20:
                self.dy = 0
                self.dx = 20
                
    def hit_body(self):
        count = 0
        for point in self.points:
            if self.points[-1] == point:
                count += 1
        if count == 2:
            return True
        return False