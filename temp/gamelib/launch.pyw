try:
    with open("data/levels/1.txt","r")as f:
        folder="data/"
        f.close()
except:
    folder="gamelib/data/"


#self explanatory
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


#enemy ships
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


"""
#boss heads
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
"""


#aarron head
class AarronBoss(object):
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


#aarrons attacks
class Aarronenemy(object):
    def __init__(self,wx,wy,size):
        self.rect=pygame.Rect(wx,wy,2*size,2*size)
        self.randomangle=random.randint(-20,10)
        self.time=0


#background stars
class Star(object):
    def __init__(self,wx,wy):
        self.rect=pygame.Rect(wx,wy,2,2)
        self.speed=random.randint(1,3)


#josh head
class JoshBoss(object):
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


#joshs attacks
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


# Banner head
class BannerBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 75

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy


# Banners attacks
"""
class Bannerenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0
"""

class Bannerenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-15, 10)
        self.time = 0
        self.deltax = random.randint(5, 20)
        self.deltay = random.randint(-20, 20)
        if self.deltay < 0:
            if self.deltax < -2 * self.deltay:
                self.deltax = -2 * self.deltay + 1
        if self.deltay > 0:
            if self.deltax < 2 * self.deltay:
                self.deltax = 2 * self.deltay + 1
        if self.deltax > 15:
            self.deltax = (self.deltax + 4) / 2
            self.deltay = self.deltay / 2


# Cringe head
class CringeBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy


# Cringes attacks
class Cringeenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0


# Burkes head
class BurkeBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy


# Burkes attacks
class Burkeenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0


# Digger head
class DiggerBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy


# Diggers attacks
class Diggerenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0


# Salman head
class SalmanBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy


# Salmans attacks
class Salmanenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0

# Tones head
class TonesBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy

# Tones's attacks
class Tonesenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0

# Niall head
class NiallBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy

# Niall's attacks
class Niallenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0

# Andrew head
class AndrewBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy

# Andrew's attacks
class Andrewenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0

# Garside head
class GarsideBoss(object):
    def __init__(self):
        self.rect = pygame.Rect(1600, 221, 330, 457)
        self.enemies1 = []
        self.enemies2 = []
        self.stage = random.choice([1, -1])
        self.time = 0
        self.maxhealth = self.health = 25

    def move(self, dx, dy):
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy

# Garside's attacks
class Garsideenemy(object):
    def __init__(self, wx, wy, size):
        self.rect = pygame.Rect(wx, wy, 2 * size, 2 * size)
        self.randomangle = random.randint(-20, 10)
        self.time = 0

#volume slider
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


#plays explosion images
def expanim(player):
    if time.time()-player.exptime<0.1:
        player.expmarker=exp1
    elif time.time()-player.exptime<0.2:
        player.expmarker=exp2
    elif time.time()-player.exptime<0.3:
        player.expmarker=exp3
    elif time.time()-player.exptime<0.4:
        player.expmarker=exp4
    elif time.time()-player.exptime<0.5:
        player.expmarker=exp5
    elif time.time()-player.exptime<0.6:
        player.expmarker=exp6
    elif time.time()-player.exptime<0.7:
        player.expmarker=exp7
    elif time.time()-player.exptime<0.8:
        player.expmarker=exp8
    elif time.time()-player.exptime<0.9:
        player.expmarker=exp9
    elif time.time()-player.exptime<1:
        player.expmarker=exp10
    elif time.time()-player.exptime<1.1:
        player.expmarker=exp11
    elif time.time()-player.exptime<1.2:
        player.expmarker=exp12
    elif time.time()-player.exptime<1.3:
        player.expmarker=exp13
    elif time.time()-player.exptime<1.4:
        player.expmarker=exp14
    else:
        player.expmarker=exp0

import pygame,random,math,time,os

#joshs japanese
japchars=[]
for file in os.listdir(folder+"sprites/japchar"):
    japchars.append(pygame.image.load(os.path.join(folder+"sprites/japchar",file)))

#shorthand for sprite directory
spriteLOC=folder+"sprites/"

#colours
lightblue=(221,160,221)
white=(255,255,255)
purple=(139,0,139)
orange=(255,69,0)
blue=(0,255,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)

#?
level=startlevel=0
someothernumber=0
shotcollisions=[]

#inside options menu? textures enabled?
inoptions=False
display=True

#SND CHANNELS
channels=[]
sometime=0

#entities list
enemies=[]
aarrons=[]
joshs=[]
banners=[]#
cringes=[]#
burkes=[]#
diggers=[]#
salmans=[]#
dans=[]#
nialls=[]#
andrews=[]#
garsides=[]#
stars=[]
deadenemies=[]

#running (?)
r=True

#quarantine
g1=0
g=0

#window config
os.environ["SDL_VIDEO_WINDOW_POS"]="0,0"
pygame.init()
pygame.mouse.set_visible(False)
#screen = pygame.display.set_mode((1600,900))
screen = pygame.display.set_mode((1600,900),pygame.FULLSCREEN)
clock = pygame.time.Clock()

#bodies
playership=pygame.image.load(spriteLOC+"player.gif")
enemyship=pygame.image.load(spriteLOC+"enemy.png")
aarronship=pygame.image.load(spriteLOC+"aarron.png")
joshship=pygame.image.load(spriteLOC+"josh.png")
bannership=pygame.image.load(spriteLOC+"banner.png")
cringeship=pygame.image.load(spriteLOC+"cringe.png")#sprite needed
burkeship=pygame.image.load(spriteLOC+"burke.png")#sprite needed
diggership=pygame.image.load(spriteLOC+"diggers.png")
salmanship=pygame.image.load(spriteLOC+"salman.png")
danship=pygame.image.load(spriteLOC+"tones.png")#sprite needed
niallship=pygame.image.load(spriteLOC+"naill.png")
andrewship=pygame.image.load(spriteLOC+"andrew.png")
garsideship=pygame.image.load(spriteLOC+"garside.png")

#buttons & bounding boxes
titlebg=pygame.image.load(spriteLOC+"titlebg.png")
playrect=pygame.image.load(spriteLOC+"playrect.png")
optionrect=pygame.image.load(spriteLOC+"optionrect.png")
quitrect=pygame.image.load(spriteLOC+"quitrect.png")
exitrect=pygame.image.load(spriteLOC+"backrect.png")
right=pygame.image.load(spriteLOC+"right.png")
left=pygame.image.load(spriteLOC+"left.png")
selected=pygame.image.load(spriteLOC+"selected.png")
unselected=pygame.image.load(spriteLOC+"unselected.png")
ticked=pygame.image.load(spriteLOC+"ticked.png")

#sprites
fireshot=pygame.image.load(spriteLOC+"fire.png")
cursor=pygame.image.load(spriteLOC+"cursor.png")

for file in os.listdir(spriteLOC+"explosions"):
    exec("exp{} = pygame.image.load(os.path.join(spriteLOC+'explosions',file))".format(file[:-4])) #removes .png from file name

#player shield bounds
shieldrect=pygame.image.load(spriteLOC+"shield.png")
actshieldrect=pygame.image.load(spriteLOC+"actshield.png")

#collisions
class Collision(object):
    def __init__(self,wx,wy):
        self.rect=pygame.Rect(wx,wy,1,1)
        self.exptime=0
        self.expmarker=exp0

