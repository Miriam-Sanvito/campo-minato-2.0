import pygame
class Barra:
    def __init__(self, schermo, pos, size):
        self.size = size 
        self.schermo = schermo
        self.pos = pos
        self.colore = (250,10,20)
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self):
       pygame.draw.rect(self.schermo, self.colore, self.rect, 5 )

