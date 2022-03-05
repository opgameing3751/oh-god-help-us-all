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
        




