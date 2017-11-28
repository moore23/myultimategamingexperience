try:
    with open("data/levels/1.txt","r")as f:
        folder="data/"
        f.close()
except:
    folder="gamelib/data/"
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
        self.randomangle=random.randint(-20,10)
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
japchars=[]
for file in os.listdir(folder+"sprites/japchar"):
    japchars.append(pygame.image.load(os.path.join(folder+"sprites/japchar",file)))
spriteLOC=folder+"sprites/"
lightblue=(221,160,221)
white=(255,255,255)
purple=(139,0,139)
level=startlevel=0
someothernumber=0
shotcollisions=[]
orange=(255,69,0)
blue=(0,255,255)
green=(0,255,0)
inoptions=False
deadenemies=[]
red=(255,0,0)
black=(0,0,0)
display=True
channels=[]
sometime=0
enemies=[]
aarrons=[]
joshs=[]
stars=[]
r=True
g1=0
g=0
os.environ["SDL_VIDEO_WINDOW_POS"]="0,0"
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1600,900),pygame.FULLSCREEN)
clock = pygame.time.Clock()
playership=pygame.image.load(spriteLOC+"player.gif")
enemyship=pygame.image.load(spriteLOC+"enemy.png")
aarronship=pygame.image.load(spriteLOC+"aarron.png")
joshship=pygame.image.load(spriteLOC+"josh.png")
titlebg=pygame.image.load(spriteLOC+"titlebg.png")
playrect=pygame.image.load(spriteLOC+"playrect.png")
optionrect=pygame.image.load(spriteLOC+"optionrect.png")
quitrect=pygame.image.load(spriteLOC+"quitrect.png")
exitrect=pygame.image.load(spriteLOC+"backrect.png")
right=pygame.image.load(spriteLOC+"right.png")
left=pygame.image.load(spriteLOC+"left.png")
selected=pygame.image.load(spriteLOC+"selected.png")
unselected=pygame.image.load(spriteLOC+"unselected.png")
fireshot=pygame.image.load(spriteLOC+"fire.png")
ticked=pygame.image.load(spriteLOC+"ticked.png")
cursor=pygame.image.load(spriteLOC+"cursor.png")
for file in os.listdir(spriteLOC+"explosions"):
    exec("exp{} = pygame.image.load(os.path.join(spriteLOC+'explosions',file))".format(file[:-4]))
shieldrect=pygame.image.load(spriteLOC+"shield.png")
actshieldrect=pygame.image.load(spriteLOC+"actshield.png")
class Collision(object):
    def __init__(self,wx,wy):
        self.rect=pygame.Rect(wx,wy,1,1)
        self.exptime=0
        self.expmarker=exp0
myfont=pygame.font.SysFont("Arial",30)
myfont.set_underline(True)
vollabel=myfont.render("VOLUME",0,white,black)
texlabel=myfont.render("TEXTURES?",0,white,black)
levlabel=myfont.render("LEVEL SELECT",0,white,black)
elabel=myfont.render("EASY",0,white,black)
mlabel=myfont.render("MEDIUM",0,white,black)
hlabel=myfont.render("HARD",0,white,black)
difficulty="m"
levlabels=[]
for file in os.listdir(folder+"levels"):
    levlabels.append(myfont.render(file[:-4],0,white,black))
player=Player()
player.maxhealth=player.health
player.sound=pygame.mixer.Sound(folder+"sounds/fire.wav")
player.hitsound=pygame.mixer.Sound(folder+"sounds/hit.wav")
player.shieldsound=pygame.mixer.Sound(folder+"sounds/shield.wav")
pygame.mixer.set_num_channels(25)
channel0=pygame.mixer.Channel(0)
channel1=pygame.mixer.Channel(1)
channel2=pygame.mixer.Channel(2)
channel3=pygame.mixer.Channel(3)
channel4=pygame.mixer.Channel(4)
channel5=pygame.mixer.Channel(5)
channel6=pygame.mixer.Channel(6)
channel7=pygame.mixer.Channel(7)
channel8=pygame.mixer.Channel(8)
channel9=pygame.mixer.Channel(9)
channel10=pygame.mixer.Channel(10)
channel11=pygame.mixer.Channel(11)
channel12=pygame.mixer.Channel(12)
channel13=pygame.mixer.Channel(13)
channel14=pygame.mixer.Channel(14)
channel15=pygame.mixer.Channel(15)
channel16=pygame.mixer.Channel(16)
channel17=pygame.mixer.Channel(17)
channel18=pygame.mixer.Channel(18)
channel19=pygame.mixer.Channel(19)
channel20=pygame.mixer.Channel(20)
channel21=pygame.mixer.Channel(21)
channel22=pygame.mixer.Channel(22)
channel23=pygame.mixer.Channel(23)
channel24=pygame.mixer.Channel(24)
enemychannels=[channel3,channel4,channel5,channel6,channel7,channel8,channel9,channel10,channel11,channel12,channel13,channel14,channel15,channel16,channel17,channel18,channel19,channel20,channel21,channel22]
volume=channel0.get_volume()
music1=pygame.mixer.Sound(folder+"music/josh.wav")
music2=pygame.mixer.Sound(folder+"music/aarron.wav")
for turn in range(500):
    stars.append(Star(random.randint(0,1598),random.randint(0,898)))
