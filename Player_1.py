import pygame
from pygame import mixer


class Player1:
    
    def __init__(self, max_hp, strength):
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.damage = 2
        self.image = pygame.image.load("Char/Test_img_id.png")
        self.right1 = False
        self.left1 = False
        self.jump1 = False
        self.down1 = False
        self.punch = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
     
        self.button = False
        self.faceL = True
        self.faceR = False
        #walking frames 
        self.image = pygame.image.load('Char/BOY/wank/BW0.png'), pygame.image.load('Char/BOY/wank/BW1.png'), pygame.image.load('Char/BOY/wank/BW2.png'), pygame.image.load('Char/BOY/wank/BW3.png'),pygame.image.load('Char/BOY/wank/BW4.png'),pygame.image.load('Char/BOY/wank/BW5.png'),pygame.image.load('Char/BOY/wank/BW6.png')
        self.imageL = []
        for i in range(7):
            imageL_ = pygame.transform.flip(self.image[i],True,False)
            self.imageL.append(imageL_)

        #punk frames
        self.punk = pygame.image.load('Char/BOY/punk/punk1.png'), pygame.image.load('Char/BOY/punk/punk2.png'), pygame.image.load('Char/BOY/punk/punk3.png'), pygame.image.load('Char/BOY/punk/punk4.png'), pygame.image.load('Char/BOY/punk/punk5.png')
        self.punkL = []
        for i in range(5):
            punkL_ = pygame.transform.flip(self.punk[i],True,False)
            self.punkL.append(punkL_)

        #kick frames
        self.kick = pygame.image.load('Char/BOY/kick/0AFBKC.png'), pygame.image.load('Char/BOY/kick/0BFBKC.png'), pygame.image.load('Char/BOY/kick/0CFBKC.png'), pygame.image.load('Char/BOY/kick/0DFBKC.png'), pygame.image.load('Char/BOY/kick/0EFBKC.png')
        self.kickL = []
        for i in range(5):
            kickL_ = pygame.transform.flip(self.kick[i],True,False)
            self.kickL.append(kickL_)
        
        #jump frames
        self.jumpAni = pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png")
        self.jumpAniL = []
        for i in range(2):
            jumpAniL = pygame.transform.flip(self.jumpAni[i],True,False)
            self.jumpAniL.append(jumpAniL)

        #death frames
        self.death_Ani = pygame.image.load('Char/BOY/death/0AFBDH.png'), pygame.image.load('Char/BOY/death/0BFBDH.png'), pygame.image.load('Char/BOY/death/0CFBDH.png'), pygame.image.load('Char/BOY/death/0DFBDH.png'), pygame.image.load('Char/BOY/death/0EFBDH.png'), pygame.image.load('Char/BOY/death/0FFBDH.png'), pygame.image.load('Char/BOY/death/0GFBDH.png')
        self.death_AniL = []
        for i in range(7):
            death_AniL_ = pygame.transform.flip(self.death_Ani[i],True,False)
            self.death_AniL.append(death_AniL_)
        

    def update(self):
    
        self.mouse = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_ESCAPE]:
            pygame.quit()
            print("quit")
        if keystate[pygame.K_0]:
            mixer.music.load("SOUNDS/jam.mp3")
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
            self.faceL = False
            self.faceR = True
        else:
            self.right1 = False
        if keystate[pygame.K_a]:
            self.left1 = True
            self.faceR = False
            self.faceL = True
        else:
            self.left1 = False
        
        if keystate[pygame.K_LSHIFT]:
            self.punch = True
        else:
            self.punch = False
        
      #test




