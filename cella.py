import pygame
class Cella:
    def __init__(self, x, y, larghezza, altezza, riga, colonna ) -> None:
        self.x = x
        self.y = y
        self.riga = riga
        self.colonna = colonna
        self.larghezza = larghezza
        self.altezza = altezza 
        self.image = pygame.Surface((larghezza, altezza))
        self.rect = pygame.Rect(x, y, larghezza, altezza )

    def draw(self, surface):
        if (self.riga + self.colonna)%2 == 0:
            self.image.fill((158,250,105))
            surface.blit(self.image, (self.x, self.y))
        else:
            self.image.fill((91,186,35))
            surface.blit(self.image, (self.x, self.y))




