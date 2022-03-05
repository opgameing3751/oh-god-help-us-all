from asyncio import wait_for
import pygame, time, sys, os ,dotenv, random, math

from pygame.locals import *
from pygame import mixer
from Player_1 import Player1
from Player_2 import Player2
from stage1 import stage_1

#from stage1 import stage_1

pygame.init()

#var
RED = (255,0,0)
GREEN = (0,255,0)
grav = 10
fps = 1
mousex = 0
mousey = 0 
start_screen = True
mousepressed = False
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
res = (1920, 1080)
run = True
mousepressed = 0
P1X = 216
P1Y = 647
P2X = 1700
P2Y = 649
jump1go = 0
jump2go = 0

wn = pygame.display.set_mode((res))
mainClock = pygame.time.Clock()

#img
BG = pygame.image.load("BG/bg.png")
#player1pngboy = pygame.image.load("Char\Test_img_id.png").convert_alpha()
#player2pnggirl = pygame.image.load('Char/testpose1.png')
pointer = pygame.image.load("pointer\pointer.png").convert_alpha()
startBG = pygame.image.load('start screen\startBG.png').convert_alpha()
start_button = pygame.image.load("start screen\start_button.png").convert_alpha()
start_button_click = pygame.image.load("start screen\start_button_cliced.png").convert_alpha()
player_sel = pygame.image.load('start screen\player sel.png').convert_alpha()
button_box = pygame.image.load('start screen/button_box.png').convert_alpha()
button_box_blue = pygame.image.load("start screen/button_box_blue.png").convert_alpha()
zone_sel_png = pygame.image.load("start screen\zone sel.png").convert()
button_box_green = pygame.image.load('start screen/button_box_green.png').convert_alpha()
button_rec_blue = pygame.image.load('start screen/button_rec_Blue.png').convert_alpha()
button_rec_red = pygame.image.load('start screen/button_rec_Red.png').convert_alpha()
volcano_stage = pygame.image.load("BG\sample_volcano.png").convert()

#sounds
punch_sound = pygame.mixer.Sound("SOUNDS\punch.wav")

#def
def game_render():
    global mousex, mousey
    mousex, mousey = player1.mouse
    wn.blit(fpsrender, (0,0))
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




player1 = Player1(100,10)
player2 = Player2(100,10)
player1_health_bar = HealthBar(50,50, player1.hp, player1.max_hp)
player2_health_bar = HealthBar(1250,50, player2.hp, player2.max_hp)
RGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RGG = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
player1.hp = 75
while run:
    
    print(mousepressed)
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
    if event.type == pygame.MOUSEBUTTONUP:
        mousepressed = 0
          
    
    #font renders
    font = pygame.font.Font(None,30)
    fpsrender = font.render(f'FPS {fps}',True,(RGB))
    
    if start_screen:
        wn.blit(startBG, (0,0))
        
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
        if player1_Girl and mousepressed == 0:
            zone_sel = True
            playersel = False
        if player2_Boy and mousepressed == 0:
            zone_sel = True
            playersel = False
        if player2_Girl and mousepressed == 0:
            zone_sel = True
            playersel = False
    

    def stage_1_music():
        mixer.music.load("SOUNDS\Mick Gordon - 11. BFG Division.mp3")
        mixer.music.play(1)

    if zone_sel:
        wn.blit(zone_sel_png, (0,0))
        wait = time.time()
        if wait > 500:
            if mousex > 1150 and mousex < 1852 and mousey > 580 and mousey < 1000:
                    wn.blit(button_rec_red, (0, 0))
                    if mousepressed > 0:
                        print('red')
                        stage_1 =True
                        stage_1_music()
                        zone_sel = False
        
            if mousex > 658 and mousex < 1356 and mousey > 202 and mousey < 535:
                    wn.blit(button_rec_blue, (0, 0))
                    if mousepressed > 0:
                        print('hi')
                        zone_sel = False

            if mousex > 46 and mousex < 755 and mousey > 565 and mousey < 1015:
                    wn.blit(button_box_green, (0, 0))
                    if mousepressed > 0:
                        print('hi')
                        zone_sel = False
    
    if stage_1:
        wn.blit(volcano_stage, (0,0))
        if P1Y < 647:
            P1Y += (grav)
        if player1.jump1 and P1Y > 600:
            jump2go = 20
        if player1.right1:
            P1X += 10
        if player1.left1:
            P1X -= 10
        player1.update()
        #player1.draw()
        #wn.blit(player1.image, (P1X, P1Y))

        keystate = pygame.key.get_pressed()

        if P2Y < 647:
            P2Y += (grav)
        if keystate[pygame.K_i] and P2Y > 600:
            jump1go = 20
            print('hi')
        if keystate[pygame.K_l]:
            P2X += 10
            print('hi')
        if keystate[pygame.K_j]:
            P2X -= 10
        if jump1go > 0:
            P2Y -= jump1go
            jump1go -= 1
        if jump2go > 0:
            P1Y -= jump2go
            jump2go -= 1
        player2.update()
        #player2.draw()
        #wn.blit(player2.image, (P2X, P2Y))
        distance = math.sqrt ((math.pow(P1X-P2X,2)) + (math.pow(P1Y-P2Y,2)))
        if player1.punch and distance < 50:
            pygame.mixer.Sound.play(punch_sound)
            
        player1_health_bar.draw(player1.hp)
        player2_health_bar.draw(player2.hp)
    print(f'{P2X},{P2Y}')

    

    player1.update()
    game_render()
    fps_s = time.time() - start
    #if fps_s == 0.:
       
    if fps_s < 40.:
        fps1 = 1. / fps_s
    if fps_s > 40.:
        fps1 = fps_s
    #else:
        
    fps = int(fps1)
    pygame.display.update()
    mainClock.tick(60)
    