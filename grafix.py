#Globals
import pygame
red = (255,0,0)
green = (0, 255, 0)
blue = (0,0,255)

#Func

def deRGB(c):
    if len(c) != 3:
        print("INVALID INPUT TO RGBIFY (MUST BE 3 LENGTH TUPLE)")
    else:
        try:
            modifier = 120
            Cc = list(c)
            for i in range(0,3):
                if Cc[i] < modifier:
                    Cc[i] = 0
                else:
                    Cc[i] -= modifier
            Cc = tuple(Cc)
            return Cc
        except:
            print("INVALID INPUT TO RGBIFY (INVALID ARGUMENTS MUST BE INTEGERS > 0)")

def draw_grid(screen,offset,grid_size,colour):
    #colour will be BG colour, change to differentiate
    colour = deRGB(colour)
    print(colour)
    x = round((screen.get_width()-offset)/grid_size)
    y = round((screen.get_height() - offset)/grid_size)
    for i in range(0,x+1):
        pygame.draw.line(screen, colour, ((offset-1+(i*grid_size)),0),((offset-1+(i*grid_size)),screen.get_height()-offset))
    for i in range(0,y+1):
        pygame.draw.line(screen, colour, (offset,i*grid_size),(screen.get_width(),i*grid_size) )


def draw_candle(screen,x,y,scale,candleData):
    #candleData format must be {"open":x,"close":y,"high":z,"low":a} close being current val if most recent candle
    increments = 9
    if candleData["close"] < candleData["open"]:
        colour = red
    else:
        colour = green
    candleWidthFactor = 9
    candleHeightFactor = candleWidthFactor*2
    rect_width, rect_height = (candleWidthFactor, candleHeightFactor)*scale
    rect_x, rect_y = x,y#screen_width / 2 - rect_width / 2, screen_height / 2 - rect_height / 2
    if colour == green:
        hi = candleData["high"]-candleData["close"]
    else:
        hi = candleData["high"]-candleData["open"]
    hi = hi*increments
    pygame.draw.line(screen, colour, (x+((candleWidthFactor*scale)/2),y), (x+((candleWidthFactor*scale)/2),y-(hi)) )
    pygame.draw.rect(screen, colour, pygame.Rect(rect_x, rect_y, rect_width, rect_height))  # Draw rectangle


def draw_candle_chart(width,height):
    pygame.init()
    # Set screen
    screen_width, screen_height = width,height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Grafix")

    increments = 9
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #######################################

            draw_grid(screen,64,8,blue)

            draw_candle(screen,50,50,1,{"open":2,"close":3,"high":4,"low":0})

            #######################################
            # Update the display
            pygame.display.flip()


    # Quit Pygame
    pygame.quit()