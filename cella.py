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
    
    def sbiadisci(self, surface):
        colore_iniziale = self.colore
        self.colore = self.colore5
        self.draw(surface)
        self.colore = colore_iniziale

    def bandiera(self):
        self.bandiere = True 
    
    # def contamine(self, celle):
    #     mine = 0
    #     for riga in range(self.riga - 1, self.riga + 2):
    #         for colonna in range(self.colonna - 1, self.colonna + 2):
    #             if 2<= riga < 10 and 0 <= colonna < 10:
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine += 1
    #     return mine
    
    
    # def contamine(self, celle):
    #     mine = 0
    #     if riga==2 and colonna ==0:
    #         for riga in range(self.riga, self.riga+2):
    #             for colonna in range(self.colonna, self.colonna+2):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif riga==2 and colonna ==9:
    #         for riga in range(self.riga, self.riga+2):
    #             for colonna in range(self.colonna-1, self.colonna+1):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif riga==9 and colonna ==9:
    #         for riga in range(self.riga-1, self.riga):
    #             for colonna in range(self.colonna-1, self.colonna+1):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif riga ==9 and colonna==0:
    #         for riga in range(self.riga-1, self.riga):
    #             for colonna in range(self.colonna, self.colonna+2):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif riga ==2 and 2<colonna<9:
    #         for riga in range(self.riga, self.riga+2):
    #             for colonna in range(self.colonna-1, self.colonna+2):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif 2<riga<9 and colonna == 9:
    #         for riga in range(self.riga-1, self.riga+2):
    #             for colonna in range(self.colonna-1, self.colonna+1):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif riga == 9 and 2<colonna<9:
    #         for riga in range(self.riga-1, self.riga+1):
    #             for colonna in range(self.colonna-1, self.colonna+2):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     elif 2<riga<9 and colonna==0:
    #         for riga in range(self.riga-1, self.riga+2):
    #             for colonna in range(self.colonna, self.colonna+2):
    #                 if celle[riga][colonna].valore == 'B':
    #                     mine+=1
    #     else:
    #         for riga in range(self.riga - 1, self.riga + 2):
    #             for colonna in range(self.colonna - 1, self.colonna + 2):
    #                 if 0 <= riga < len(celle) and 0 <= colonna < len(celle[0]):
    #                     if celle[riga][colonna].valore == 'B':
    #                         mine += 1
    #     return mine
        






