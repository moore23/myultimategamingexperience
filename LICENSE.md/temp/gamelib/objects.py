import pygame,random,time,os
class Player(object):
    def __init__(self):
        self.rect=pygame.Rect(387,425,50,50)
        self.health=500
        self.shots=[]
        self.shottime=0
        self.specialtime=0
    def move(self,dx,dy):
        if dx!=0:
            self.rect.x+=dx
        if dy!=0:
            self.rect.y+=dy
        if self.rect.x>775:
            self.rect.x=775
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.y>850:
            self.rect.y=850
    def shoot(self):
        self.shots.append(pygame.Rect(self.rect.x+45,self.rect.y+23,10,4))
class Enemy(object):
    def __init__(self):
        self.rect=pygame.Rect(1600,random.randint(0,800),100,100)
        self.speed=random.randint(-5,5)
        if self.speed==0:
            self.speed=random.choice([1,-1])
        self.boundary=random.randint(1000,1450)
        self.shot=pygame.Rect(self.rect.x,self.rect.y+48,10,4)
    def move(self,dx,dy):
        if dx!=0:
            self.rect.x+=dx
        if dy!=0:
            self.rect.y+=dy
            if self.rect.y>800:
                self.rect.y=800
                self.speed=-self.speed
            if self.rect.y<0:
                self.rect.y=0
                self.speed=-self.speed
class Boss(object):
    def __init__(self):
        self.rect=pygame.Rect(1600,221,330,457)
        self.enemies1=[]
        self.enemies2=[]
        self.stage=random.choice([1,-1])
        self.time=0
        self.maxhealth=self.health=25
    def move(self,dx,dy):
        if dx!=0:
            self.rect.x+=dx
        if dy!=0:
            self.rect.y+=dy
class Bossenemy(object):
    def __init__(self,wx,wy,size):
        self.rect=pygame.Rect(wx,wy,2*size,2*size)
        self.randomangle=random.choice([random.randint(4,10),-random.randint(9,20)])
        self.time=0
class Star(object):
    def __init__(self,wx,wy):
        self.rect=pygame.Rect(wx,wy,2,2)
        self.speed=random.randint(1,3)
class Joshenemy(object):
    def __init__(self,wx,wy,japchars):
        self.image=random.choice(japchars)
        self.rect=pygame.Rect(wx,wy,200,200)
        self.deltax=random.randint(5,20)
        self.deltay=random.randint(-20,20)
        if self.deltay<0:
            if self.deltax<-2*self.deltay:
                self.deltax=-2*self.deltay+1
        if self.deltay>0:
            if self.deltax<2*self.deltay:
                self.deltax=2*self.deltay+1
        if self.deltax>15:
            self.deltax=(self.deltax+4)/2
            self.deltay=self.deltay/2
def volcollision(mouseloc,volume):
    if pygame.Rect(663,438,24,24).collidepoint(mouseloc):
        return 0.0
    elif pygame.Rect(688,438,24,24).collidepoint(mouseloc):
        return 0.1
    elif pygame.Rect(713,438,24,24).collidepoint(mouseloc):
        return 0.2
    elif pygame.Rect(738,438,24,24).collidepoint(mouseloc):
        return 0.3
    elif pygame.Rect(763,438,24,24).collidepoint(mouseloc):
        return 0.4
    elif pygame.Rect(788,438,24,24).collidepoint(mouseloc):
        return 0.5
    elif pygame.Rect(813,438,24,24).collidepoint(mouseloc):
        return 0.6
    elif pygame.Rect(838,438,24,24).collidepoint(mouseloc):
        return 0.7
    elif pygame.Rect(863,438,24,24).collidepoint(mouseloc):
        return 0.8
    elif pygame.Rect(888,438,24,24).collidepoint(mouseloc):
        return 0.9
    elif pygame.Rect(913,438,24,24).collidepoint(mouseloc):
        return 1.0
    else:
        return volume
