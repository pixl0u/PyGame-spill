import pygame
import sys
import random
# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 798
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Human fighter ultra deluxe+++")

# Clock
clock = pygame.time.Clock()

# Square settings
square_size = 64
playerpos = pygame.math.Vector2(550, 350)
speed = 5
print('sknskje') 
alien = pygame.image.load('images/alien_front.png')
ship = pygame.image.load('images/ship_big.png')
ufo = pygame.image.load('images/gfo.png')
ufo2 =pygame.transform.scale(ufo, (232, 112))
alien_rect = alien.get_rect()
ufo_rect = ufo2.get_rect()

beam = pygame.image.load('images\Big_beam.png')
ufo = pygame.image.load('images\cig_aufo.gif')
sign = pygame.image.load('images/sign.png')

background1 = pygame.image.load('images/bev_back.png').convert_alpha()
background2 = pygame.image.load('images/col_back.png').convert_alpha()
grass = pygame.image.load('images/grass.png').convert_alpha()
background3 = pygame.image.load('images/com_back.png').convert_alpha()
background4 = pygame.image.load('images/win_and_lose.png').convert_alpha()

beam_rect=beam.get_rect()
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
    def __init__(self,name,move1,move2,move3,move4,phealth,u,i,image):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.phealth = phealth
        self.u = u
        self.i = i
        self.image =  pygame.image.load(image)

class enemy:
    def __init__(self,name,damage,ehealth,image):
        self.name = name
        self.damage = damage
        self.ehealth = ehealth
        self.image =  pygame.image.load(image)


enemys = [
    enemy('buff',25,225,'images/enemybuff.png'),
    enemy('fat',15,275,'images/enemyfat.png'),
    enemy('human',20,200,'images/enemyhuman.png'),
    enemy('mutant',20,230,'images/enemymutant.png'),
    enemy('slim',10,125,'images/enemyslim.png')
]     

humans = [
    human('cow','Milksplash','Milkshot','Moo','Drink milk',135,100,674,'images/humancow.png'),
    human('suit','Slap','Bag charge','Moneyspread','Block',185,300,674,'images/humansuit.png'),
    human('nerd','Trip','Super jump','Dodge','Power up',160,500,674,'images/human2.png'),
    human('hoodie','Punch','Slash','Dodge','Stab',235,700,674,'images/humanhoodie.png'),
    human('fire','Axe chop','Slash','Fireball','Block',260,900,674,'images/humanfire.png'),
    human('human','Punch','Kick','Dodge','Block',210,1100,674,'images/human.png')
]

pickup1 = humans[0] 
pickup2 = humans[1] 
pickup3 = humans[2] 
pickup4 = humans[3] 
pickup5 = humans[4] 
pickup6 = humans[5] 

fiende1 = enemys[0]
fiende2 = enemys[1]
fiende3 = enemys[2]
fiende4 = enemys[3]
fiende5 = enemys[4]

pickups = [pickup1,pickup2,pickup3,pickup4,pickup5,pickup6]

player = humans[5] 
enemy = enemys[0]  
# Create buttons

enemy = random.choice(enemys)
  


angle = 0
g=3
phealth= player.phealth
ehealth = enemy.ehealth
bleed=0
bleeding=5
timer = 1


width = player.image.get_width() * 2
height = player.image.get_height() * 2


width = enemy.image.get_width() * 2
height = enemy.image.get_height() * 2

cooldown_max = 30   
cooldown_counter = 0
active_pickups = random.sample(pickups, 3)
# Game loop
while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        buttons = [
            Button(player.move1, 905, 500, 129*2, 65*2),
            Button(player.move2, 905, 625, 129*2, 65*2),
            Button(player.move3, 650, 500, 129*2, 65*2),
            Button(player.move4, 650, 625, 129*2, 65*2)
        ]
        wall1 = pygame.Rect(675, 0, 240, 175)
        wall2 = pygame.Rect(250, 0, 240, 175)
        door = pygame.Rect(500, 0, 168, 10)

       

        if level=='bev':
            speed=3
            alien_rect.x = playerpos.x
            alien_rect.y = playerpos.y

            ufo_rect.x = 90
            ufo_rect.y = 300
    # Key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                alien= pygame.image.load('images/alien_left.png')
                playerpos.x -= speed
                if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
                    playerpos.x += 20
            if keys[pygame.K_d]:
                alien= pygame.image.load('images/alien_right.png')
                playerpos.x += speed
                if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
                    playerpos.x -= 20
            if keys[pygame.K_w]:
                alien= pygame.image.load('images/alien_back.png')
                playerpos.y -= speed
                if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
                    playerpos.y += 20
            if keys[pygame.K_s]:
                alien= pygame.image.load('images/alien_front.png')
                playerpos.y += speed
                if alien_rect.colliderect(wall1) or alien_rect.colliderect(wall2):
                    playerpos.y -= 20

