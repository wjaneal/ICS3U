import pygame
from os import path
import random

WIDTH=300
HEIGHT=500
FPS=30

img_dir=path.join(path.dirname(__file__))
'''pygame error:

if doesn't work, change to this:
img_dir=path.join(path.dirname(__file__),"GitHub/ICS3U/JAKA/Angel")'''

#define colors
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
YELLOW=(255,255,0)

#define font
font_name=pygame.font.match_font("arial")
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,WHITE)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
    
#let rain fall
def newrain():
    r=Rain()
    all_sprites.add(r)
    drops.add(r)
    
#define pct and display
def draw_shield_bar(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGTH=100
    BAR_HEIGHT=10
    fill=(pct/100)*BAR_LENGTH
    outline_rect=pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)
    
#define heart and display
def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect=img.get_rect()
        img_rect.x= x + 30 * i
        img_rect.y= y
        surf.blit(img,img_rect)
        
#define start/end screen
def show_go_screen():
    screen.blit(background,background_rect)
    draw_text(screen,"Haaa",64,WIDTH/2,HEIGHT/4)
    draw_text(screen,"collect blue and avoid yellow",22,WIDTH/2,HEIGHT/2)
    draw_text(screen,"miss one blue drop = -10 blood",22,WIDTH/2,HEIGHT/2+25)
    draw_text(screen,"1 life = 100 blood",22,WIDTH/2,HEIGHT/2+50)
    draw_text(screen,"mouse to move",18,WIDTH/2,HEIGHT*3/4-20)
    draw_text(screen,"Press a key to begin",18,WIDTH/2,HEIGHT*3/4)
    pygame.display.flip()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYUP:
                waiting=False
                
#define rain and bullet
def level_up():
        for i in range(20):
                newrain()
                if random.random()<0.1:
                    b=Bullet()
                    all_sprites.add(b)
                    bullets.add(b)
            

#player img and update
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,50))
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.radius=25
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx=WIDTH/2
        self.rect.bottom =HEIGHT-10
        self.speedx=0
        self.shield=100
        self.lives=3
        #self.hidden=False
        #self.hide_timer=pygame.time.get_ticks()
        
    def update(self):
        self.speedx=0

        pos=pygame.mouse.get_pos()
        self.rect.midtop=pos
        '''if press key to move, code is here:
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-10
        if keystate[pygame.K_RIGHT]:
            self.speedx=10'''

        '''self.rect.x+=self.speedx'''
       
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
        if self.rect.top<450:
            self.rect.top=450

        '''#unhide if hidden
        if self.hidden and pygame.time.get_ticks()-self.hide_timer>1000:
            self.hidden=False
            self.rect.centerx=WIDTH/2
            self.rect.bottom=HEIGHT-10'''

    '''def hide(self):
        self.hidden=True
        self.hide_timer=pygame.time.get_ticks()
        self.rect.center=(WIDTH/2,HEIGHT+200)'''
    
#define rain and update        
class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image, BLUE,self.rect.center,self.radius)
        self.rect.x=random.randrange((WIDTH-self.rect.width)/10)*10
        self.rect.y=random.randrange(-100,0)*30
        self.speedy=level
      
    def update(self):
        
        self.rect.y+=self.speedy
        if self.rect.top>HEIGHT+10:
            self.rect.x=random.randrange((WIDTH-self.rect.width)/10)*10
            self.rect.y=random.randrange(-100,0)*30
            self.speedy=level
        if self.rect.bottom>HEIGHT:
            self.kill()
            player.shield-=10
            
#define bullet and update
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width/2)
        self.rect.bottom=random.randrange(-2000,0)
        self.rect.centerx=random.randrange((WIDTH-self.rect.width)/10)*10
        self.speedy=level
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom>HEIGHT:
            self.kill()


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock=pygame.time.Clock()

#load all game graphics
background=pygame.image.load(path.join(img_dir,"bg.png")).convert()
background_rect=background.get_rect()
player_img=pygame.image.load(path.join(img_dir,"p1_stand.png")).convert()
life_img=pygame.image.load(path.join(img_dir,"hud_heartFull.png")).convert()
life_img.set_colorkey(BLACK)
life_img=pygame.transform.scale(life_img,(25,19))


#Game loop
running=True
game_over=True
fall=True
while running:
    if game_over:
        show_go_screen()
        game_over=False
        all_sprites=pygame.sprite.Group()
        drops=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        player=Player()
        all_sprites.add(player)
        score=0
        level=1
    if fall:
            level_up()
            fall=False#pause after 1 turn
    if len(drops)==0:#start another turn
            level+=1#level up
            fall=True
            
                      
    clock.tick(FPS)
    #process input(events)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
    #update
    all_sprites.update()

    #check to see if a bullet hit the player
    hits=pygame.sprite.spritecollide(player,bullets,True,pygame.sprite.collide_circle)
    if hits:
        player.lives-=1

    #check to see if a drop hit the player
    hits=pygame.sprite.spritecollide(player,drops,True,pygame.sprite.collide_circle)
    for hit in hits:
        score+=level
        
    #-1 live    
    if player.shield<=0:
        #player.hide()
        player.lives-=1
        player.shield=100
        
    #game over
    if player.lives==0:
        game_over=True

    #display
    screen.fill((0,0,0))
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen,str(score),18,WIDTH/2,10)
    draw_text(screen,"level"+str(level),18,WIDTH/2,30)
    draw_shield_bar(screen,5,5,player.shield)
    draw_lives(screen,WIDTH-100,5,player.lives,life_img)
    pygame.display.flip()
    
pygame.quit()
    

