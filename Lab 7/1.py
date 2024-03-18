import pygame
import time

pygame.init()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

clock_image = pygame.image.load(r"C:\pp2\Lab 7\images\mainclock.png")
sec_hand_image = pygame.image.load(r"C:\pp2\Lab 7\images\leftarm.png")
min_hand_image = pygame.image.load(r"C:\pp2\Lab 7\images\rightarm.png")

done = False

rect1 = clock_image.get_rect()
rect1.center = screen.get_rect().center

#rect2 = sec_hand_image.get_rect()
#rect2.center = screen.get_rect().center

#rect3 = min_hand_image.get_rect()
#rect3.center = screen.get_rect().center

while not done:
    screen.fill((255, 255, 255))
    screen.blit(clock_image, rect1)
    #screen.blit(sec_hand_image, rect2)
    #screen.blit(min_hand_image, rect3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    sec_angle = -(current_time.tm_sec * 360 / 60)
    min_angle = -(current_time.tm_min * 360 / 60)

    sec_hand = pygame.transform.rotate(sec_hand_image, sec_angle)
    min_hand = pygame.transform.rotate(min_hand_image, min_angle)

    rect2 = sec_hand.get_rect()
    rect2.center = screen.get_rect().center
    screen.blit(sec_hand, rect2)
    
    rect3 = min_hand.get_rect()
    rect3.center = screen.get_rect().center
    screen.blit(min_hand, rect3)

    pygame.display.update()

pygame.quit()