#---------------------------------------------------------------------------------
# collection
#---------------------------------------------------------------------------------

        elif level=='col': 
            keys = pygame.key.get_pressed()
          

            beam_rect.x = x  
            beam_rect.y = y



            if keys[pygame.K_SPACE]:
                current_image = beam
                y=100
                for pickup in  active_pickups[:]:
                    pickup_rect = pickup.image.get_rect(topleft=(pickup.u, pickup.i))
                    if beam_rect.colliderect(pickup_rect):         
                        print(f'{pickup.name}')
                        player=pickup
                        active_pickups.remove(pickup)
                        

            elif keys[pygame.K_r]:
                active_pickups = random.sample(pickups, 3)
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
            healthbar=pygame.Rect(630, 70, ehealth*2, 50)
            healthbar2=pygame.Rect(75, 630, phealth*2, 50)
            player_scaled = pygame.transform.scale(player.image, (width, height))
            enemy_scaled = pygame.transform.scale(enemy.image, (width, height))
            if phealth<=0:
                phealth =0
            for i in range(3):
                
                if ehealth<=0:
                   
                    ehealth=0
                    g=g-1
                    if g>0:
                        enemy = random.choice(enemys)
                        ehealth = enemy.ehealth
                        phealth +=35
                    
                if phealth<=0 or g==0:
                            if phealth<=0:
                                print('du tapte')
                                level='lose'
                                
                            elif g==0:
                                print('du vant')
                                level='win'
                                



            if cooldown_counter > 0:
                cooldown_counter -= 1   
                timer = 0
            else:
                timer = 1           
        
        
        #knappene
            for button in buttons:
           
                if button.clicked(event):
                        if timer == 1 :
                            cooldown_counter = cooldown_max 
                            crit=random.randint(1,100)
                            if crit > 95:
                                print (f"{crit} crit")
                                print(f"{button.text} clicked!")
                            if bleed==1:
                                bleeding -=1     
                                ehealth -= 30
                            if bleeding<=0:
                                bleed=0
                       
                        
                            damage=enemy.damage
                            if g>0:
                                phealth=phealth-damage
                            if button.text == 'Punch' or button.text =='Slap':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                        ehealth-=40
                                    else:
                                        ehealth -= 25
                                if angle==270:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,270-angle)
                                    angle = 270
                                print(ehealth)
                            elif button.text == 'Axe chop' or button.text == 'Milksplash':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                else:
                                    if crit >=95:
                                        ehealth -= 60
                                    else:
                                        ehealth -= 40
                                if angle==270:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,270-angle)
                                    angle = 270
                                print(ehealth)
                            elif button.text == 'Trip':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                else:
                                    if crit >=95:
                                        phealth -= 10
                                    else:
                                        phealth -= 5
                                if angle==270:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,270-angle)
                                    angle = 270
                                print(ehealth)
                            
                            elif button.text == 'Block':
                                    if ehealth<=0:
                                        print(f"{ehealth} Health")
                                
                                    else:
                                        phealth=phealth+damage
                                    if angle==90:
                                        mid = pygame.transform.rotate(mid,0)
                                    else:
                                        mid = pygame.transform.rotate(mid,90-angle)
                                        angle = 90
                                    print(f"{ehealth} Health")
                            elif button.text == 'Drink milk':
                                    if ehealth<=0:
                                        print(f"{ehealth} Health")
                                
                                    else:
                                        if phealth > 300:
                                            phealth += damage
                                        else:
                                            phealth=phealth+(damage*2)
                                    if angle==90:
                                        mid = pygame.transform.rotate(mid,0)
                                    else:
                                        mid = pygame.transform.rotate(mid,90-angle)
                                        angle = 90
                                    print(f"{ehealth} Health")
                            elif button.text == 'Stab' or button.text== 'Power up':
                                    if ehealth<=0:
                                        print(f"{ehealth} Health")
                                    else:
                                        ehealth -= 20
                                        bleeding=5
                                        bleed=1
                                    if angle==360:
                                        mid = pygame.transform.rotate(mid,0)
                                    else:
                                        mid = pygame.transform.rotate(mid,90-angle)
                                        angle = 90
                                    print(f"{ehealth} Health")

                            elif button.text == 'Slash' or button.text =='Kick':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=80:
                                        ehealth-= 40
                                    else:
                                        ehealth -= 25
                                if angle==180:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,180-angle)
                                    angle = 180
                                print(ehealth)
                            elif button.text == 'Super jump' or button.text == 'Milkshot':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                        ehealth-=30
                                        if enemy.damage > 5:
                                            enemy.damage -= 5
                                    else:
                                        ehealth -= 15
                                        if enemy.damage > 5:
                                            enemy.damage -= 3
                                if angle==180:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,180-angle)
                                    angle = 180
                                print(ehealth)
                            elif button.text == 'Moneyspread' or button.text == 'Moo':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                        ehealth-=70
                                      
                                    else:
                                        ehealth -= 10
                                      
                                if angle==360:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,360-angle)
                                    angle = 360
                                print(ehealth)
                            
                            elif button.text == 'Fireball':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                        ehealth-=60
                                        bleeding=2
                                        bleed=1
                                    else:
                                        ehealth -= 40
                                        bleeding=2
                                        bleed=1
                                if angle==360:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,360-angle)
                                    angle = 360
                                print(ehealth)
                            elif button.text == 'Bag charge':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                       player.move2 = 'Bag throw'
                                       phealth = phealth + (damage-5)
                                    else:
                                        player.move2 = 'Bag throw'
                                        print(player.move2)
                                if angle==180:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,180-angle)
                                    angle = 180
                                print(ehealth)
                            elif button.text == 'Bag throw':
                            
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=95:
                                       ehealth-=100
                                       player.move2 = 'Bag charge'
                                    else:
                                        player.move2 = 'Bag charge'
                                        ehealth-=70
                                if angle==180:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,180-angle)
                                    angle = 180
                                print(ehealth)
                            elif button.text == 'Dodge':
                                if ehealth<=0:
                                    print(f"{ehealth} Health")
                                
                                else:
                                    if crit >=70:
                                      pass
                                    else:
                                        phealth += (damage-5)
                                        ehealth -= 10
                                        
                                if angle==360:
                                    mid = pygame.transform.rotate(mid,0)
                                else:
                                    mid = pygame.transform.rotate(mid,360-angle)
                                    angle = 360
                                print(ehealth)
        elif level == 'win' or level == 'lose':
            pass
  

    # Keep square on screen
        playerpos.x = max(0, min(WIDTH - alien.get_width(), playerpos.x))
        playerpos.y = max(0, min(HEIGHT - alien.get_height(), playerpos.y))

    
    # Drawing
        screen.fill((200,200,200))
        if level =='bev':
            
            pygame.draw.rect(screen, (0,200,255), wall1)
            pygame.draw.rect(screen, (0,200,255), wall2)
            pygame.draw.rect(screen, (0,200,255), wall1)
            screen.blit(background1,(0,0))
            screen.blit(ship, (0,0))
            screen.blit(alien, (playerpos.x,playerpos.y))
            screen.blit(ufo2, (90,300))
            screen.blit(sign, (85,450))

       
        if level=="col":
            screen.blit(background2,(0,0))
            col_text = font.render(
                f'Press space to pick up, press Esc to return',
                True,
                (0,0,0)
            )
            screen.blit(col_text, ((0, 0)))
            screen.blit(current_image,(x,y))
            for pickup in active_pickups:
                screen.blit(pickup.image, (pickup.u, pickup.i))
            screen.blit(grass,(0,0))
            
          
             
        if level=="com":
            screen.blit(background3,(0,0))
            screen.blit(player_scaled, (150, 385))  
            screen.blit(enemy_scaled, (800, 295))
            screen.blit(top,(905,500))
            screen.blit(top2,(650,500))
            screen.blit(bot,(905,625))
            screen.blit(bot2,(650,625))
            screen.blit(mid,(892,614))
            text = font.render(
                f'Enemy health {ehealth}',
                True,
                (0, 0, 0)
            )
           
            screen.blit(text, (630, 135))
            text2 = font.render(
                f'Your health {phealth}',
               True, 
                (0, 0, 0)
            )
            screen.blit(text2,(75,715))
            pygame.draw.rect(screen,red,healthbar)
            pygame.draw.rect(screen,red,healthbar2)
            for button in buttons:
                button.draw(screen)

        if level == 'win':
            screen.blit(background4,(0,0))
            wtext = font.render(
                f'You won',
               True, 
                (255, 255, 255)
            )
            screen.blit(wtext,(500,375))
        elif level == 'lose':
            screen.blit(background4,(0,0))
            ltext = font.render(
                f'You lost',
               True, 
                (255, 255, 255)
            )
            screen.blit(ltext,(500,375))

    
        if alien_rect.colliderect(door) and level not in ('win', 'lose'):
           level="com"
        elif alien_rect.colliderect(ufo_rect) and level not in ('win', 'lose'):
            level="col"
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and level not in ('win', 'lose'): 
                active_pickups = random.sample(pickups, 3)
                level='bev'
                playerpos.x = 550
                playerpos.y = 350

   
        pygame.display.flip()
        clock.tick(60)