#initial options
myfont=pygame.font.SysFont("Arial",30)
myfont.set_underline(True)
vollabel=myfont.render("VOLUME",0,white,black)
texlabel=myfont.render("TEXTURES?",0,white,black)
levlabel=myfont.render("LEVEL SELECT",0,white,black)
elabel=myfont.render("EASY",0,white,black)
mlabel=myfont.render("MEDIUM",0,white,black)
hlabel=myfont.render("HARD",0,white,black)
difficulty="m" #begins on medium difficulty

#level selector
levlabels=[]
for file in os.listdir(folder+"levels"):
    levlabels.append(myfont.render(file[:-4],0,white,black))#removes '.txt' from the file name

#player options
player=Player()
player.maxhealth=player.health
player.sound=pygame.mixer.Sound(folder+"sounds/fire.wav")
player.hitsound=pygame.mixer.Sound(folder+"sounds/hit.wav")
player.shieldsound=pygame.mixer.Sound(folder+"sounds/shield.wav")

#SND CHANNELS
pygame.mixer.set_num_channels(50)
channel0=pygame.mixer.Channel(0) #aarron BGM
channel1=pygame.mixer.Channel(1) #player SFX
channel2=pygame.mixer.Channel(2) #josh BGM
channel3=pygame.mixer.Channel(3) #enemy SFX
channel4=pygame.mixer.Channel(4) #enemy SFX
channel5=pygame.mixer.Channel(5) #enemy SFX
#channel6=pygame.mixer.Channel(6) #enemy SFX
#channel7=pygame.mixer.Channel(7) #enemy SFX
#channel8=pygame.mixer.Channel(8) #enemy SFX
#channel9=pygame.mixer.Channel(9) #enemy SFX
#channel10=pygame.mixer.Channel(10) #enemy SFX
#channel11=pygame.mixer.Channel(11) #enemy SFX
#channel12=pygame.mixer.Channel(12) #enemy SFX
#channel13=pygame.mixer.Channel(13) #enemy SFX
#channel14=pygame.mixer.Channel(14) #enemy SFX
#channel15=pygame.mixer.Channel(15) #enemy SFX
#channel16=pygame.mixer.Channel(16) #enemy SFX
#channel17=pygame.mixer.Channel(17) #enemy SFX
#channel18=pygame.mixer.Channel(18) #enemy SFX
#channel19=pygame.mixer.Channel(19) #enemy SFX
#channel20=pygame.mixer.Channel(20) #enemy SFX
#channel21=pygame.mixer.Channel(21) #enemy SFX
#channel22=pygame.mixer.Channel(22) #enemy SFX
channel23=pygame.mixer.Channel(23) #explosion SFX
channel24=pygame.mixer.Channel(24) #shield SFX
channel25=pygame.mixer.Channel(25) #generic
channel26=pygame.mixer.Channel(26) #banner BGM
channel27=pygame.mixer.Channel(27) #cringe BGM
channel28=pygame.mixer.Channel(28) #burke BGM
channel29=pygame.mixer.Channel(29) #digger BGM
channel30=pygame.mixer.Channel(30) #aarron VOX
channel31=pygame.mixer.Channel(31) #josh VOX
channel32=pygame.mixer.Channel(32) #banner VOX
channel33=pygame.mixer.Channel(33) #cringe VOX
channel34=pygame.mixer.Channel(34) #burke VOX
channel35=pygame.mixer.Channel(35) #digger VOX
channel36=pygame.mixer.Channel(36) #salman BGM
channel37=pygame.mixer.Channel(37) #salman VOX
channel38=pygame.mixer.Channel(38) #tones BGM
channel39=pygame.mixer.Channel(39) #tones VOX
channel40=pygame.mixer.Channel(40) #niall BGM
channel41=pygame.mixer.Channel(41) #niall SFX
channel42=pygame.mixer.Channel(42) #andrew BGM
channel43=pygame.mixer.Channel(43) #andrew SFX
channel44=pygame.mixer.Channel(44) #garside BGM
channel45=pygame.mixer.Channel(45) #garside SFX
channel46=pygame.mixer.Channel(46)
channel47=pygame.mixer.Channel(47)
channel48=pygame.mixer.Channel(48)
channel49=pygame.mixer.Channel(49)

#20 enemy channels, max 20 enemies ###3 for now
#enemychannels=[channel3,channel4,channel5,channel6,channel7,channel8,channel9,channel10,channel11,channel12,channel13,channel14,channel15,channel16,channel17,channel18,channel19,channel20,channel21,channel22]
enemychannels=[channel3,channel4,channel5]
#23 & 24 maybve expl

#master volume
volume=channel0.get_volume()

#moving background
for turn in range(500):
    stars.append(Star(random.randint(0,1598),random.randint(0,898)))

#deletes killed enemies
def deletealllists():
    global enemies,aarrons,joshs,banners,cringes,burkes,diggers,salmans,dans,nialls,andrews,garsides
    enemies=[]
    aarrons=[]
    joshs=[]
    banners=[]
    cringes=[]
    burkes=[]
    diggers=[]
    salmans=[]
    dans=[]
    nialls=[]
    andrews=[]
    garsides=[]

#level select buttons
def levelselect(lx):
    global level,startlevel
    if lx<=599:
        startlevel=level=0
        deletealllists()
    elif lx>=615 and lx<=639:
        startlevel=level=1
        deletealllists()
    elif lx>=655 and lx<=679:
        startlevel=level=2
        deletealllists()
    elif lx>=695 and lx<=719:
        startlevel=level=3
        deletealllists()
    elif lx>=735 and lx<=759:
        startlevel=level=4
        deletealllists()
    elif lx>=775 and lx<=799:
        startlevel=level=5
        deletealllists()
    elif lx>=815 and lx<=839:
        startlevel=level=6
        deletealllists()
    elif lx>=855 and lx<=879:
        startlevel=level=7
        deletealllists()
    elif lx>=895 and lx<=919:
        startlevel=level=8
        deletealllists()
    elif lx>=935 and lx<=959:
        startlevel=level=9
        deletealllists()
    elif lx>=975 and lx<=999:
        startlevel=level=10
        deletealllists()
    elif lx>=1015 and lx<=1039:
        startlevel=level=11
        deletealllists()
    elif lx>=1055 and lx<=1079:
        startlevel=level=12
        deletealllists()
    elif lx>=1095 and lx<=1119:
        startlevel=level=13
        deletealllists()
    elif lx>=1135 and lx<=1159:
        startlevel=level=14
        deletealllists()
    elif lx>=1175 and lx<=1199:
        startlevel=level=15
        deletealllists()
    elif lx>=1215 and lx<=1239:
        startlevel=level=16
        deletealllists()
    elif lx>=1255 and lx<=1279:
        startlevel=level=17
        deletealllists()
    elif lx>=1295 and lx<=1319:
        startlevel=level=18
        deletealllists()

