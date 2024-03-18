import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")

done = False
x, y = 400, 300
while not done:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, "Red", (x, y), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_DOWN:
                y += 20
    pygame.display.update()
    
pygame.quit()