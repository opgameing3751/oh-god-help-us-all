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
        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552:
            wn.blit(start_button_click, (895, 480))

        if mousex > 895 and mousex < 1114 and mousey > 480 and mousey < 552 and mousepressed:
            wn.blit(start_button_click, (895, 480))
            time.sleep(0.5)
            playersel = True
    if playersel:
        wn.blit(player_sel, (0,0))

    #if gamerunning1:
        
    #if gamerunning2:

    player1.update()
    game_render()
    fps_s = time.time() - start
    fps1 = 1. / fps_s
    fps = int(fps1)
    pygame.display.update()
    mainClock.tick(60)
    