#start screen
def startmenu(runningthefuckaway,someotherfuckingtime):
    global volume,display,inoptions,r,someothernumber,startlevel,difficulty
    someotherfuckingtime=time.time()

    #in pause menu
    while runningthefuckaway:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                runningthefuckaway=False
            if e.type==pygame.MOUSEBUTTONDOWN:
                mouseloc=pygame.mouse.get_pos()
                if mouseloc[0]>533 and mouseloc[0]<1066:
                    if mouseloc[1]>=180 and mouseloc[1]<336:
                        runningthefuckaway=False
                    if mouseloc[1]>=360 and mouseloc[1]<516:
                        inoptions=True
                        screen.fill((0,0,0))
                    if mouseloc[1]>=540 and mouseloc[1]<696:
                        r=False
                        runningthefuckaway=False

        #user can press escape to close pause menu
        user_input=pygame.key.get_pressed()
        if user_input[pygame.K_ESCAPE]and time.time()-someotherfuckingtime>0.2:
            runningthefuckaway=False
        while inoptions:
            screen.fill((0,0,0))
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    running=False
                if e.type==pygame.MOUSEBUTTONDOWN:
                    mouseloc=pygame.mouse.get_pos()
                    if mouseloc[1]>=438 and mouseloc[1]<=462:
                        if mouseloc[0]>=638 and mouseloc[0]<=662 and volume>0.1:
                            volume-=0.1
                        elif mouseloc[0]>=638 and mouseloc[0]<=662:
                            volume=0
                        if mouseloc[0]>=938 and mouseloc[0]<=962 and volume<0.9:
                            volume+=0.1
                        elif mouseloc[0]>=938 and mouseloc[0]<=962:
                            volume=1
                    if mouseloc[0]>=575 and mouseloc[0]<=1095:
                        if mouseloc[1]>=350 and mouseloc[1]<=374:
                            levelselect(mouseloc[0])
                    if mouseloc[1]>=550 and mouseloc[1]<=574 and mouseloc[0]>=788 and mouseloc[0]<=812:
                        if display:
                            display=False
                        else:
                            display=True
                    if mouseloc[1]>=600 and mouseloc[1]<=700 and mouseloc[0]>=638 and mouseloc[0]<=962:
                        inoptions=False
                    if mouseloc[1]>=150 and mouseloc[1]<=174:
                        if mouseloc[0]>=595 and mouseloc[0]<=619:
                            difficulty="e"
                        if mouseloc[0]>=788 and mouseloc[0]<=812:
                            difficulty="m"
                        if mouseloc[0]>=995 and mouseloc[0]<=1019:
                            difficulty="h"
                    volume=volcollision(mouseloc,volume)
            user_input=pygame.key.get_pressed()
            if user_input[pygame.K_ESCAPE]:
                inoptions=False
                runningthefuckaway=False
            for lev in levlabels:
                if someothernumber>=9:
                    screen.blit(lev,(574+someothernumber*40,300))
                else:
                    screen.blit(lev,(581+someothernumber*40,300))
                screen.blit(selected,(575+someothernumber*40,350))
                someothernumber+=1
            screen.blit(unselected,(575+startlevel*40,350))
            someothernumber=0
            screen.blit(selected,(595,150))
            screen.blit(selected,(788,150))
            screen.blit(selected,(995,150))
            if difficulty=="e":
                screen.blit(ticked,(595,150))
            if difficulty=="m":
                screen.blit(ticked,(788,150))
            if difficulty=="h":
                screen.blit(ticked,(995,150))
            screen.blit(elabel,(575,100))
            screen.blit(mlabel,(750,100))
            screen.blit(hlabel,(975,100))

            screen.blit(levlabel,(716,250))

            screen.blit(vollabel,(754,400))
            screen.blit(left, (638, 438))
            screen.blit(right, (938, 438))
            screen.blit(texlabel,(734,500))

            screen.blit(exitrect,(638,600))

            if display:
                screen.blit(ticked,(788,550))
            else:
                screen.blit(selected,(788,550))
            for turn in range(11):
                screen.blit(unselected,(turn*25+663,438))
            screen.blit(selected,(volume*250+663,438))
            screen.blit(cursor,pygame.mouse.get_pos())
            pygame.display.update()
            pygame.display.flip()
        screen.fill((0,0,0))
        screen.blit(playrect,(533,180))
        screen.blit(optionrect,(533,360))
        screen.blit(quitrect,(533,540))
        screen.blit(cursor,pygame.mouse.get_pos())
        pygame.display.update()
        pygame.display.flip()
startmenu(True,sometime)

#stuff to do with explosions
player.exptime=0
player.expmarker=exp1

#aarron music channel 1
#josh music channel 2
joshrndbgm1=pygame.mixer.Sound(folder+"music/josh1.wav")
joshrndbgm2=pygame.mixer.Sound(folder+"music/josh2.wav")
joshrndbgm3=pygame.mixer.Sound(folder+"music/josh3.wav")
joshrndbgm4=pygame.mixer.Sound(folder+"music/josh4.wav")
joshrndbgm5=pygame.mixer.Sound(folder+"music/josh5.wav")
joshrndbgm6=pygame.mixer.Sound(folder+"music/josh6.wav")
joshrndbgm7=pygame.mixer.Sound(folder+"music/josh7.wav")
joshbossbgm=[joshrndbgm1,joshrndbgm2,joshrndbgm3,joshrndbgm4,joshrndbgm5,joshrndbgm6,joshrndbgm7]

aarronbossbgm=pygame.mixer.Sound(folder+"music/aarron.wav")
#bannerbossbgm=
#cringebossbgm=
#burkebossbgm
#diggerbossbgm
#salman
#dan
#niall
#andrew
#garside
###########################
rndbgm1=pygame.mixer.Sound(folder+"music/bgm/bgm1.wav")
rndbgm2=pygame.mixer.Sound(folder+"music/bgm/bgm2.wav")
rndbgm3=pygame.mixer.Sound(folder+"music/bgm/bgm3.wav")
rndbgm4=pygame.mixer.Sound(folder+"music/bgm/bgm4.wav")
rndbgm5=pygame.mixer.Sound(folder+"music/bgm/bgm5.wav")
rndbgm6=pygame.mixer.Sound(folder+"music/bgm/bgm6.wav")
rndbgm7=pygame.mixer.Sound(folder+"music/bgm/bgm7.wav")
rndbgm8=pygame.mixer.Sound(folder+"music/bgm/bgm8.wav")
rndbgm9=pygame.mixer.Sound(folder+"music/bgm/bgm9.wav")
rndbgm10=pygame.mixer.Sound(folder+"music/bgm/bgm10.wav")
rndbgm11=pygame.mixer.Sound(folder+"music/bgm/bgm11.wav")

rndsndtrack=[rndbgm1,rndbgm2,rndbgm3,rndbgm4,rndbgm5,rndbgm6,rndbgm7,rndbgm8,rndbgm9,rndbgm10,rndbgm11]

