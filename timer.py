#https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
#code help from stack overflow
import pygame

screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

class time():
    def __init__(self):

        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else wn.blit('Game over')
            if e.type == pygame.QUIT: 
                run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)