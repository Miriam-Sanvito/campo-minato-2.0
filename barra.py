import pygame
import time
class Barra:
    def __init__(self, schermo, pos, size):
        self.size = size 
        self.schermo = schermo
        self.pos = pos
        self.colore = (0, 0, 0)
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.font = pygame.font.Font(None, 50)
        self.inizio_timer = time.time()
        self.orologio_surface = pygame.Surface((40, 40))
        # self.orologio_rect = pygame.Rect(0, 10, 25, 25)
        self.orologio = pygame.image.load('timer.png').convert_alpha()
        self.orologio = pygame.transform.scale(self.orologio, (40,40))
        self.bandiera_surface = pygame.Surface((40,40))
        self.bandiera = pygame.image.load("bandiera.png").convert_alpha()
        self.bandiera = pygame.transform.scale(self.bandiera, (40,40))


    def aggiorna_timer(self):
        tempo_trascorso = int(time.time() - self.inizio_timer)
        return tempo_trascorso

    def draw(self, nbandiere):
       self.image.fill((33, 99, 42))
       pygame.draw.rect(self.schermo, self.colore, self.rect, 5 )
       testo_timer = self.font.render(f"{self.aggiorna_timer()}", True, (255, 0, 0))
       self.image.blit(testo_timer, (65, 30))
       self.image.blit(self.orologio, (10, 30))
       self.image.blit(self.bandiera, (510, 30))
       font = pygame.font.Font("font.ttf", 30)

       testo_nbandiere = font.render(f"{nbandiere}", True, (255, 111, 0))
       self.image.blit(testo_nbandiere, (550, 35))

       self.schermo.blit(self.image, self.rect)

