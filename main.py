from ast import Try
from distutils.log import error
import pygame, time, sys, os ,dotenv, random, math, pathlib
from pygame.locals import *
from pygame import mixer
from Player_1 import Player1
from Player_2 import Player2
from operator import itemgetter

ver = "1.7.4"

loading = True
load_log = []
pygame.init()
res = (1920, 1080)
wn = pygame.display.set_mode((res))
mainClock = pygame.time.Clock()
missingtex = pygame.image.load("BG/missing Texture.png").convert_alpha()
load_log.append(
    "BG/missing texture.png"
)
initial_count = 0
fail = pygame.image.load("BG/LOAD FAIL.png").convert_alpha()
load_log.append(
    "BG/LOAD FAIL.PNG"
)
print(load_log)
dir = "maps"

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)) or os.path.isdir(os.path.join(dir, path)):
        initial_count += 1
"""try:
    loadingimg = pygame.image.load()
except:
    quit()

while loading:
    wn.blit(loadingimg, (0,0))
"""

print(f"data-{initial_count} map files found")
zones = []
zoneimg = []
zoneimgpath = []
zoneimg_small = []
zonemusic = []
known_ERRORS = []
for i in range(initial_count):
            
    try:
        zonesel = (f'zone{i}')
        pathname = (f'maps/{zonesel}/mapdata.env')
        with open(pathname):
            print(f"data-found path - {pathname}")

            dotenv_path = (pathname)
            
            dotenv.load_dotenv(dotenv_path=dotenv_path, override=True)
            zone = os.environ.get("zonename")
            zones.append(zone)
    except IOError or FileNotFoundError:
        print(f'Error-IOError or File Not Found - {pathname}')
        known_ERRORS.append(f"Error-IOError or File Not Found - {pathname}")
for i in range(initial_count):
    try:
        zonesel = (f'zone{i}')
        pathname = (f'maps/{zonesel}/zoneBG.png')
        
        with open(pathname):
            print(f'data-found path - {pathname}')
            zoneimg.append(pygame.image.load(pathname).convert())
            pathnametran = pygame.image.load(pathname).convert_alpha()
            pathnametran = pygame.transform.scale(pathnametran, (674, 449))
            zoneimg_small.append(pathnametran)
            zoneimgpath.append(pathname)
    except IOError or FileNotFoundError:
        
        print(f'Error-IOError or File Not Found - {pathname}')
        known_ERRORS.append(f"Error-IOError or File Not Found - {pathname}")
        zoneimg.append(pygame.image.load("BG/missing Texture.png").convert_alpha())
        pathname = "BG\missing Texture.png"
        zoneimgpath.append(pathname)
for i in range(initial_count):
    try:
        zonesel = (f'zone{i}')
        pathname = (f'maps{zonesel}/zonemusic.mp3')
        zonemusic.append(pygame.mixer.Sound(pathname))
        print(f'data-found path - {pathname}')
    except IOError or FileNotFoundError:
        print(f'Error-IOError or File Not Found - {pathname}')
        known_ERRORS.append(f"Error-IOError or File Not Found - {pathname}")
                

print(f"data-all zones - {zones}")
print(f'data-zone imgs {zoneimg}')
print(f'data-zone icons created - {zoneimg_small}')
print(f'data-zone music {zonemusic}')
print(f'data-paths find {zoneimgpath}')
#print("wait-sleeping")


#there is a new glitch i have never seen after the code here
    
    



#var
initial_count = 0
RED = (255,0,0)
GREEN = (0,255,0)
grav = 10
debug = 1
debugon = True
mousex = 0
mousey = 0 
start_screen = True
playersel = False
player1_Girl = False
player1_Boy = False
player2_Boy = False
player2_Girl = False
zone_sel = False
stage_1 = False
stage_2 = False
stage_3 = False
pause_menu = False
sel = 0

run = True
mousepressed = 0
P1X = 216
P1Y = 627
P2X = 1700
P2Y = 629
jump1go = 0
jump2go = 0
walkcount = 0
rightboy = False
rightgirl = False


font = pygame.font.Font(None,20)
black = pygame.image.load("BG/black.png").convert()
load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
wn.blit(black, (0,0))
wn.blit(load_log_render, (0,0))

pygame.display.update()

