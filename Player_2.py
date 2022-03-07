import pygame
from pygame import mixer


class Player2:
    
    def __init__(self, max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        #self.image = pygame.image.load('Char/testpose1.png')
        self.right2 = False
        self.left2 = False
        self.jump2 = False
        self.down2 = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        self.image = [pygame.image.load('Char\GIRL\wank\GW0.png'), pygame.image.load('Char\GIRL\wank\GW1.png'), pygame.image.load('Char\GIRL\wank\GW2.png'), pygame.image.load('Char\GIRL\wank\GW3.png')]  


    def update(self):
        
       self.mouse = pygame.mouse.get_pos()
       keystate = pygame.key.get_pressed()
        
        
        
       if keystate[pygame.K_i]:
            self.jump2 = True
       else:
            self.jump2 = False  
       if keystate[pygame.K_k]:
            self.down2 = True
       else:
            self.down2 = False
       if keystate[pygame.K_l]:
            self.right2 = True
       else:
            self.right2 = False
       if keystate[pygame.K_j]:
            self.left2 = True
       else:
            self.left2 = False
        