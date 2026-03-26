import pygame
import sys


pygame.init()

# Screen
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Square")
clock = pygame.time.Clock()

# Colors
BACKGROUND = (125, 125, 125)
SQUARE_COLOR = (0, 200, 255)
beam = pygame.image.load('images\Big_beam.png')
ufo = pygame.image.load('images\cig_aufo.gif')
# Square
size = 192
x = -size
y = 100
speed = 3

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    # Animate movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('nei')
        current_image = beam
        y=100
    elif keys[pygame.K_r]:
       pass
    else:
        y=42
        current_image= ufo
        x += speed
        if x > 1010:
         speed=speed*-1
        elif x< 0:
            speed=3
        
   

    # Draw
    screen.fill(BACKGROUND)
    screen.blit(current_image,(x,y))
 

    pygame.display.flip()
    clock.tick(60)