#img
print("data-loading imgs")
load_log.append("data-loading imgs")

try:
    BG = pygame.image.load("BG/bg.png").convert_alpha()
    load_log.append("BG/bg.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 27.27, 25))
    pygame.display.update()
    
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-BG")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    idleboy = pygame.image.load("Char/BOY/IdleBoy.png").convert_alpha()
    load_log.append("Char/BOY/IdleBoy.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 54.54, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-idleboy")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    idlegirl = pygame.image.load('Char/GIRL/idlegirl.png').convert_alpha()
    load_log.append('Char/GIRL/idlegirl.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 81.81, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-idlegirl")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    pointer = pygame.image.load("pointer/pointer.png").convert_alpha()
    load_log.append("pointer/pointer.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 109.08, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-pointer")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    startBG = pygame.image.load('start screen/StartBG.png').convert_alpha()
    load_log.append('start screen/StartBG.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 136.35, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-startBG")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    start_button = pygame.image.load("start screen/start_button.png").convert_alpha()
    load_log.append("start screen/start_button.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 163.62, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-start_button")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    start_button_click = pygame.image.load("start screen/start_button_cliced.png").convert_alpha()
    load_log.append("start screen/start_button_cliced.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 190.89, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-start_button_click")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    player_sel = pygame.image.load('start screen/player sel.png').convert_alpha()
    load_log.append('start screen/player sel.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 218.16, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-player_sel")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button_box = pygame.image.load('start screen/button_box.png').convert_alpha()
    load_log.append('start screen/button_box.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 245.43, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button_box")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button_box_blue = pygame.image.load("start screen/button_box_blue.png").convert_alpha()
    load_log.append("start screen/button_box_blue.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 272.7, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button_box_blue")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    zone_sel_png = pygame.image.load("BG/select stage.png").convert()
    load_log.append("BG/select stage.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 299.97, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-zone_sel_png")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button_box_green = pygame.image.load('start screen/button_box_green.png').convert_alpha()
    load_log.append('start screen/button_box_green.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 327.24, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button_box_green")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button_rec_blue = pygame.image.load('start screen/button_rec_Blue.png').convert_alpha()
    load_log.append('start screen/button_rec_Blue.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 354.51, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button_rec_blue")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button_rec_red = pygame.image.load('start screen/button_rec_Red.png').convert_alpha()
    load_log.append('start screen/button_rec_Red.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 381.78, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button_rec_red")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    volcano_stage = pygame.image.load("BG/sample_volcano.png").convert()
    load_log.append("BG/sample_volcano.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 409.05, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-volcano_stage")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    stadium = pygame.image.load('start screen/stadium.png').convert()
    load_log.append('start screen/stadium.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 436.32, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-stadium")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    forest = pygame.image.load("start screen/forest.png").convert()
    load_log.append("start screen/forest.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 463.59, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-forest")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    player1win = pygame.image.load('start screen/player1win.png').convert_alpha()
    load_log.append('start screen/player1win.png')
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 490.86, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-player1win")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    button1_for_zonesel = pygame.image.load("start screen/reeeee.png").convert_alpha()
    load_log.append("start screen/reeeee.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 518.13, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-button1_for_zonesel")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try: 
    prev_button = pygame.image.load("start screen\prev.png").convert_alpha()
    load_log.append("start screen\prev.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 545.4, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-prev_button")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try: 
    next_button = pygame.image.load("start screen/next_button.png").convert_alpha()
    load_log.append("start screen/next_button.png")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 572.67, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-next_button")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
try:
    player2win = pygame.image.load("start screen/player2win.png").convert_alpha()
    load_log.append("start screen/player2win.png")
    print("data-imgs loaded")
    load_log.append("data-imgs loaded")
    load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
    wn.blit(black, (0,0))
    wn.blit(load_log_render, (0,0))
    pygame.draw.rect(wn, (255,255,255), (650, 550, 600, 25))
    pygame.draw.rect(wn, (0,0,255), (650, 550, 600, 25))
    pygame.display.update()
except:
    print("FATAL ERROR- main sprites faild to load or somthing is missing-player2win")
    print("ending program")
    wn.blit(fail, (0,0))
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    running = 0
print(f'load log - {load_log}')
load_log_render = font.render((f'load log - {load_log}'),True,(255,255,255))
wn.blit(black, (0,0))
wn.blit(load_log_render, (0,0))
pygame.display.update()
#sounds
punch_sound = pygame.mixer.Sound("SOUNDS/punch.wav")

#def
def game_render():
    global mousex, mousey
    mousex, mousey = player1.mouse
   
    wn.blit(pointer, (player1.mouse))
   


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    def draw(self, hp):
        # update with new health
        self.hp = hp
        # calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(wn, RGB, (self.x, self.y, 600, 25))
        pygame.draw.rect(wn, RGG, (self.x, self.y, 600 * ratio, 25))




def play():
    global walkcount, P1Y,P1X,P2X,P2Y, jump1go, jump2go
    
    if P1Y < 687:
        P1Y += (grav)
    if player1.jump1 and P1Y > 680:
        jump2go = 25
    if player1.right1:
        P1X += 10
    if player1.left1:
        P1X -= 10
        player1.update()
        #player1.draw()
        #wn.blit(player1.image, (P1X, P1Y))

    keystate = pygame.key.get_pressed()
    
    if keystate[pygame.K_b]:
        sel += 1
    if keystate[pygame.K_v]:
        sel -= 1
    if P2Y < 647:
         P2Y += (grav)
    if keystate[pygame.K_i] and P2Y > 600:
        jump1go = 25
        
    if keystate[pygame.K_l]:
        P2X += 5
        
    if keystate[pygame.K_j]:
        P2X -= 5
    if jump1go > 0:
        P2Y -= jump1go
        jump1go -= 1
    if jump2go > 0:
        P1Y -= jump2go
        jump2go -= 1
    player2.update()
    #player2.draw()
    #wn.blit(player2.image, (P2X, P2Y))
    
            
    player1_health_bar.draw(player1.hp)
    player2_health_bar.draw(player2.hp)

    #walking and ani

    walkcount += 1
    if walkcount >=32:
        walkcount = 0
    
    
    def attack(self):
        rand = random.randint(-5,5)
        if player1.punch:
            player1.damage = self.strength + rand
        else:
            player2.damage = self.strength + rand
    #boy movement
    distance = math.sqrt ((math.pow(P1X-P2X,2)) + (math.pow(P1Y-P2Y,2)))
    if player1.punch and distance < 150 and walkcount > 25:
        if player1.faceR:
            P2X += 20
        elif player1.faceL:
            P2X -= 20
        pygame.mixer.Sound.play(punch_sound)
        player2.hp -= player1.damage
    if player2.punch and distance < 150 and walkcount > 25:
        if player2.faceR:
            P1X += 30
        elif player2.faceL:
            P1X -= 30
        pygame.mixer.Sound.play(punch_sound)
        player1.hp -= player2.damage

    if player1.right1 and player1.punch:
        wn.blit(player1.punk[walkcount // 7], (P1X,P1Y))
    elif player1.right1:    
        wn.blit(player1.image[walkcount // 5], (P1X,P1Y))
    

    idleboy_left = pygame.transform.flip(idleboy,True,False)
    if player1.left1 and player1.punch:
        wn.blit(player1.punkL[walkcount // 7], (P1X,P1Y))
    elif player1.left1:
        wn.blit(player1.imageL[walkcount // 5], (P1X,P1Y))

    elif player1.punch and player1.faceR:
        wn.blit(player1.punk[walkcount // 7], (P1X,P1Y))
    elif player1.punch and player1.faceL:
        wn.blit(player1.punkL[walkcount // 7],(P1X,P1Y))
    elif player1.left1 == False and player1.right1 == False and player1.faceR:
        wn.blit(idleboy, (P1X, P1Y))
    elif player1.left1 == False and player1.right1 == False and player1.faceL:
        wn.blit(idleboy_left, (P1X,P1Y))
    elif player1.punch and player1.faceR:
        wn.blit(player1.punk[walkcount // 7], (P1X,P1Y))
    elif player1.punch and player1.faceL:
        wn.blit(player1.punkL[walkcount // 7],(P1X,P1Y))
    

    #girl movement
    player2.update()
    idlegirl_left = pygame.transform.flip(idlegirl,True,False)
    if player2.right2 and player2.punch:
        wn.blit(player2.punk[walkcount // 8], (P2X,P2Y))
    elif player2.right2:
        wn.blit(player2.image[walkcount // 4], (P2X,P2Y))
    
    if player2.left2 and player2.punch:
        wn.blit(player2.punkL[walkcount // 8], (P2X, P2Y))
    elif player2.left2 and player2.punch == False:
        wn.blit(player2.imageL[walkcount // 4], (P2X, P2Y))
    
    
    elif player2.punch and player2.faceR:
        wn.blit(player2.punk[walkcount // 8], (P2X,P2Y))
    elif player2.punch and player2.faceL:
        wn.blit(player2.punkL[walkcount // 8],(P2X,P2Y))
    
    elif player2.left2 == False and player2.right2 == False and player2.faceR:
        wn.blit(idlegirl, (P2X, P2Y))
    elif player2.left2 == False and player2.right2 == False and player2.faceL:
        wn.blit(idlegirl_left, (P2X, P2Y))
    
    

clock = pygame.time.Clock()



player1 = Player1(70,20)
player2 = Player2(150,5)
player1_health_bar = HealthBar(50,50, player1.hp, player1.max_hp)
player2_health_bar = HealthBar(1250,50, player2.hp, player2.max_hp)
RGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RGG = (random.randint(50,255),random.randint(50,255),random.randint(50,255))
while run:
    clock.tick()
    #print(clock.get_fps())
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_g]:
            if debug == 1:
                debugon = True
            if debug == 0:
                debugon == False

    

    
    if pygame.mouse.get_visible():
                pygame.mouse.set_visible(False)
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0
            print('game quit')
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousepressed = 1
        print('mouse clicked')
    if event.type == pygame.MOUSEBUTTONUP:
        mousepressed = 0
          
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_y]:
            if debugon == False:
                debugon = True
            elif debugon == True:
                debugon = False
    #font renders
    font = pygame.font.Font(None,20)
    

    if start_screen:
        wn.blit(startBG, (0,0))
        """mapzone = font.render((f"loaded map files{zones}"),True,(0,0,0))
        mapzoneimg = font.render((f'loaded backgrounds{zoneimg}'),True,(0,0,0))
        mapzoneimg_small = font.render((f'loaded icons{zoneimg_small}'),True,(0,0,0))
        Errors = font.render((f'Errors {known_ERRORS}'),True,(0,0,0))"""
        
        #start button
        wn.blit(start_button, (895, 480))
        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552 and start_screen:
            wn.blit(start_button_click, (895, 480))

        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552 and mousepressed > 0 and start_screen:
            wn.blit(start_button_click, (895, 480))
            time.sleep(0.5)
            playersel = True
            start_screen = False
            mousepressed = 0
    

    
    font = pygame.font.Font(None,50)
    if playersel:
        wn.blit(player_sel, (0,0))
        
        #wn.blit(button_box, (113,192))

        if mousex > 1210 and mousex < 1837 and mousey > 178 and mousey < 767:
            wn.blit(button_box_blue, (1208, 180))
            if mousepressed > 0:
                player1_Girl = False
                player1_Boy = True
                player2_Girl = True
                player2_Boy = False
                
                
                
        if mousex > 113 and mousex < 740 and mousey > 192 and mousey < 781:
            wn.blit(button_box, (113, 192))
            if mousepressed > 0:
                player1_Girl = True
                player2_Boy = False
                player1_boy = True
                player2_Girl = False
                
        if player1_Boy and mousepressed == 0:
            zone_sel = True
            playersel = False
            zone_update()
        if player1_Girl and mousepressed == 0:
            zone_sel = True
            playersel = False
            zone_update()
        if player2_Boy and mousepressed == 0:
            zone_sel = True
            playersel = False
            zone_update()
        if player2_Girl and mousepressed == 0:
            zone_sel = True
            playersel = False
            zone_update()
    

    def stage_1_music():
        mixer.music.load("SOUNDS/Mick Gordon - 11. BFG Division.mp3")
        mixer.music.play(1)

    def zone_update():
        global sel1, sel2, sel3, mapsel1_
        try:
            mapsel1 = f"{itemgetter(0+sel)(zoneimgpath)}"
        except:
            mapsel1 = pygame.image.load("BG/missing Texture.png").convert_alpha()
        
        try:
            sel1 = font.render((f"{itemgetter(0+sel)(zones)}"),True,(0,0,0))
            mapsel1_ = pygame.image.load(mapsel1).convert_alpha()
            
        except:
            print(error)
        try:
            sel2 = font.render((f"{itemgetter(1+sel)(zones)}"),True,(0,0,0))
        except:
            print(error)
        try:
            sel3 = font.render((f"{itemgetter(2+sel)(zones)}"),True,(0,0,0))
        except:
            print("Error-font create error sel3")





    if zone_sel:

        wn.blit(zone_sel_png, (0,0))
        #wait = time.time()
        #once i get home take this out of if statments 
        #display = 0
        

        try: 
            wn.blit(sel1, (240, 180))
        except: 
            print("Error-blit select 1")
        try:
            wn.blit(sel2, (250,400))
        except:
            print("Error-blit select 2")
        try:
            wn.blit(sel3, (250,600))
        except:
            print("Error-blit select 3")
        
        if mousey > 950 and mousex > 1580:
            wn.blit(next_button, (0, 0))
            if mousepressed:
                sel += 1
                zone_update()
                mousepressed = False
        if mousey > 908 and mousex > 633 and mousex < 950:
            wn.blit(prev_button, (0,0))
            if mousepressed: 
                sel -= 1
                zone_update()
                mousepressed = False
        if mousex > 80 and mousex < 500 and mousey > 100 and mousey < 300:
            wn.blit(button1_for_zonesel, (0, 0))
            if mousepressed:
                zone_sel = False
                stage_1 = True
                mousepressed = False
        
        
        """if wait > 500:
            if mousex > 1150 and mousex < 1852 and mousey > 580 and mousey < 1000:
                    wn.blit(button_rec_red, (0, 0))
                    if mousepressed > 0:
                      
                        stage_1 =True
                        stage_1_music()
                        zone_sel = False
        
            if mousex > 658 and mousex < 1356 and mousey > 202 and mousey < 535:
                    wn.blit(button_rec_blue, (0, 0))
                    if mousepressed > 0:
                        stage_2 = True
                        zone_sel = False

            if mousex > 46 and mousex < 755 and mousey > 565 and mousey < 1015:
                    wn.blit(button_box_green, (0, 0))
                    if mousepressed > 0:
                        stage_3 = True
                        zone_sel = False"""
    
    if stage_1:
        wn.blit(mapsel1_, (0,0))
        
        play()
  
    if player1.hp == 0:
        wn.blit(player2win, (0,0))
        stage_1 = False
        stage_1_music = False
        stage_2 = False
        stage_3 = False
        mixer.music.stop
    if player2.hp == 0:
        wn.blit(player1win, (0,0))
        stage_1 = False
        stage_1_music = False
        stage_2 = False
        stage_3 = False
        mixer.music.stop
    
    
    player1.update()
    game_render()
    
  
       
    
    
   
        
   
    
    
   
  
    if player1.hp == 0:
        wn.blit(player2win, (0,0))
        stage_1 = False
        stage_1_music = False
        stage_2 = False
        stage_3 = False
        mixer.music.stop
    if player2.hp == 0:
        wn.blit(player1win, (0,0))
        stage_1 = False
        stage_1_music = False
        stage_2 = False
        stage_3 = False
        mixer.music.stop
    
    

    if debugon:

        font = pygame.font.Font(None,20)
        mapzone = font.render((f"loaded map files{zones}"),True,(255,255,255))
        mapzoneimg = font.render((f'loaded backgrounds{zoneimg}'),True,(255,255,255))
        mapzoneimg_small = font.render((f'loaded icons{zoneimg_small}'),True,(255,255,255))
        Errors = font.render((f'Errors {known_ERRORS}'),True,(255,255,255))
        ver_render = font.render((f'Game version {ver}'),True,(255,255,255))
        wn.blit(mapzone, (0,20))
        wn.blit(mapzoneimg, (0,40))
        wn.blit(mapzoneimg_small,(0,60))
        wn.blit(Errors, (0,80))
        wn.blit(ver_render, (0,100))
        






    player1.update()
    game_render()
   
 
       
    
    
    
    fps = font.render((f'FPS - {clock.get_fps()}'),True,(255,255,255))
    wn.blit(fps, (0,0))
    #print(clock.get_fps)
    pygame.display.update()
    if stage_1:
        mainClock.tick(60)
    