import pygame
class Barra:
    def __init__(self, schermo, pos, size):
        self.size = size 
        self.schermo = schermo
        self.pos = pos
        self.image = pygame.Surface(self.size)

    def scritta(self):
        scritta = "campo minato"

    def draw(self):
       self.image.fill((78,98,54) )
       self.schermo.blit(self.image, self.pos)

