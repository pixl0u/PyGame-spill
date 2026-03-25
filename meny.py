import pygame
import sys
import random
pygame.init()

# Screen
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("6️⃣7️⃣🤥")
clock = pygame.time.Clock()

# Colors
BG_COLOR = (150, 150, 150)
BUTTON_COLOR = (70, 130, 180)
HOVER_COLOR = (100, 170, 220)
TEXT_COLOR = (0, 0, 0)
top = pygame.image.load('images/top_right.png')
top2 = pygame.image.load('images/top_left.png')
bot = pygame.image.load('images/bottom_right.png')
bot2 = pygame.image.load('images/bottom_left.png')
mid = pygame.image.load('images/middle.png')
# Font
font = pygame.font.Font('images/HomeVideo-BLG6G.ttf', 34)

red=(255,0,0)
# Button class
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surface):
        color = HOVER_COLOR if self.rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        

        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

# Create buttons
buttons = [
    Button("Stab", 905, 500, 129*2, 65*2),
    Button("Slice", 905, 625, 129*2, 65*2),
    Button("Poison", 650, 500, 129*2, 65*2),
    Button("Sheild", 650, 625, 129*2, 65*2)
]
te = 100
angle = 0
x=3
phealth= 200
poison=0
k=5
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #healthbar.width = pygame.math.lerp(healthbar.width,te,0.1)
        #healthbar=pygame.Rect(200, 150, healthbar.width, 50)
        healthbar=pygame.Rect(200, 150, te*2, 50)
       
        
        for i in range(3):
            if te<=0:
                te=0
                x=x-1
                if x>0:
                    new_health=random.randint(100,300)
                    te=new_health
                    phealth=phealth+50
              
        
        
        #knappene kinda
        for button in buttons:
           
            if button.clicked(event):
                crit=random.randint(1,100)
                print (f"{crit} crit")
                print(f"{button.text} clicked!")
                if poison==1:
                    k=k-1     
                    te=te-10
                    if k<=0:
                        poison=0
                if phealth<=0 or x==0:
                    if phealth<=0:
                        print('du tapte')
                    elif x==0:
                        print('du vant')
                else:
                    damage=random.randint(1,10)
                    phealth=phealth-damage
                    if button.text == 'Stab':
                        if te<=0:
                            print(f"{te} Health")
                        else:
                            if crit >=95:
                                te=te-30
                            else:
                                te = te - 15
                        if angle==270:
                            mid = pygame.transform.rotate(mid,0)
                        else:
                            mid = pygame.transform.rotate(mid,270-angle)
                            angle = 270
                        print(te)
                    
                    elif button.text == 'Slice':
                        if te<=0:
                            print(f"{te} Health")
                        else:
                            if crit >=95:
                                te=te-20
                            else:
                                te = te - 10
                        if angle==180:
                            mid = pygame.transform.rotate(mid,0)
                        else:
                            mid = pygame.transform.rotate(mid,180-angle)
                            angle = 180
                        print(f"{te} Health")
                    elif button.text == 'Poison':
                        if te<=0:
                            print(f"{te} Health")
                        else:
                            k=5
                            poison=1
                        if angle==360:
                            mid = pygame.transform.rotate(mid,0)
                        else:
                            mid = pygame.transform.rotate(mid,360-angle)
                            angle = 360
                        print(f"{te} Health")
                    elif button.text == 'Sheild':
                        if te<=0:
                            print(f"{te} Health")
                        else:
                           phealth=phealth+damage
                        if angle==90:
                            mid = pygame.transform.rotate(mid,0)
                        else:
                            mid = pygame.transform.rotate(mid,90-angle)
                            angle = 90
                        print(f"{te} Health")
           
   

   
    # Draw
    screen.fill(BG_COLOR)
    screen.blit(top,(905,500))
    screen.blit(top2,(650,500))
    screen.blit(bot,(905,625))
    screen.blit(bot2,(650,625))
    screen.blit(mid,(892,614))
    text = font.render(
        f'health {te}',
        True,
        (255, 255, 255)
    )
    screen.blit(text, (400, 500))
    text1 = font.render(
        f'{angle}',
        True,
        (255, 255, 255)
    )
    screen.blit(text1, (400, 400))
    text2 = font.render(
        f'{phealth}',
        True,
        (255, 255, 255)
    )
    screen.blit(text2,(400,300))
    pygame.draw.rect(screen,red,healthbar)
    for button in buttons:
     button.draw(screen)

    pygame.display.flip()
    clock.tick(60)
