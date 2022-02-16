import pygame, time, sys, os ,dotenv, random
from pygame.locals import *
from pygame import mixer
fps = 0
pygame.init()

res = (1920, 1080)
run = True
wn = pygame.display.set_mode((res))
mainClock = pygame.time.Clock()

#img
BG = pygame.image.load("BG/bg.png")
char = pygame.image.load("Char\char1.png").convert_alpha()
pointer = pygame.image.load("pointer\pointer.png").convert_alpha()

#def
def game_render():

    wn.blit(BG, (0,0))
    wn.blit(fpsrender, (0,0))
    wn.blit(pointer, (player.mouse))

#class
class Player1:
    
    def __inti__(self, max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.image = char
    def update(self):
        self.mouse = pygame.mouse.get_pos()

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q]:
            pygame.quit()
            print("quit")
        if keystate[pygame.K_0]:
            mixer.music.load("SOUNDS\jam.mp3")
            mixer.music.play(1)

class Player2:
    def __inti__(self,max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
       

player = Player1()
"""female = Player1(100,10)
male = Player2(100,10)   """ 
while run:
    if pygame.mouse.get_visible():
                pygame.mouse.set_visible(False)
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0
            print('game quit')
    
    #font renders
    font = pygame.font.Font(None,30)
    fpsrender = font.render(f'FPS {fps}',True,(255,255,255))
    
    player.update()
    game_render()
    fps_s = time.time() - start
    fps1 = 1. / fps_s
    fps = int(fps1)
    pygame.display.update()
    mainClock.tick(60)
    