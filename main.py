import pygame, time, sys, os ,dotenv, random
from pygame.locals import *
from pygame import mixer
from Player_1 import Player1
fps = 0
pygame.init()
mousex = 0
mousey = 0 
start_screen = True
mousepressed = False
playersel = False
player1_Girl = False
player1_Boy = False
player2_Boy = False
player2_Girl = False
res = (1920, 1080)
run = True
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
#def
def game_render():
    global mousex, mousey
    mousex, mousey = player1.mouse
    wn.blit(fpsrender, (0,0))
    wn.blit(pointer, (player1.mouse))

player1 = Player1(100,10)


 
while run:
    if pygame.mouse.get_visible():
                pygame.mouse.set_visible(False)
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0
            print('game quit')
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousepressed = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousepressed = False
            
    
    #font renders
    font = pygame.font.Font(None,30)
    fpsrender = font.render(f'FPS {fps}',True,(255,255,255))
    
    if start_screen:
        wn.blit(startBG, (0,0))
        
        #start button
        wn.blit(start_button, (895, 480))
        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552 and start_screen:
            wn.blit(start_button_click, (895, 480))

        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552 and mousepressed and start_screen:
            wn.blit(start_button_click, (895, 480))
            time.sleep(0.5)
            playersel = True
            start_screen = False


    if playersel:
        wn.blit(player_sel, (0,0))

        #wn.blit(button_box, (113,192))
        if mousex > 113 and mousex < 740 and mousey > 192 and mousey < 781 and playersel:
            wn.blit(button_box, (113, 192))
            player1_Girl = True
            player2_Boy = True
        if mousex > 1210 and mousex < 1837 and mousey > 178 and mousey < 767 and playersel:
            wn.blit(button_box_blue, (1208, 180))
            player1_Boy = True
            player2_Girl = True

    #if gamerunning1:
        
    #if gamerunning2:

    player1.update()
    game_render()
    fps_s = time.time() - start
    fps1 = 1. / fps_s
    fps = int(fps1)
    pygame.display.update()
    mainClock.tick(60)
    