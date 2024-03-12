import pygame,random,math
from pygame.locals import *
pygame.init()
screen_width,screen_height = 1520,770
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.flip()
clock = pygame.time.Clock()
# map
background = pygame.image.load(r"C:\Users\daniel\Downloads\gimmie-pig-02-server-sample-2.jpg")
background_transform = pygame.transform.scale(background,(screen_width, screen_height))
mapX,mapY = 0,0

ememies_list = []
class Ememies(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0.01
        self.angle = 0
        list = [r"C:\Users\daniel\Downloads\city-battle-pj-1 - Copy-modified.png",r"C:\Users\daniel\Downloads\fbbaa9cd0ec2ea73c76cdf1585cf1652-modified.png",r"C:\Users\daniel\Downloads\png-clipart-mechwarrior-online-mechwarrior-3050-mechwarrior-4-vengeance-battletech-battlemech-military-robot-video-game-weapon-modified.png",r"C:\Users\daniel\Downloads\png-clipart-robot-mecha-robot-electronics-action-figure-thumbnail-modified.png"]
        self.image = pygame.image.load(random.choice(list))
        self.image_transform = pygame.transform.scale(self.image,(self.width,self.height))
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        self.rect = self.image.get_rect()
        # hit box
        self.hitbox = (self.x,self.y,self.width,self.height)

    def hit(self):
        for ememies in ememies_list:
            if player.hitbox[0] <= ememies.x + ememies.width <= player.hitbox[0] + player.hitbox[2] and player.hitbox[1] <= ememies.y + ememies.height <= player.hitbox[1] + player.hitbox[3]:
                restart()
        # ------------------------
        try:
            for ememies in ememies_list:
                for bullet in bullet_list:
                    if bullet.hitbox[0] <= ememies.x + ememies.width <= bullet.hitbox[0] + bullet.hitbox[2] and bullet.hitbox[1] <= ememies.y + ememies.height <= bullet.hitbox[1] + bullet.hitbox[3]:
                        ememies_list.remove(ememies)
                        bullet_list.remove(bullet)
                        add_ememies()
        except:
            pass
        
    def move(self):
        if self.y + 5 > player.y:
            self.y -= self.speed
        if self.y + 5 < player.y:
            self.y += self.speed
        if self.x + 5 > player.x:
            self.x -= self.speed
        if self.x + 5 < player.x:
            self.x += self.speed
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.move()
        self.hit()
        screen.blit(self.image_rotate, (self.x,self.y))
        self.hitbox = (self.x,self.y,self.width,self.height)

bullet_list = []
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,angle):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load(r"C:\Users\daniel\Downloads\bullet.png")
        self.image_transform = pygame.transform.scale(self.image,(self.width,self.height))
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        self.rect = self.image.get_rect()
        # hit box
        self.hitbox = (self.x,self.y,self.width + 40,self.height + 40)

    def move(self):
        #  move at angles
        if self.angle == 0:
            self.y -= 1
        if self.angle == 180:
            self.y += 1
        if self.angle == 90:
            self.x -= 1
        if self.angle == -90:
            self.x += 1
        # update
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        screen.blit(self.image_rotate, (self.x,self.y))
        self.hitbox = (self.x,self.y,self.width,self.height)
               
        

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 0.3
        self.angle = 0
        self.reload = 100
        self.image = pygame.image.load(r"C:\Users\daniel\Downloads\e633cf62a2bf83fbeb77b741cff62414--dark-matter-perso-modified.png")
        self.image_transform = pygame.transform.scale(self.image,(self.width,self.height))
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        self.rect = self.image.get_rect()
        # hit box
        self.hitbox = (self.x,self.y,self.width,self.height)
        
    def Reload(self):
        if self.reload > 0:
            self.reload -= 1

    def Rotate_player(self):
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            self.angle = 90
        if userInput[pygame.K_RIGHT]:
            self.angle = -90
        if userInput[pygame.K_UP]:
            self.angle = 0
        if userInput[pygame.K_DOWN]:
            self.angle = 180
        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
        
    def move(self):
        self.rect.x = self.x
        self.rect.y = self.y
        # ------------------
        self.Rotate_player()
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_d]:
            self.x += self.speed
        if userInput[pygame.K_a]:
            self.x -= self.speed
        if userInput[pygame.K_w]:
            self.y -= self.speed
        if userInput[pygame.K_s]:
            self.y += self.speed
        if userInput[pygame.K_SPACE] and self.reload <= 0:
            bullet = Bullet(self.x,self.y,10,10,player.angle)
            bullet_list.append(bullet)
            self.reload = 100
        # --------------------------- boundery
        if self.x <= 0:
            self.x += 1
        if self.x >= screen_width - self.width:
            self.x -= 1
        if self.y <= 0:
            self.y += 1
        if self.y >= screen_height - self.height:
            self.y -= 1

        self.image_rotate = pygame.transform.rotate(self.image_transform, self.angle)
            
    def draw(self):
        self.Reload()
        self.move()
        screen.blit(self.image_rotate, (self.x,self.y))
        self.hitbox = (self.x,self.y,self.width,self.height)


def restart():
    global x,y, ememies_list,max_speed
    player.x,player.y = screen_width / 2,screen_height / 2
    max_speed = 0.01
    for ememies in ememies_list:
        ememies.x,ememies.y = random.randint(40,screen_width - 40),random.randint(40,screen_height - 40)
        ememies.speed = max_speed
        
max_speed = 0.01
def add_ememies():
    global max_speed,max_ememies
    max_speed += 0.01
    for x in range(1):
        ememies = Ememies(random.randint(0,screen_width - 40),random.randint(0,screen_height - 40),40,40)
        ememies.speed = max_speed
        ememies_list.append(ememies)
        
    

# players
player = Player(screen_width / 2,screen_height / 2,40,40)

for x in range(5):
    ememies = Ememies(random.randint(0,screen_width - 40),random.randint(0,screen_height - 40),40,40)
    ememies_list.append(ememies)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill((255,255,255))
    screen.blit(background_transform, (mapX,mapY))
    
    player.draw()

    for bullet in bullet_list:
        bullet.move()
    
    for ememies in ememies_list:
        ememies.draw()

    pygame.display.update()
    clock.tick(0)
