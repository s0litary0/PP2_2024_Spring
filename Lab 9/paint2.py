import pygame

#creating rectangle on 'screen' surface with 'color' color
def setRectangle(x1, y1, x2, y2, screen, color):
    x_init = min(x1, x2)
    y_init = min(y1, y2)
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    pygame.draw.rect(screen, color, (x_init, y_init, x, y), 1)
#creating square on 'screen' surface with 'color' color
def setSquare(x1, y1, x2, y2, screen, color):
    x_init = min(x1, x2)
    y_init = min(y1, y2)
    length = min(abs(x2 - x_init), abs(y2 - y_init))
    pygame.draw.rect(screen, color, (x_init, y_init, length, length), 1)

#creating right triangle on 'screen' surface with 'color' color
def setRightTriangle(x1, y1, x2, y2, screen, color):
    pygame.draw.line(screen, color, (x1, y1), (x1, y2))
    pygame.draw.line(screen, color, (x1, y2), (x2, y2))
    pygame.draw.line(screen, color, (x1, y1), (x2, y2))
#creating equilateral triangle on 'screen' surface with 'color' color
def setEquilateralTriangle(x1, y1, x2, y2, screen, color):
    pygame.draw.line(screen, color, ((x2 - x1) / 2 + x1, y1), (x1, y2))
    pygame.draw.line(screen, color, ((x2 - x1) / 2 + x1, y1), (x2, y2))
    pygame.draw.line(screen, color, (x1, y2), (x2, y2))
#creating rhombus on 'screen' surface with 'color' color
def setRhombus(x1, y1, x2, y2, screen, color):
    pygame.draw.line(screen, color, (x1 + (x2 - x1) / 2, y1), (x1, y1 + (y2 - y1) / 2))
    pygame.draw.line(screen, color, (x1 + (x2 - x1) / 2, y1), (x2, y1 + (y2 - y1) / 2))
    pygame.draw.line(screen, color, (x1 + (x2 - x1) / 2, y2), (x1, y1 + (y2 - y1) / 2))
    pygame.draw.line(screen, color, (x1 + (x2 - x1) / 2, y2), (x2, y1 + (y2 - y1) / 2))
#creating circle on 'screen' surface with 'color' color
def setCircle(x1, y1, x2, y2, screen, color):
    radius = abs(x1 + y1 - x2 - y2) / 4
    pygame.draw.circle(screen, color, (x1 + radius, y1 + radius), radius, 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    layer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 18)
    binds = font.render("Colors: 1 - Red, 2 - Green, 3 - Blue, 4 - Black", True, "Black")
    
    currentDrawingShape = "Rectangle"
    cur_shape = font.render(currentDrawingShape, True, "Black")
    mode = 'Black'
    x_start = 0
    y_start = 0
    cur_x = x_start
    cur_y = y_start
    i = 0
    
    tools = ["Rectangle", "Square", "Circle", "Line", "RightTriangle", "EquilateralTriangle", "Rhombus"]
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
                elif event.key == pygame.K_RIGHT:
                    i += 1
                    if i == len(tools): i = 0
                    currentDrawingShape = tools[i]
                    cur_shape = font.render(currentDrawingShape, True, "Black")
                elif event.key == pygame.K_LEFT:
                    i -= 1
                    if i == -1: i = len(tools) - 1
                    currentDrawingShape = tools[i]
                    cur_shape = font.render(currentDrawingShape, True, "Black")
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
                            setRectangle(x_start, y_start, cur_x, cur_y, screen, mode)
                        
                        elif currentDrawingShape == "Square":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            setSquare(x_start, y_start, cur_x, cur_y, screen, mode)

                        elif currentDrawingShape == "Rhombus":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            setRhombus(x_start, y_start, cur_x, cur_y, screen, mode)
                        
                        elif currentDrawingShape == "RightTriangle":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            setRightTriangle(x_start, y_start, cur_x, cur_y, screen, mode)
                        
                        elif currentDrawingShape == "EquilateralTriangle":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            setEquilateralTriangle(x_start, y_start, cur_x, cur_y, screen, mode)
                        
                        elif currentDrawingShape == "Circle":
                            screen.blit(layer, (0, 0))
                            cur_x = event.pos[0]
                            cur_y = event.pos[1]
                            setCircle(x_start, y_start, cur_x, cur_y, screen, mode)
                        
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
        pygame.draw.rect(screen, "White", (0, 432, 160, 60))
        screen.blit(cur_shape, (0, 450))
        pygame.display.flip()
        
        clock.tick(60)
    
main()