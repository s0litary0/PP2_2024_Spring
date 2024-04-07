import pygame

def setRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    x2 = abs(x1 - x2)
    y2 = abs(y1 - y2)
    return (x, y, x2, y2)

def setCircle(x1, y1, x2, y2):
    radius = abs(x1 + y1 - x2 - y2) / 4
    return [(x1 + radius, y1 + radius), radius]


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    layer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 14)
    binds = font.render("Colors: 1 - Red, 2 - Green, 3 - Blue, 4 - Black Shapes: r - Rectangle, c - Circle, l - Line, e - Eraser", True, "Black")

    mode = 'black'
    x_start = 0
    y_start = 0
    cur_x = x_start
    cur_y = y_start
    currentDrawingShape = None
    MouseDown = False

    layer.fill((255, 255, 255))
    screen.fill((255, 255, 255))

    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            # determin if X was clicked
            if event.type == pygame.QUIT:
                return
                # determine if a key was pressed
            if event.type == pygame.KEYDOWN:    
                #sets 1, 2, 3, 4 keys for changing color
                if event.key == pygame.K_1:
                    mode = 'red'
                elif event.key == pygame.K_2:
                    mode = 'green'
                elif event.key == pygame.K_3:
                    mode = 'blue'
                elif event.key == pygame.K_4:
                    mode = 'black'
                
                #sets r and c keys for choosing shape to draw (rectangle, circle or line)
                elif event.key == pygame.K_r:
                    currentDrawingShape = "Rectangle"
                elif event.key == pygame.K_c:
                    currentDrawingShape = "Circle"
                elif event.key == pygame.K_l:
                    currentDrawingShape = "Line"
                #choose eraser
                elif event.key == pygame.K_e:
                    currentDrawingShape = "Eraser"
                #start of drawing position
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left click
                    cur_x = event.pos[0]
                    cur_y = event.pos[1]
                    x_start = cur_x
                    y_start = cur_y
                    MouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    MouseDown = False
                    layer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                    if MouseDown == True:
                        if currentDrawingShape == "Rectangle":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            pygame.draw.rect(screen, mode, setRectangle(x_start, y_start, cur_x, cur_y), 1)
                        
                        elif currentDrawingShape == "Circle":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            pygame.draw.circle(screen, mode, setCircle(x_start, y_start, cur_x, cur_y)[0], setCircle(x_start, y_start, cur_x, cur_y)[1], 1)
                        
                        elif currentDrawingShape == "Line":
                            x_start = cur_x
                            y_start = cur_y
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            pygame.draw.line(screen, mode, (x_start, y_start), (cur_x, cur_y))
                        
                        elif currentDrawingShape == "Eraser":
                            x_start = cur_x
                            y_start = cur_y
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            pygame.draw.line(screen, (255, 255, 255), (x_start, y_start), (cur_x, cur_y), 50)
        
        screen.blit(binds, (0, 0))
        pygame.display.flip()
        
        clock.tick(60)
    
main()