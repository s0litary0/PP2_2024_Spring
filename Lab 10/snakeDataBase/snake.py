import pygame
import time
from insert_score import insert_score
from game_object import GameObject
from worm import Worm
from food import Food

pygame.init()

font = pygame.font.SysFont("comicsansms", 16)

def create_background(screen, width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    tile_width = 20
    y = 0
    while y < height:
        x = 0
        while x < width:
            row = y // tile_width
            col = x // tile_width
            pygame.draw.rect(screen, colors[(row + col) % 2], (x, y, tile_width, tile_width))
            x += tile_width
        y += tile_width

def hit_border(x, y):
    if x == -20 or x == 400 or y == -20 or y == 300:
        return True
    return False

done = False
playing = True

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

speed = 6
score = 0
level = 1
scoreBar = "Your score: {}"
levelBar = "Level: {}"
worm = Worm()

food = Food()
create_background(screen, 400, 300)

username = input("Enter your name: ")

while not done:
    if username and playing:    
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.USEREVENT:
                food.counter -= 1
                #print(food.counter)
                if food.counter == 0:
                    food.spawn(worm.points)
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_BACKSPACE:
                    #playing = not playing
            else:
                filtered_events.append(event)

        if playing:
            worm.process_input(filtered_events)
            worm.move()
            if hit_border(worm.points[-1][0], worm.points[-1][1]):
                done = True
            if worm.hit_body():
                done = True

            #If food was eaten: increase size of snake and spawn new food
            if food.was_eaten(worm.points[-1]) != 0:
                score += food.was_eaten(worm.points[-1])
                if score % 5 == 0:
                    level += 1
                    speed += 1 
                worm.increase()
                food.spawn(worm.points)
            create_background(screen, 400, 300)

            worm.draw(screen)
            food.draw(screen)
            scoreText = font.render(scoreBar.format(score), True, "Red")
            levelText = font.render(levelBar.format(level), True, "Red")
            screen.blit(scoreText, (0, 0))
            screen.blit(levelText, (320, 0))
        pygame.display.flip()
        clock.tick(speed)

insert_score(username, score)