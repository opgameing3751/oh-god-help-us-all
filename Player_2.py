import pygame
from pygame import mixer


class Player2:
    
    def __init__(self, max_hp, damage):
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.image = pygame.image.load('Char/testpose1.png')
        self.right2 = False
        self.left2 = False
        self.jump2 = False
        self.down2 = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
# load idle images
        temp_list = []
        for i in range(1):
            img = pygame.image.load(f'char/BOY/wank/0.png')
            self.animation_list.append(temp_list)
    
        def update(self):
            animation_cooldown = 100
            # handle animation
            # update image
            self.image = self.animation_list[self.action][self.frame_index]
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # if the animation has run out then reset back to the start
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()
        def idle(self):
            # set variables to idle animation
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

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
        