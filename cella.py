import pygame
class Cella:
    def __init__(self, x, y, larghezza, altezza, riga, colonna, valore =0) -> None:
        self.x = x
        self.y = y
        self.riga = riga
        self.colonna = colonna
        self.larghezza = larghezza
        self.altezza = altezza 
        self.colore1= (158,250,105)
        self.colore2= (91,186,35)
        self.colore3= (191, 204, 184)
        self.colore4= (137, 161, 143)
        self.valore = valore
        self.image = pygame.Surface((larghezza, altezza))
        self.rect = pygame.Rect(x, y, larghezza, altezza )
        self.bandiere = False
        self.numero = False
        self.bombe = False
        self.valore = valore
        self.schiacciata = False
        self.perso = False
    
    

        if (self.riga + self.colonna)%2 == 0:
            self.colore = self.colore1
        else:
            self.colore = self.colore2
        
    def draw(self, tavolo):
        self.image.fill(self.colore)
        tavolo.blit(self.image, (self.x, self.y))
        if self.bandiere:
            bandiera = pygame.image.load('bandiera.png').convert_alpha()
            bandiera = pygame.transform.scale(bandiera, (int(self.larghezza), int(self.altezza))) 
            tavolo.blit(bandiera, (self.x, self.y))
        if self.numero:
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.valore), True, (255, 255, 255))
            tavolo.blit(text, (self.x+15, self.y+7))
        if self.bombe:
            bomba = pygame.image.load('bomba.png').convert_alpha()
            bomba = pygame.transform.scale(bomba, (int(self.larghezza), int(self.altezza)))
            tavolo.blit(bomba, (self.x, self.y))

    def cambia_colore(self):
        if self.colore == self.colore1:
            self.colore = self.colore3
        elif self.colore == self.colore2:
            self.colore = self.colore4

    def bandiera(self):
        self.bandiere = True
        self.schiacciata = True
    
    def stampa_numero(self):
        if self.bandiere == False:
            self.numero = True
    
    def bomba(self):
        self.bombe = True
    
    def perso(self):
        self.perso = True
    

        





