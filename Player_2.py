
import pygame
from pygame import mixer


class Player2:
    
    def __init__(self, max_hp, strength):
          self.max_hp = max_hp
          self.hp = max_hp
          self.strength = strength
          self.damage = 1
          #self.image = pygame.image.load('Char/testpose1.png')
          self.right2 = False
          self.left2 = False
          self.jump2 = False
          self.down2 = False
          self.animation_list = []
          self.frame_index = 0
          self.action = 0
        
          self.faceL = True
          self.faceR = False
          self.punch = False
          #walk frames
          self.image = pygame.image.load('Char\GIRL\wank\GW0.png'), pygame.image.load('Char\GIRL\wank\GW1.png'), pygame.image.load('Char\GIRL\wank\GW2.png'), pygame.image.load('Char\GIRL\wank\GW3.png') 
          self.imageL = []
          for i in range(4):
               imageL_ = pygame.transform.flip(self.image[i],True,False)
               self.imageL.append(imageL_)

          #punk frames
          self.punk = pygame.image.load('Char\GIRL\punk\TBPN0A.png'), pygame.image.load('Char\GIRL\punk\TBPN0B.png'), pygame.image.load('Char\GIRL\punk\TBPN0C.png'), pygame.image.load('Char\GIRL\punk\TBPN0D.png'), pygame.image.load('Char\GIRL\punk\TBPN0E.png'), pygame.image.load('Char\GIRL\punk\TBPN0F.png')
          self.punkL = []
          for i in range(6):
               punkL_ = pygame.transform.flip(self.punk[i],True,False)
               self.punkL.append(punkL_)
          
          #kick frames
          self.kick = pygame.image.load('Char/GIRL/kick/TBKC0A.png'), pygame.image.load('Char/GIRL/kick/TBKC0B.png'), pygame.image.load('Char/GIRL/kick/TBKC0C.png'), pygame.image.load('Char/GIRL/kick/TBKC0D.png'), pygame.image.load('Char/GIRL/kick/TBKC0D.png'), pygame.image.load('Char/GIRL/kick/TBKC0E.png')
          self.kickL = []
          for i in range(6):
               kickL_ = pygame.transform.flip(self.kick[i],True,False)
               self.kickL.append(kickL_)
          
          #jump frames
          self.jumpAni = pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png"), pygame.image.load("Char/GIRL/jump/C0JUMP.png")
          self.jumpAniL = []
          for i in range(6):
               jumpAniL = pygame.transform.flip(self.jumpAni[i],True,False)
               self.jumpAniL.append(jumpAniL)

          #death frames
          self.death_Ani = pygame.image.load('Char/GIRL/Death/TBDH0A.png'), pygame.image.load('Char/GIRL/Death/TBDH0B.png'), pygame.image.load('Char/GIRL/Death/TBDH0C.png'), pygame.image.load('Char/GIRL/Death/TBDH0D.png')
          self.death_AniL = []
          for i in range(4):
               death_AniL_ = pygame.transform.flip(self.death_Ani[i],True,False)
               self.death_AniL.append(death_AniL_)
          
          #falling will have to be baced on player high so useing walkcount would not work - ima put this on hold for now
          #falling frames
          #self.falling = pygame.image.load("")
          
    
    
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
            self.faceR = True
            self.faceL = False
       else:
            self.right2 = False
       
       if keystate[pygame.K_j]:
            self.left2 = True
            self.faceR = False
            self.faceL = True
       else:
            self.left2 = False
       if keystate[pygame.K_RSHIFT]:
            self.punch = True
       else:
            self.punch = False
        