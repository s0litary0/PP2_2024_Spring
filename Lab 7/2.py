import pygame 
import os 
 
pygame.init() 

screen = pygame.display.set_mode((1200, 675)) 
pygame.display.set_caption("Music Player") 
 
background = pygame.image.load("C:\pp2\Lab 7\images\minecraft.jpeg")  
 
songs = os.listdir("C:\pp2\Lab 7\music") 
 
playingMusic = True
index = 0
done = False

pygame.mixer.music.load("C:\pp2\Lab 7\music\\" + songs[index]) 

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p:
                  pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                  if playingMusic == False: 
                        pygame.mixer.music.unpause() 
                        playingMusic = True 
                  elif playingMusic == True:
                        pygame.mixer.music.pause()
                        
            elif event.key == pygame.K_LEFT and index == 0: 
                  pygame.mixer.music.load("C:\pp2\Lab 7\music\\" + songs[len(songs) - 1]) 
                  pygame.mixer.music.play() 
                  index = len(songs) - 1 
            elif event.key == pygame.K_LEFT and index != 0: 
                  pygame.mixer.music.load("C:\pp2\Lab 7\music\\" + songs[index - 1]) 
                  pygame.mixer.music.play() 
                  index -= 1 
            elif event.key == pygame.K_RIGHT and index == len(songs) - 1: 
                  pygame.mixer.music.load("C:\pp2\Lab 7\music\\" + songs[0]) 
                  pygame.mixer.music.play() 
                  index = 0 
            elif event.key == pygame.K_RIGHT and index != len(songs) - 1: 
                  pygame.mixer.music.load("C:\pp2\Lab 7\music\\" + songs[index + 1]) 
                  pygame.mixer.music.play() 
                  index =+ 1
 
        screen.blit(background, (0, 0)) 
    pygame.display.update()

pygame.quit()