#once game has started
while r:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            r=False
    for channel in enemychannels:
        channel.set_volume(volume)
    channel0.set_volume(volume)
    channel1.set_volume(volume)
    channel2.set_volume(volume)

    #music
    #nobody
    if len(aarrons)==0 and len(joshs)==0 and len(banners)==0:
        if not channel25.get_busy():
            channel25.play(random.choice(rndsndtrack))
    else:
        channel25.stop()

    #when josh
    if len(joshs)>0:
        if not channel0.get_busy():
            channel0.play(random.choice(joshbossbgm))
    else:
        channel0.stop()

    #when aarron and no josh
    if len(aarrons)>0 and len(joshs)==0:
        if not channel2.get_busy():
            channel2.play(aarronbossbgm)
    else:
        channel2.stop()

    #when banner is active
    if len(banners)>0:
        if not channel26.get_busy():
            channel26.play(random.choice(rndsndtrack))
    else:
        channel26.stop()

    #starting a new level
    if len(enemies)+len(aarrons)+len(joshs)+len(banners)+len(cringes)+len(burkes)+len(diggers)+len(salmans)+len(dans)+len(nialls)+len(andrews)+len(garsides)==0:
        level+=1
        try:
            with open(folder+"levels/"+str(level)+".txt","r")as f:
                for row in f:
                    number=""
                    for col in row:
                        if col in"0123456789":
                            number+=col
                        if col in"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                            letter = col
                            number=int(number)
                            #generic enemies
                            if letter in"Ee":
                                for turn in range(number):
                                    enemies.append(Enemy())
                            #aarrons
                            if letter in"Aa":
                                for turn in range(number):
                                    aarrons.append(AarronBoss())
                                if len(aarrons)==2:
                                    aarrons[0].rect.y=0
                                    aarrons[1].rect.y=450
                                #ensures both aarrons start in the same attack phase
                                try:
                                    aarrons[0].stage=aarrons[1].stage=1
                                except:
                                    aarrons[0].stage=1
                            #joshs
                            if letter in"Jj":
                                for turn in range(number):
                                    joshs.append(JoshBoss())
                                if len(joshs)==2:
                                    joshs[0].rect.y=0
                                    joshs[1].rect.y=450
                            #banners
                            if letter in"Bb":
                                for turn in range(number):
                                    banners.append(BannerBoss())
                                if len(banners)==2:
                                    banners[0].rect.y=0
                                    banners[1].rect.y=450
                            #cringes
                            if letter in"Cc":
                                for turn in range(number):
                                    cringes.append(CringeBoss())
                                if len(cringes)==2:
                                    cringes[0].rect.y=0
                                    cringes[1].rect.y=450
                            #burkes
                            if letter in"Vv":
                                for turn in range(number):
                                    burkes.append(BurkeBoss())
                                if len(burkes)==2:
                                    burkes[0].rect.y=0
                                    burkes[1].rect.y=450
                            #diggers
                            if letter in"Dd":
                                for turn in range(number):
                                    diggers.append(DiggerBoss())
                                if len(diggers)==2:
                                    diggers[0].rect.y=0
                                    diggers[1].rect.y=450
                            #salmans
                            if letter in "Ss":
                                for turn in range(number):
                                    salmans.append(SalmanBoss())
                                if len(salmans)==2:
                                    salmans[0].rect.y=0
                                    salmans[1].rect.y=450
                            #tones
                            if letter in"Tt":
                                for turn in range(number):
                                    dans.append(TonesBoss())
                                if len(dans)==2:
                                    dans[0].rect.y=0
                                    dans[1].rect.y=450
                            #niall
                            if letter in"Nn":
                                for turn in range(number):
                                    nialls.append(NiallBoss())
                                if len(nialls)==2:
                                    nialls[0].rect.y=0
                                    nialls[0].rect.y=450
                            #andrew
                            if letter in"Ww":
                                for turn in range(number):
                                    andrews.append(AndrewBoss())
                                if len(andrews)==2:
                                    andrews[0].rect.y=0
                                    andrews[1].rect.y=450
                            #garside
                            if letter in"Gg":
                                for turn in range(number):
                                    garsides.append(GarsideBoss())
                                if len(garsides)==2:
                                    garsides[0].rect.y=0
                                    garsides[1].rect.y=450
        except:
            level=startlevel
            startmenu(True,sometime)

        if level==startlevel+1:
            if difficulty=="h":
                player.maxhealth=200
                for items in [aarrons,joshs,banners,cringes,burkes,salmans,diggers,dans,nialls,andrews,garsides]:
                    for item in items:
                        item.maxhealth=item.health=25
            elif difficulty=="m":
                player.maxhealth=200
                for items in [aarrons,joshs,banners,cringes,burkes,salmans,diggers,dans,nialls,andrews,garsides]:
                    for item in items:
                        item.maxhealth=item.health=15
            elif difficulty=="e":
                player.maxhealth=200
                for items in [aarrons,joshs,banners,cringes,burkes,salmans,diggers,dans,nialls,andrews,garsides]:
                    for item in items:
                        item.maxhealth=item.health=10
            player.health=player.maxhealth

        somefuckingnumber=0

        #handles enemy firing sounds (can get loud)
        #for enemy in range(3):#stops it from getting too dank
        for enemy in enemies:
            try:
                enemy.sound=pygame.mixer.Sound(folder+"sounds/fire.wav")
                enemy.channel=enemychannels[somefuckingnumber]
                somefuckingnumber+=1
            except:
                pass

    #when player dies
    if player.health<=0:
        level=startlevel
        deletealllists()

    #key presses
    user_input=pygame.key.get_pressed()
    if user_input[pygame.K_w]:
        player.move(0,-10) #move up

    if user_input[pygame.K_s]:
        player.move(0,10) #move down

    if user_input[pygame.K_a]:
        player.move(-10,0) #move left

    if user_input[pygame.K_d]:
        player.move(10,0) #move right

    if user_input[pygame.K_SPACE]:
        if difficulty=="h":
            if time.time() - player.shottime > 0.25:
                player.shottime=time.time()
                player.shoot()
                channel1.play(player.sound) #fires shot
        elif difficulty == "m":
            if time.time() - player.shottime > 0.3:
                player.shottime = time.time()
                player.shoot()
                channel1.play(player.sound)  # fires shot
        elif difficulty == "e":
            if time.time() - player.shottime > 0.33:
                player.shottime = time.time()
                player.shoot()
                channel1.play(player.sound)  # fires shot

    #enables shield
    if user_input[pygame.K_LSHIFT]and time.time()-player.specialtime>2:
        channel24.play(player.shieldsound)
        player.specialtime=time.time()
        circlerect=pygame.Rect(player.rect.x-90,player.rect.y-90,230,230)
        for enemy in enemies:
            if enemy.shot.colliderect(circlerect):
                enemy.shot.y=2000
            if enemy.shot.colliderect(player.rect):
                    player.health+=1
        for aarron in aarrons:
            for item in aarron.enemies1:
                if item.rect.colliderect(circlerect):
                    aarron.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=1
            for item in aarron.enemies2:
                if item.rect.colliderect(circlerect):
                    aarron.enemies2.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=1
        for josh in joshs:
            for item in josh.enemies1:
                if item.rect.colliderect(circlerect):
                    josh.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=5
        for banner in banners:
            for item in banner.enemies1:
                if item.rect.colliderect(circlerect):
                    banner.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for cringe in cringes:
            for item in cringe.enemies1:
                if item.rect.colliderect(circlerect):
                    cringe.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for burke in burkes:
            for item in burke.enemies1:
                if item.rect.colliderect(circlerect):
                    burke.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for digger in diggers:
            for item in digger.enemies1:
                if item.rect.colliderect(circlerect):
                    digger.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for salman in salmans:
            for item in salman.enemies1:
                if item.rect.colliderect(circlerect):
                    salman.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for dan in dans:
            for item in dan.enemies1:
                if item.rect.colliderect(circlerect):
                    dan.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for niall in nialls:
            for item in niall.enemies1:
                if item.rect.colliderect(circlerect):
                    niall.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for andrew in andrews:
            for item in andrew.enemies1:
                if item.rect.colliderect(circlerect):
                    andrew.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for garside in garsides:
            for item in garside.enemies1:
                if item.rect.colliderect(circlerect):
                    garside.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1

    #pause menu
    if user_input[pygame.K_ESCAPE]and time.time()-sometime>0.5:
        pygame.mixer.pause()
        for aarron in aarrons:
            aarron.time=time.time()-aarron.time
        startmenu(True,sometime)
        for aarron in aarrons:
            aarron.time+=time.time()
        sometime=time.time()

    pygame.mixer.unpause()
    screen.fill((0,0,0))
    for star in stars:
        star.rect.x-=star.speed
        if star.rect.x<=0:
            star.rect.x=1600
        pygame.draw.rect(screen,white,star.rect)
    screen.blit(titlebg,(0,0))
    pygame.draw.circle(screen,purple,(player.rect.x+25,player.rect.y+25),125,1)

    #puts up half second shield
    if time.time()-player.specialtime<0.5:
        circlerect=pygame.Rect(player.rect.x-90,player.rect.y-90,230,230)
        for enemy in enemies:
            if enemy.shot.colliderect(circlerect):
                enemy.shot.y=2000
            if enemy.shot.colliderect(player.rect):
                    player.health+=1
        for aarron in aarrons:
            for item in aarron.enemies1:
                if item.rect.colliderect(circlerect):
                    aarron.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=1
            for item in aarron.enemies2:
                if item.rect.colliderect(circlerect):
                    aarron.enemies2.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=1
        for josh in joshs:
            for item in josh.enemies1:
                if item.rect.colliderect(circlerect):
                    josh.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health+=5
        for banner in banners:
            for item in banner.enemies1:
                if item.rect.colliderect(circlerect):
                    banner.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 5
        for cringe in cringes:
            for item in cringe.enemies1:
                if item.rect.colliderect(circlerect):
                    cringe.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for burke in burkes:
            for item in burke.enemies1:
                if item.rect.colliderect(circlerect):
                    burke.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for digger in diggers:
            for item in digger.enemies1:
                if item.rect.colliderect(circlerect):
                    digger.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for salman in salmans:
            for item in salman.enemies1:
                if item.rect.colliderect(circlerect):
                    salman.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for dan in dans:
            for item in dan.enemies1:
                if item.rect.colliderect(circlerect):
                    dan.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for niall in nialls:
            for item in niall.enemies1:
                if item.rect.colliderect(circlerect):
                    niall.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for andrew in andrews:
            for item in andrew.enemies1:
                if item.rect.colliderect(circlerect):
                    andrew.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1
        for garside in garsides:
            for item in garside.enemies1:
                if item.rect.colliderect(circlerect):
                    garside.enemies1.remove(item)
                if item.rect.colliderect(player.rect):
                    player.health += 1

    #displays shield sprite
    if time.time()-player.specialtime<0.25:
        screen.blit(shieldrect,(player.rect.x-102,player.rect.y-102))
    elif time.time()-player.specialtime<0.5:
        screen.blit(actshieldrect,(player.rect.x-115,player.rect.y-102))
    if display:
        screen.blit(playership,(player.rect.x,player.rect.y+1))
        pygame.draw.rect(screen,white,pygame.Rect(player.rect.x-1,player.rect.y-1,4,52))
    else:
        pygame.draw.rect(screen,white,player.rect)

    #player health bar
    pygame.draw.rect(screen,red,pygame.Rect(player.rect.x,player.rect.y,2,50))
    pygame.draw.rect(screen,green,pygame.Rect(player.rect.x,player.rect.y+50-((player.health*50)/player.maxhealth),2,(player.health*50)/player.maxhealth))

    #explosion animations if textures enabled
    if display:
        expanim(player)
        screen.blit(player.expmarker,(player.rect.x-40,player.rect.y-40))

    #handles enemy attacks
    for enemy in enemies:
        if enemy.rect.x > enemy.boundary:
            enemy.move(-5,0)
        if difficulty=="h":
            enemy.shot.x-=50
        elif difficulty=="m":
            enemy.shot.x-=30
        elif difficulty=="e":
            enemy.shot.x-=20
        enemy.move(0,enemy.speed)
        if enemy.shot.x<0:
            try:
                enemy.channel.play(enemy.sound)
            except:
                pass
            enemy.shot.x=enemy.rect.x
            enemy.shot.y=enemy.rect.y+48
        if enemy.shot.colliderect(player.rect):
            channel23.play(player.hitsound)
            player.exptime=time.time()
            player.expmarker=exp1
            if difficulty =="h":
                player.health-=2
            elif difficulty =="m":
                player.health-=1
            elif difficulty=="e":
                player.health-=1
            enemy.shot.y=2000
        if enemy.shot.y<=50 or enemy.shot.y>=800:
            enemy.shot.y=2000
        if display:
            screen.blit(enemyship,(enemy.rect.x,enemy.rect.y+15))
            screen.blit(fireshot,(enemy.shot.x,enemy.shot.y))
        else:
            pygame.draw.rect(screen,orange,enemy.rect)
            pygame.draw.rect(screen,red,enemy.shot)

    #handles aarrons attacks
    for aarron in aarrons:
        if aarron.rect.x>1000:
            aarron.move(-5,0)
        elif time.time()-aarron.time>2:
            aarron.time=time.time()
            aarron.stage=-aarron.stage
        elif aarron.stage==1:
            aarron.enemies2=[]
            aarron.enemies1=aarron.enemies1[::-1]
            try:
                if time.time()-aarron.sometimesihatemyself>0.025:
                    if difficulty=="h":
                        aarron.enemies1.append(Aarronenemy(aarron.rect.x+random.randint(195,210),aarron.rect.y+random.randint(200,210),20))
                    elif difficulty=="m":
                        aarron.enemies1.append(Aarronenemy(aarron.rect.x + random.randint(175, 185),aarron.rect.y + random.randint(200, 210), 20))
                    elif difficulty=="e":
                        aarron.enemies1.append(Aarronenemy(aarron.rect.x + random.randint(160, 165),aarron.rect.y + random.randint(200, 210), 15))
                    aarron.sometimesihatemyself=time.time()
            except:
                aarron.sometimesihatemyself=time.time()
        elif aarron.stage==-1:
            aarron.enemies1=[]
            if difficulty=="h":
                if len(aarron.enemies2)<30:
                    aarron.enemies2.append(Aarronenemy(aarron.rect.x+random.randint(120,130),aarron.rect.y+457-random.randint(85,95),3))
            elif difficulty=="m":
                if len(aarron.enemies2)<20:
                    aarron.enemies2.append(Aarronenemy(aarron.rect.x+random.randint(120,130),aarron.rect.y+457-random.randint(85,95),2))
            elif difficulty =="e":
                if len(aarron.enemies2)<20:
                    aarron.enemies2.append(Aarronenemy(aarron.rect.x+random.randint(90,95),aarron.rect.y+457-random.randint(85,95),2))
        #remove aarron when dead
        if aarron.health<=0:
            aarrons.remove(aarron)
        if display:
            screen.blit(aarronship,(aarron.rect.x,aarron.rect.y))
        else:
            pygame.draw.rect(screen,red,aarron.rect)
        pygame.draw.rect(screen,red,pygame.Rect(aarron.rect.x+300,aarron.rect.y,2,457))
        pygame.draw.rect(screen,green,pygame.Rect(aarron.rect.x+300,aarron.rect.y+457-((aarron.health*457)/aarron.maxhealth),2,(aarron.health*457)/aarron.maxhealth))
        for aarronenemy in aarron.enemies2:
            g1=random.choice([1,-1])
            g=g1
            aarronenemy.rect.x-=random.randint(8,12)
            aarronenemy.rect.y+=aarronenemy.randomangle
            if aarronenemy.rect.x<0 or aarronenemy.rect.y<0 or aarronenemy.rect.y>898:
                aarron.enemies2.remove(aarronenemy)
            if aarronenemy.rect.colliderect(player.rect):
                try:
                    aarron.enemies2.remove(aarronenemy)
                except:
                    pass
                channel23.play(player.hitsound)
                if display:
                    player.exptime=time.time()
                    player.expmarker=exp1
                player.health-=1
            pygame.draw.rect(screen,red,aarronenemy.rect)
        if g1>0 and g>-1:
            g-=0.024
        if g1<0 and g<1:
            g+=0.024
        aarron.enemies1=aarron.enemies1[::-1]
        for aarronenemy in aarron.enemies1:
            aarronenemy.time+=1
            aarronenemy.rect.x-=20
            if aarronenemy.time>1:
                aarronenemy.rect.y-=2*g
            aarronenemy.rect.y+=10*g
            if aarronenemy.rect.x<0 or aarronenemy.rect.y<0 or aarronenemy.rect.y>898:
                aarron.enemies1.remove(aarronenemy)
            if aarronenemy.rect.colliderect(player.rect):
                try:
                    aarron.enemies1.remove(aarronenemy)
                except:
                    pass
                channel23.play(player.hitsound)
                if display:
                    player.exptime=time.time()
                    player.expmarker=exp1
                player.health-=1
            pygame.draw.rect(screen,blue,aarronenemy.rect)

    #handles joshs attacks
    for josh in joshs:
        if difficulty=="h":
            if josh.rect.x > 1350:
                josh.move(-2, 0)
            elif len(josh.enemies1) < 4:
                josh.enemies1.append(Joshenemy(josh.rect.x + 70, josh.rect.y + 300, japchars))
                josh.enemies1[-1].time = time.time()
        elif difficulty=="m":
            if josh.rect.x>1350:
                josh.move(-1,0)
            elif len(josh.enemies1)<3:
                josh.enemies1.append(Joshenemy(josh.rect.x+70,josh.rect.y+300,japchars))
                josh.enemies1[-1].time=time.time()
        elif difficulty=="e":
            if josh.rect.x > 1350:
                josh.move(-1, 0)
            elif len(josh.enemies1) < 3:
                josh.enemies1.append(Joshenemy(josh.rect.x + 55, josh.rect.y + 300, japchars))
                josh.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(josh):
                josh.health-=1
                player.shots.remove(shot)
        if josh.health<=0:
            joshs.remove(josh)
        for joshenemy in josh.enemies1:
            if joshenemy.rect.y+100>player.rect.y+25:
                joshenemy.deltay-=joshenemy.deltax/100
            if joshenemy.rect.y+100<player.rect.y+25:
                joshenemy.deltay+=joshenemy.deltax/100
            joshenemy.rect.x-=joshenemy.deltax
            joshenemy.rect.y+=joshenemy.deltay
            if joshenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                josh.enemies1.remove(joshenemy)
                if display:
                    player.exptime=time.time()
                    player.expmarker=exp1
                player.health-=5
            if joshenemy.rect.x<-200 or joshenemy.rect.y<-200 or joshenemy.rect.y>1100:
                josh.enemies1.remove(joshenemy)
            if display:
                screen.blit(joshenemy.image,(joshenemy.rect.x,joshenemy.rect.y))
            else:
                pygame.draw.rect(screen,orange,joshenemy.rect)
        if display:
            screen.blit(joshship,(josh.rect.x,josh.rect.y))
        else:
            pygame.draw.rect(screen,blue,josh.rect)
        pygame.draw.rect(screen,red,pygame.Rect(josh.rect.x+245,josh.rect.y,2,457))
        pygame.draw.rect(screen,green,pygame.Rect(josh.rect.x+245,josh.rect.y+457-((josh.health*457)/josh.maxhealth),2,(josh.health*457)/josh.maxhealth))

    # handles banners attacks
    for banner in banners:
        if difficulty=="h":
            if banner.rect.x > 1000:
                banner.move(-4, 0)
            elif len(banner.enemies1) < 51:
                banner.enemies1.append(Bannerenemy(banner.rect.x + random.randint(140, 250), banner.rect.y + random.randint(200, 270), 2))
                banner.enemies1[-1].time = time.time()
        elif difficulty=="m":
            if banner.rect.x > 1000:
                banner.move(-4, 0)
            elif len(banner.enemies1) < 41:
                banner.enemies1.append(Bannerenemy(banner.rect.x+random.randint(100,175),banner.rect.y+random.randint(200,270),2))
                banner.enemies1[-1].time = time.time()
        elif difficulty=="e":
            if banner.rect.x > 1000:
                banner.move(-4, 0)
            elif len(banner.enemies1) < 26:
                banner.enemies1.append(Bannerenemy(banner.rect.x + random.randint(80, 130), banner.rect.y + random.randint(200, 270), 2))
                banner.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(banner):
                banner.health -= 1
                player.shots.remove(shot)
        if banner.health <= 0:
            banners.remove(banner)
        for bannerenemy in banner.enemies1:
            if difficulty=="h":
                if bannerenemy.rect.y + 100 > player.rect.y + 25:
                    bannerenemy.deltay -= bannerenemy.deltax / 150
                if bannerenemy.rect.y + 100 < player.rect.y + 25:
                    bannerenemy.deltay += bannerenemy.deltax / 150
            elif difficulty=="m":
                if bannerenemy.rect.y + 100 > player.rect.y + 25:
                    bannerenemy.deltay -= bannerenemy.deltax / 200
                if bannerenemy.rect.y + 100 < player.rect.y + 25:
                    bannerenemy.deltay += bannerenemy.deltax / 200
            elif difficulty=="e":
                if bannerenemy.rect.y + 100 > player.rect.y + 25:
                    bannerenemy.deltay -= bannerenemy.deltax / 300
                if bannerenemy.rect.y + 100 < player.rect.y + 25:
                    bannerenemy.deltay += bannerenemy.deltax / 300
            bannerenemy.rect.x -= bannerenemy.deltax
            bannerenemy.rect.y += bannerenemy.deltay
            if bannerenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                banner.enemies1.remove(bannerenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                if difficulty=="h":
                    player.health-=2
                elif difficulty=="m":
                    player.health -= 2
                elif difficulty=="e":
                    player.health-=1
            if bannerenemy.rect.x < -200 or bannerenemy.rect.y < -200 or bannerenemy.rect.y > 1100:
                banner.enemies1.remove(bannerenemy)
            if display:
                #screen.blit(bannerenemy.image, (bannerenemy.rect.x, bannerenemy.rect.y))
                pygame.draw.rect(screen, orange, bannerenemy.rect)
            else:
                pygame.draw.rect(screen, orange, bannerenemy.rect)
        if display:
            screen.blit(bannership, (banner.rect.x, banner.rect.y))
        else:
            pygame.draw.rect(screen, blue, banner.rect)
        #health bar
        pygame.draw.rect(screen, red, pygame.Rect(banner.rect.x + 330, banner.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(banner.rect.x + 330, banner.rect.y + 457 - ((banner.health * 457) / banner.maxhealth), 2, (banner.health * 457) / banner.maxhealth))

    # handles cringes attacks
    for cringe in cringes:
        if cringe.rect.x > 1350:
            cringe.move(-3, 0)
        elif len(cringe.enemies1) < 3:
            cringe.enemies1.append(Cringeenemy(cringe.rect.x + 100, cringe.rect.y + 300, japchars))
            cringe.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(cringe):
                cringe.health -= 1
                player.shots.remove(shot)
        if cringe.health <= 0:
            cringes.remove(cringe)
        for cringeenemy in cringe.enemies1:
            if cringeenemy.rect.y + 100 > player.rect.y + 25:
                cringeenemy.deltay -= cringeenemy.deltax / 100
            if cringeenemy.rect.y + 100 < player.rect.y + 25:
                cringeenemy.deltay += cringeenemy.deltax / 100
            cringeenemy.rect.x -= cringeenemy.deltax
            cringeenemy.rect.y += cringeenemy.deltay
            if cringeenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                cringe.enemies1.remove(cringeenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if cringeenemy.rect.x < -200 or cringeenemy.rect.y < -200 or cringeenemy.rect.y > 1100:
                cringe.enemies1.remove(cringeenemy)
            if display:
                screen.blit(cringeenemy.image, (cringeenemy.rect.x, cringeenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, cringeenemy.rect)
        if display:
            screen.blit(cringeship, (cringe.rect.x, cringe.rect.y))
        else:
            pygame.draw.rect(screen, blue, cringe.rect)
        pygame.draw.rect(screen, red, pygame.Rect(cringe.rect.x + 245, cringe.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(cringe.rect.x + 245, cringe.rect.y + 457 - ((cringe.health * 457) / cringe.maxhealth), 2, (cringe.health * 457) / cringe.maxhealth))

    # handles burkes attacks
    for burke in burkes:
        if burke.rect.x > 1350:
            burke.move(-1, 0)
        elif len(burke.enemies1) < 3:
            burke.enemies1.append(Burkeenemy(burke.rect.x + 100, burke.rect.y + 300, japchars))
            burke.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(burke):
                burke.health -= 1
                player.shots.remove(shot)
        if burke.health <= 0:
            burkes.remove(burke)
        for burkeenemy in burke.enemies1:
            if burkeenemy.rect.y + 100 > player.rect.y + 25:
                burkeenemy.deltay -= burkeenemy.deltax / 100
            if burkeenemy.rect.y + 100 < player.rect.y + 25:
                burkeenemy.deltay += burkeenemy.deltax / 100
            burkeenemy.rect.x -= burkeenemy.deltax
            burkeenemy.rect.y += burkeenemy.deltay
            if burkeenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                burke.enemies1.remove(burkeenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if burkeenemy.rect.x < -200 or burkeenemy.rect.y < -200 or burkeenemy.rect.y > 1100:
                burke.enemies1.remove(burkeenemy)
            if display:
                screen.blit(burkeenemy.image, (burkeenemy.rect.x, burkeenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, burkeenemy.rect)
        if display:
            screen.blit(burkeship, (burke.rect.x, burke.rect.y))
        else:
            pygame.draw.rect(screen, blue, burke.rect)
        pygame.draw.rect(screen, red, pygame.Rect(burke.rect.x + 245, burke.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(burke.rect.x + 245, burke.rect.y + 457 - ((burke.health * 457) / burke.maxhealth), 2, (burke.health * 457) / burke.maxhealth))

    # handles diggers attacks
    for digger in diggers:
        if digger.rect.x > 1350:
            digger.move(-1, 0)
        elif len(digger.enemies1) < 3:
            digger.enemies1.append(Diggerenemy(digger.rect.x + 100, digger.rect.y + 300, japchars))
            digger.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(digger):
                digger.health -= 1
                player.shots.remove(shot)
        if digger.health <= 0:
            diggers.remove(digger)
        for diggerenemy in digger.enemies1:
            if diggerenemy.rect.y + 100 > player.rect.y + 25:
                diggerenemy.deltay -= diggerenemy.deltax / 100
            if diggerenemy.rect.y + 100 < player.rect.y + 25:
                diggerenemy.deltay += diggerenemy.deltax / 100
            diggerenemy.rect.x -= diggerenemy.deltax
            diggerenemy.rect.y += diggerenemy.deltay
            if diggerenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                digger.enemies1.remove(diggerenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if diggerenemy.rect.x < -200 or diggerenemy.rect.y < -200 or diggerenemy.rect.y > 1100:
                digger.enemies1.remove(diggerenemy)
            if display:
                screen.blit(diggerenemy.image, (diggerenemy.rect.x, diggerenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, diggerenemy.rect)
        if display:
            screen.blit(diggership, (digger.rect.x, digger.rect.y))
        else:
            pygame.draw.rect(screen, blue, digger.rect)
        pygame.draw.rect(screen, red, pygame.Rect(digger.rect.x + 245, digger.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(digger.rect.x + 245, digger.rect.y + 457 - ((digger.health * 457) / digger.maxhealth), 2, (digger.health * 457) / digger.maxhealth))

    # handles salmans attacks
    for salman in salmans:
        if salman.rect.x > 1350:
            salman.move(-1, 0)
        elif len(salman.enemies1) < 3:
            salman.enemies1.append(Salmanenemy(salman.rect.x + 100, salman.rect.y + 300, japchars))
            salman.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(salman):
                salman.health -= 1
                player.shots.remove(shot)
        if salman.health <= 0:
            salmans.remove(salman)
        for salmanenemy in salman.enemies1:
            if salmanenemy.rect.y + 100 > player.rect.y + 25:
                salmanenemy.deltay -= salmanenemy.deltax / 100
            if salmanenemy.rect.y + 100 < player.rect.y + 25:
                salmanenemy.deltay += salmanenemy.deltax / 100
            salmanenemy.rect.x -= salmanenemy.deltax
            salmanenemy.rect.y += salmanenemy.deltay
            if salmanenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                salman.enemies1.remove(salmanenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if salmanenemy.rect.x < -200 or salmanenemy.rect.y < -200 or salmanenemy.rect.y > 1100:
                salman.enemies1.remove(salmanenemy)
            if display:
                screen.blit(salmanenemy.image, (salmanenemy.rect.x, salmanenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, salmanenemy.rect)
        if display:
            screen.blit(salmanship, (salman.rect.x, salman.rect.y))
        else:
            pygame.draw.rect(screen, blue, salman.rect)
        pygame.draw.rect(screen, red, pygame.Rect(salman.rect.x + 245, salman.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(salman.rect.x + 245, salman.rect.y + 457 - ((salman.health * 457) / salman.maxhealth), 2, (salman.health * 457) / salman.maxhealth))

    # handles dans attacks
    for dan in dans:
        if dan.rect.x > 1350:
            dan.move(-1, 0)
        elif len(dan.enemies1) < 3:
            dan.enemies1.append(Tonesenemy(dan.rect.x + 100, dan.rect.y + 300, japchars))
            dan.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(dan):
                dan.health -= 1
                player.shots.remove(shot)
        if dan.health <= 0:
            dans.remove(dan)
        for danenemy in dan.enemies1:
            if danenemy.rect.y + 100 > player.rect.y + 25:
                danenemy.deltay -= danenemy.deltax / 100
            if danenemy.rect.y + 100 < player.rect.y + 25:
                danenemy.deltay += danenemy.deltax / 100
            danenemy.rect.x -= danenemy.deltax
            danenemy.rect.y += danenemy.deltay
            if danenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                dan.enemies1.remove(danenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if danenemy.rect.x < -200 or danenemy.rect.y < -200 or danenemy.rect.y > 1100:
                dan.enemies1.remove(danenemy)
            if display:
                screen.blit(danenemy.image, (danenemy.rect.x, danenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, danenemy.rect)
        if display:
            screen.blit(danship, (dan.rect.x, dan.rect.y))
        else:
            pygame.draw.rect(screen, blue, dan.rect)
        pygame.draw.rect(screen, red, pygame.Rect(dan.rect.x + 245, dan.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(dan.rect.x + 245, dan.rect.y + 457 - ((dan.health * 457) / dan.maxhealth), 2, (dan.health * 457) / dan.maxhealth))

    # handles nialls attacks
    for niall in nialls:
        if niall.rect.x > 1350:
            niall.move(-1, 0)
        elif len(niall.enemies1) < 3:
            niall.enemies1.append(Niallenemy(niall.rect.x + 100, niall.rect.y + 300, japchars))
            niall.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(niall):
                niall.health -= 1
                player.shots.remove(shot)
        if niall.health <= 0:
            nialls.remove(niall)
        for niallenemy in niall.enemies1:
            if niallenemy.rect.y + 100 > player.rect.y + 25:
                niallenemy.deltay -= niallenemy.deltax / 100
            if niallenemy.rect.y + 100 < player.rect.y + 25:
                niallenemy.deltay += niallenemy.deltax / 100
            niallenemy.rect.x -= niallenemy.deltax
            niallenemy.rect.y += niallenemy.deltay
            if niallenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                niall.enemies1.remove(niallenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if niallenemy.rect.x < -200 or niallenemy.rect.y < -200 or niallenemy.rect.y > 1100:
                niall.enemies1.remove(niallenemy)
            if display:
                screen.blit(niallenemy.image, (niallenemy.rect.x, niallenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, niallenemy.rect)
        if display:
            screen.blit(niallship, (niall.rect.x, niall.rect.y))
        else:
            pygame.draw.rect(screen, blue, niall.rect)
        pygame.draw.rect(screen, red, pygame.Rect(niall.rect.x + 245, niall.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(niall.rect.x + 245, niall.rect.y + 457 - ((niall.health * 457) / niall.maxhealth), 2, (niall.health * 457) / niall.maxhealth))

    # handles andrews attacks
    for andrew in andrews:
        if andrew.rect.x > 1350:
            andrew.move(-1, 0)
        elif len(andrew.enemies1) < 3:
            andrew.enemies1.append(Andrewenemy(andrew.rect.x + 100, andrew.rect.y + 300, japchars))
            andrew.enemies1[-1].time = time.time()
        for shot in player.shots:
            if shot.colliderect(andrew):
                andrew.health -= 1
                player.shots.remove(shot)
        if andrew.health <= 0:
            andrews.remove(andrew)
        for andrewenemy in andrew.enemies1:
            if andrewenemy.rect.y + 100 > player.rect.y + 25:
                andrewenemy.deltay -= andrewenemy.deltax / 100
            if andrewenemy.rect.y + 100 < player.rect.y + 25:
                andrewenemy.deltay += andrewenemy.deltax / 100
            andrewenemy.rect.x -= andrewenemy.deltax
            andrewenemy.rect.y += andrewenemy.deltay
            if andrewenemy.rect.colliderect(player.rect):
                channel23.play(player.hitsound)
                andrew.enemies1.remove(andrewenemy)
                if display:
                    player.exptime = time.time()
                    player.expmarker = exp1
                player.health -= 5
            if andrewenemy.rect.x < -200 or andrewenemy.rect.y < -200 or andrewenemy.rect.y > 1100:
                andrew.enemies1.remove(andrewenemy)
            if display:
                screen.blit(andrewenemy.image, (andrewenemy.rect.x, andrewenemy.rect.y))
            else:
                pygame.draw.rect(screen, orange, andrewenemy.rect)
        if display:
            screen.blit(andrewship, (andrew.rect.x, andrew.rect.y))
        else:
            pygame.draw.rect(screen, blue, andrew.rect)
        pygame.draw.rect(screen, red, pygame.Rect(andrew.rect.x + 245, andrew.rect.y, 2, 457))
        pygame.draw.rect(screen, green, pygame.Rect(andrew.rect.x + 245, andrew.rect.y + 457 - ((andrew.health * 457) / andrew.maxhealth), 2, (andrew.health * 457) / andrew.maxhealth))

    #when player lands a hit
    for shot in player.shots:
        if difficulty=="h":
            shot.x+=70
        elif difficulty=="m":
            shot.x+=50
        elif difficulty=="e":
            shot.x+=40
        if shot.x>=1600:
            player.shots.remove(shot)
        for enemy in enemies:
            if shot.colliderect(enemy.rect):
                channel23.play(player.hitsound)
                deadenemies.append(enemy)
                enemy.exptime=time.time()
                enemies.remove(enemy)
                try:
                    shotcollisions.append(Collision(shot.x,shot.y))
                    player.shots.remove(shot)
                except:
                    pass
        for items in [aarrons,joshs,banners,cringes,burkes,diggers,salmans,dans,nialls,andrews]:
            for item in items:
                if shot.colliderect(item.rect):
                    channel23.play(player.hitsound)
                    item.health-=1
                    try:
                        randomrectangleobjectidecidedtocreatefornogoddamnreason=Collision(shot.x,shot.y)
                        randomrectangleobjectidecidedtocreatefornogoddamnreason.exptime=time.time()
                        randomrectangleobjectidecidedtocreatefornogoddamnreason.rect.x+=random.randint(0,150)
                        shotcollisions.append(randomrectangleobjectidecidedtocreatefornogoddamnreason)
                        player.shots.remove(shot)
                    except:
                        pass
        if display:
            screen.blit(fireshot,(shot.x,shot.y))
        else:
            pygame.draw.rect(screen,blue,shot)

    #display sprites when textures enabled
    if display:
        for enemy in deadenemies:
            expanim(enemy)
            if time.time()-enemy.exptime>1.5:
                deadenemies.remove(enemy)
            screen.blit(enemy.expmarker,(enemy.rect.x-20,enemy.rect.y-5))
        for collision in shotcollisions:
            expanim(collision)
            if time.time()-collision.exptime>1.5:
                shotcollisions.remove(collision)
            screen.blit(collision.expmarker,(collision.rect.x,collision.rect.y-60))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()