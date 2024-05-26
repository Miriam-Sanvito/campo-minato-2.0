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
        self.valore = valore
        self.image = pygame.Surface((larghezza, altezza))
        self.rect = pygame.Rect(x, y, larghezza, altezza )
        self.bandiere = False
        self.numeri = False
    
    

        if (self.riga + self.colonna)%2 == 0:
            self.colore = self.colore1
        else:
            self.colore = self.colore2
        
    def draw(self, surface):
        self.image.fill(self.colore)
        surface.blit(self.image, (self.x, self.y))
        if self.bandiere:
            bandiera = pygame.image.load('bandiera.png')
            bandiera = pygame.transform.scale(bandiera, (int(self.larghezza), int(self.altezza))) 
            surface.blit(bandiera, (self.x, self.y))
        if self.numeri:
            font = pygame.font.Font(None, 74)
            text = font.render(self.valore, True, (255, 255, 255))
            surface.blit(text, (self.x+15, self.y+7))
    
    def stampa_numero(self):
        if self.bandiere == False:
            self.numeri = True
    

    
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

    # def sbiadisci(self, surface):
    #     self.colore = self.colore5
    #     self.draw(surface)
    #     self.colore = colore_iniziale


    def bandiera(self):
        if self.numeri == False:
            self.bandiere = True 
        






