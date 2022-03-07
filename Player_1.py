import pygame
from pygame import mixer


class Player1:
    
    def __init__(self, max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.image = pygame.image.load("Char/Test_img_id.png")
        self.right1 = False
        self.left1 = False
        self.jump1 = False
        self.down1 = False
        self.punch = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
    def update(self):
    
        self.mouse = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_ESCAPE]:
            pygame.quit()
            print("quit")
        if keystate[pygame.K_0]:
            mixer.music.load("SOUNDS\jam.mp3")
            mixer.music.play(1)
            
        if keystate[pygame.K_w]:
            self.jump1 = True
        else:
            self.jump1 = False  
        if keystate[pygame.K_s]:
            self.down1 = True
        else:
            self.down1 = False
        if keystate[pygame.K_d]:
            self.right1 = True
        else:
            self.right1 = False
        if keystate[pygame.K_a]:
            self.left1 = True
        else:
            self.left1 = False

        if keystate[pygame.K_q]:
            self.punch = True
        else:
            self.punch = False
        




