import pygame
import sys
import random
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
print('sknskje') 
alien = pygame.image.load('images/elien.png')
background = pygame.image.load('images/ship_big.png')
ufo = pygame.image.load('images/gfo.png')
ufo2 =pygame.transform.scale(ufo, (232, 112))
alien_rect = alien.get_rect()
ufo_rect = ufo2.get_rect()





beam = pygame.image.load('images\Big_beam.png')
ufo = pygame.image.load('images\cig_aufo.gif')
# Square
size = 192
x = -size
y = 100
speed = 3
level='bev'






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
        color = red
        

        text_surf = font.render(self.text, True, (0,0,0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

class human:
    def __init__(self,name,move1,move2,move3,move4,phealth,image):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.phealth = phealth
        self.image =  pygame.image.load(image)

class enemy:
    def __init__(self,name,damage,ehealth,image):
        self.name = name
        self.damage = damage
        self.ehealth = ehealth
        self.image =  pygame.image.load(image)


enemys = [
    enemy('buff',20,225,'images/enemybuff.png'),
    enemy('fat',20,225,'images/enemyfat.png'),
    enemy('human',20,225,'images/enemyhuman.png'),
    enemy('mutant',20,225,'images/enemymutant.png'),
    enemy('slim',20,225,'images/enemyslim.png')
]     

humans = [
    human('cow','Milksplash','Moo','Blind','Drink milk',125,'images/humancow.png'),
    human('suit','Moneyspread','Bag throw','Punch','Block',175,'images/humansuit.png'),
    human('nerd','Fall down','Super jump','Dodge','Power up',150,'images/human2.png'),
    human('hoodie','Stab','Slash','Punch','Hide',225,'images/humanhoodie.png'),
    human('fire','Axe chop','Slash','Fireball','Block',250,'images/humanfire.png'),
    human('human','Punch','Kick','Dodge','Block',200,'images/human.png')
]
player = humans[0]  # cow
enemy1 = enemys[0]  # buff
# Create buttons
buttons = [
    Button(player.move1, 905, 500, 129*2, 65*2),
    Button(player.move2, 905, 625, 129*2, 65*2),
    Button(player.move3, 650, 500, 129*2, 65*2),
    Button(player.move4, 650, 625, 129*2, 65*2)
]
te = 100
angle = 0
g=3
phealth= 200
poison=0
k=5






# Game loop
while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

        wall1 = pygame.Rect(675, 0, 240, 175)
        wall2 = pygame.Rect(250, 0, 240, 175)
        door = pygame.Rect(500, 0, 168, 10)
    





        if level=='bev':
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

#---------------------------------------------------------------------------------
# collection
#---------------------------------------------------------------------------------

        elif level=='col': 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print('nei')
                current_image = beam
                y=100
            elif keys[pygame.K_r]:
                level="bev"
            else:
                y=42
                current_image= ufo
                x += speed
                if x > 1010:
                    speed=speed*-1
                elif x< 0:
                    speed=3

#---------------------------------------------------------------------------------
# combat
#---------------------------------------------------------------------------------
        elif level=="com":
            healthbar=pygame.Rect(200, 150, te*2, 50)
       
        
            for i in range(3):
                if te<=0:
                    te=0
                    g=g-1
                    if g>0:
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
        

    
  

    # Keep square on screen
        playerpos.x = max(0, min(WIDTH - alien.get_width(), playerpos.x))
        playerpos.y = max(0, min(HEIGHT - alien.get_height(), playerpos.y))

    
    # Drawing
        screen.fill((150, 150, 150))  # background
        if level =='bev':
            pygame.draw.rect(screen, (0,200,255), wall1)
            pygame.draw.rect(screen, (0,200,255), wall2)
            pygame.draw.rect(screen, (0,200,255), wall1)
            screen.blit(background, (0,0))
            screen.blit(alien, (playerpos.x,playerpos.y))
            screen.blit(ufo2, (90,300))

       
        if level=="col":
            screen.blit(current_image,(x,y))
        if level=="com":
          
            screen.blit(player.image, (100, 400))  
            screen.blit(enemy1.image, (800, 400))
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
    
        if alien_rect.colliderect(door):
           level="com"
        elif alien_rect.colliderect(ufo_rect):
           level="col"
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
                level='bev'
                playerpos.x = 600
                playerpos.y = 400

   
        pygame.display.flip()
        clock.tick(60)
