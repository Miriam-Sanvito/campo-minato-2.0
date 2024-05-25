import pygame
class Cella:
    def __init__(self, x, y, larghezza, altezza, riga, colonna, colore, valore) -> None:
        self.x = x
        self.y = y
        self.riga = riga
        self.colonna = colonna
        self.larghezza = larghezza
        self.altezza = altezza 
        self.colore  = colore
        self.colore1= (158,250,105)
        self.colore2= (91,186,35)
        self.colore3= (233, 242, 228)
        self.colore4= (191, 204, 184)
        self.colore5 = (247, 247, 247)
        self.image = pygame.Surface((larghezza, altezza))
        self.rect = pygame.Rect(x, y, larghezza, altezza )
    
    

        if (self.riga + self.colonna)%2 == 0:
            self.colore = self.colore1
        else:
            self.colore = self.colore2
        
    def draw(self, surface):
        self.image.fill(self.colore)
        surface.blit(self.image, (self.x, self.y))
    
    def stampa_numero(self, surface):
        font = pygame.font.Font(None, 74)
        text = font.render(self.valore, True, (255, 255, 255))
        surface.blit(text, (self.x+20, self.y+7))

    
    def cambia_colore(self, surface):
        if self.colore == self.colore1:
            self.colore = self.colore3
        elif self.colore == self.colore2:
            self.colore = self.colore4
        self.draw(surface)
    
    # def sbiadisci(self, surface):
    #     colore_iniziale = self.colore
    #     self.colore = self.colore5
    #     self.draw(surface)
    #     self.colore = colore_iniziale

    def sbiadisci(self, surface):
        self.colore = self.colore5
        self.draw(surface)
        self.colore = colore_iniziale








