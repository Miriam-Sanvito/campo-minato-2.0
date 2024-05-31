import pygame, sys
from cella import Cella

class Tavolo:
    def __init__(self, screen, pos, size):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.nrighe = 8
        self.ncolonne= 10
        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.pos0=pos[0]
        self.pos1=pos[1]
        self.larghezza_cella = size[0] // self.ncolonne
        self.altezza_cella = size[1] // self.nrighe

        self.celle = [[Cella(pos[0] + colonna * self.larghezza_cella, pos[1] + riga * self.altezza_cella, self.larghezza_cella, self.altezza_cella, riga, colonna, valore=0) for colonna in range(self.ncolonne)] for riga in range(self.nrighe)]

    def draw(self):
        for riga in self.celle:
            for cella in riga:
                cella.draw(self.screen)

    def cambia_colore(self, pos):
        for riga in self.celle:
            for cella in riga:
                if cella.rect.collidepoint(pos):
                    cella.cambia_colore()
    
    def bandiera(self, pos):
        for riga in self.celle:
            for cella in riga:
                if cella.rect.collidepoint(pos):
                    cella.bandiera()