def deletealllists():
    global enemies,aarrons,joshs
    enemies=[]
    aarrons=[]
    joshs=[]
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
def startmenu(runningthefuckaway,someotherfuckingtime):
    global volume,display,inoptions,r,someothernumber,startlevel,difficulty
    someotherfuckingtime=time.time()
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
            screen.blit(texlabel,(734,500))
            screen.blit(exitrect,(638,600))
            screen.blit(left,(638,438))
            screen.blit(right,(938,438))
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
player.exptime=0
player.expmarker=exp1
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
    if level>=6 and level<13:
        if not channel0.get_busy():
            channel0.play(music1)
    else:
        channel0.stop()
    if level>1 and (len(aarrons)>0 or level<6):
        if not channel2.get_busy():
            channel2.play(music2)
    else:
        channel2.stop()
    if len(enemies)+len(aarrons)+len(joshs)==0:
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
                            if letter in"Ee":
                                for turn in range(number):
                                    enemies.append(Enemy())
                            if letter in"Aa":
                                for turn in range(number):
                                    aarrons.append(Boss())
                                if len(aarrons)==2:
                                    aarrons[0].rect.y=0
                                    aarrons[1].rect.y=450
                                try:
                                    aarrons[0].stage=aarrons[1].stage=1
                                except:
                                    aarrons[0].stage=1
                            if letter in"Jj":
                                for turn in range(number):
                                    joshs.append(Boss())
                                if len(joshs)==2:
                                    joshs[0].rect.y=0
                                    joshs[1].rect.y=450
        except:
            level=startlevel
            startmenu(True,sometime)
        if level==startlevel+1:
            if difficulty=="h":
                player.maxhealth=50
                for items in [aarrons,joshs]:
                    for item in items:
                        item.maxhealth=item.health=50
            elif difficulty=="m":
                player.maxhealth=75
                for items in [aarrons,joshs]:
                    for item in items:
                        item.maxhealth=item.health=40
            elif difficulty=="e":
                player.maxhealth=100
                for items in [aarrons,joshs]:
                    for item in items:
                        item.maxhealth=item.health=30
            player.health=player.maxhealth
        somefuckingnumber=0
        for enemy in enemies:
            enemy.sound=pygame.mixer.Sound(folder+"sounds/fire.wav")
            enemy.channel=enemychannels[somefuckingnumber]
            somefuckingnumber+=1
    if player.health<=0:
        level=startlevel
        deletealllists()
    user_input=pygame.key.get_pressed()
    if user_input[pygame.K_w]:
        player.move(0,-10)
    if user_input[pygame.K_s]:
        player.move(0,10)
    if user_input[pygame.K_a]:
        player.move(-10,0)
    if user_input[pygame.K_d]:
        player.move(10,0)
    if user_input[pygame.K_SPACE]and time.time()-player.shottime>0.5:
        player.shottime=time.time()
        player.shoot()
        channel1.play(player.sound)
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
    if time.time()-player.specialtime<0.25:
        screen.blit(shieldrect,(player.rect.x-102,player.rect.y-102))
    elif time.time()-player.specialtime<0.5:
        screen.blit(actshieldrect,(player.rect.x-115,player.rect.y-102))
    if display:
        screen.blit(playership,(player.rect.x,player.rect.y+1))
        pygame.draw.rect(screen,white,pygame.Rect(player.rect.x-1,player.rect.y-1,4,52))
    else:
        pygame.draw.rect(screen,white,player.rect)
    pygame.draw.rect(screen,red,pygame.Rect(player.rect.x,player.rect.y,2,50))
    pygame.draw.rect(screen,green,pygame.Rect(player.rect.x,player.rect.y+50-((player.health*50)/player.maxhealth),2,(player.health*50)/player.maxhealth))
    if display:
        expanim(player)
        screen.blit(player.expmarker,(player.rect.x-40,player.rect.y-40))
    for enemy in enemies:
        if enemy.rect.x > enemy.boundary:
            enemy.move(-5,0)
        enemy.shot.x-=20
        enemy.move(0,enemy.speed)
        if enemy.shot.x<0:
            enemy.channel.play(enemy.sound)
            enemy.shot.x=enemy.rect.x
            enemy.shot.y=enemy.rect.y+48
        if enemy.shot.colliderect(player.rect):
            channel23.play(player.hitsound)
            player.exptime=time.time()
            player.expmarker=exp1
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
                    aarron.enemies1.append(Bossenemy(aarron.rect.x+random.randint(175,185),aarron.rect.y+random.randint(200,210),20))
                    aarron.sometimesihatemyself=time.time()
            except:
                aarron.sometimesihatemyself=time.time()
        elif aarron.stage==-1:
            aarron.enemies1=[]
            if len(aarron.enemies2)<20:
                aarron.enemies2.append(Bossenemy(aarron.rect.x+random.randint(120,130),aarron.rect.y+457-random.randint(85,95),2))
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
    for josh in joshs:
        if josh.rect.x>1350:
            josh.move(-1,0)
        elif len(josh.enemies1)<3:
            josh.enemies1.append(Joshenemy(josh.rect.x+100,josh.rect.y+300,japchars))
            josh.enemies1[-1].time=time.time()
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
    for shot in player.shots:
        shot.x+=20
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
        for items in [aarrons,joshs]:
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
