import pygame, time, sys, os ,dotenv, random
from pygame.locals import *
from pygame import mixer
from Player_1 import Player1
pygame.init()

#var
fps = 0
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
res = (1920, 1080)
run = True
mousepressed = 0


wn = pygame.display.set_mode((res))
mainClock = pygame.time.Clock()

#img
BG = pygame.image.load("BG/bg.png")
char = pygame.image.load("Char\char1.png").convert_alpha()
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

#def
def game_render():
    global mousex, mousey
    mousex, mousey = player1.mouse
    wn.blit(fpsrender, (0,0))
    wn.blit(pointer, (player1.mouse))

player1 = Player1(100,10)


 
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
    fpsrender = font.render(f'FPS {fps}',True,(255,255,255))
    
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
                player2_Boy = True
                zone_sel = True
                playersel = False
                
        if mousex > 113 and mousex < 740 and mousey > 192 and mousey < 781:
            wn.blit(button_box, (113, 192))
            if mousepressed > 0:
                player1_Girl = True
                player2_Boy = False
                zone_sel = True
                playersel = False
                


        
      
            

    if zone_sel:
        wn.blit(zone_sel_png, (0,0))

        if mousex > 1150 and mousex < 1852 and mousey > 580 and mousey < 1000:
                wn.blit(button_rec_red, (0, 0))
                if mousepressed > 0:
                    print('hi')
    
        if mousex > 658 and mousex < 1356 and mousey > 202 and mousey < 535:
                wn.blit(button_rec_blue, (0, 0))
                if mousepressed > 0:
                    print('hi')

        if mousex > 46 and mousex < 755 and mousey > 565 and mousey < 1015:
                wn.blit(button_box_green, (0, 0))
                if mousepressed > 0:
                    print('hi')
                

    #if gamerunning1:
        
    #if gamerunning2:

    player1.update()
    game_render()
    fps_s = time.time() - start
    fps1 = 1. / fps_s
    fps = int(fps1)
    pygame.display.update()
    mainClock.tick(60)
    