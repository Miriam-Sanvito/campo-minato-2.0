import pygame, sys
from cella import Cella

class Tavolo:
    def __init__(self, screen, pos, altezzatavolo, larghezzatavolo, nrighe, ncolonne):
        self.screen = screen
        self.pos = pos
        self.size = [larghezzatavolo, altezzatavolo]
        self.nrighe = nrighe
        self.ncolonne= ncolonne
      

    def draw(self):
        altezza_cella = (int(self.size[0])/self.nrighe)
        larghezza_cella = (int(self.size[1])/self.ncolonne)
        celle = []
        for _ in range(self.nrighe):
            riga_celle = []
            for _ in range(self.ncolonne):
                cella = Cella( larghezza_cella, altezza_cella)
                riga_celle.append(cella)
            celle.append(riga_celle)
        
        for riga in range(len(celle)):
            for colonna in range(len(celle[riga])):
                cella = celle[riga][colonna]
                if (riga + colonna)%2 == 0:
                    
                    cella.image.fill((200, 200, 200))
                    cella_pos = (self.pos[0] + colonna * larghezza_cella, self.pos[1] + riga * altezza_cella)
                    self.screen.blit(cella.image, cella_pos)
                else:
                    cella.image.fill((30, 30, 200))
                    cella_pos = (self.pos[0] + colonna * larghezza_cella, self.pos[1] + riga * altezza_cella)
                    self.screen.blit(cella.image, cella_pos)


# if (self.riga + self.colonna)%2 == 0:
#             self.colore = self.colore1
#         else:
#             self.colore = self.colore2


        # if self.bandiere:
        #     bandiera = pygame.image.load('bandiera.png')
        #     bandiera = pygame.transform.scale(bandiera, (int(self.larghezza), int(self.altezza))) 
        #     surface.blit(bandiera, (self.x, self.y))
        # if self.numeri:
        #     font = pygame.font.Font(None, 74)
        #     text = font.render(self.valore, True, (255, 255, 255))
        #     surface.blit(text, (self.x+15, self.y+7))
        

