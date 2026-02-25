import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square")

# Clock
clock = pygame.time.Clock()

# Square settings
square_size = 64
playerpos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
speed = 5

alien = pygame.image.load('images\elien.png')
background = pygame.image.load('images\ship_big.png')
ufo = pygame.image.load('images\gfo.png')
ufo2 =pygame.transform.scale(ufo, (232, 112))
alien_rect = alien.get_rect()
ufo_rect = ufo2.get_rect()
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    alien_rect.x = playerpos.x
    alien_rect.y = playerpos.y

    ufo_rect.x = 90
    ufo_rect.y = 300
    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerpos.x -= speed
        if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
            playerpos.x += 20
    if keys[pygame.K_d]:
        playerpos.x += speed
        if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
            playerpos.x -= 20
    if keys[pygame.K_w]:
        playerpos.y -= speed
        if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
            playerpos.y += 20
    if keys[pygame.K_s]:
        playerpos.y += speed
        if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
            playerpos.y -= 20
    

    


    # Keep square on screen
    playerpos.x = max(0, min(WIDTH - alien.get_width(), playerpos.x))
    playerpos.y = max(0, min(HEIGHT - alien.get_height(), playerpos.y))

    
    # Drawing
    screen.fill((150, 150, 150))  # background
    door=pygame.draw.rect(
        screen,
        (0, 200, 255),
        (500, 0, 168, 10)
    )
    wall1=pygame.draw.rect(
        screen,
        (0, 200, 255),
        (675, 0, 240, 175)
    )
    wall2=pygame.draw.rect(
        screen,
        (0, 200, 255),
        (250, 0, 240, 175)
    )
    screen.blit(background, (0,0))
    screen.blit(alien, (playerpos.x,playerpos.y))
    screen.blit(ufo2, (90,300))
    
   
   
    
    if alien_rect.colliderect(door) or alien_rect.colliderect(ufo_rect):
        print("Collision with one of them!")
    
   
    pygame.display.flip()
    clock.tick(60)
