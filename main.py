import pygame
import bevegelse 
import combat
import collect
pygame.init()

state = "bev"

while True:
    print('a')
    if state == "bev":
        state = bevegelse.run_bev()
    elif state == "col":
        state = collect.run_col()
        
    elif state == "com":
        state = combat.run_com()
    elif state == "quit":
        break

pygame.quit()