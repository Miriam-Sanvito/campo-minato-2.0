import pygame, sys 
from cella import Cella
from pygame.locals import *
from random import randint
from tavolo import Tavolo
from barra import Barra

larghezza_schermo = 600
altezza_schermo = 600
dimensioni_schermo = (larghezza_schermo, altezza_schermo)
schermo = pygame.display.set_mode(dimensioni_schermo)
pygame.display.set_caption("campo minato")
pygame.init()
pygame.font.init()


numero_colonne = 10
numero_righe = 8
altezza_cella = (altezza_schermo/numero_righe)
larghezza_cella = (larghezza_schermo/numero_colonne)

#schermata iniziale
x_start = (larghezza_schermo/2-65)
y_start = (altezza_schermo/2+32)
larghezza_start = 150
altezza_start = 60

clock = pygame.time.Clock()
fps = 60

class Bottone:
    def __init__(self, screen, pos, size):
        self.screen = screen
        self.pos = pos 
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.cliccato = False
        self.colore_sfondo = (255, 255, 255)  # Bianco per lo sfondo
        self.colore_bordo = (255, 111, 0)
        
        font = pygame.font.Font("font.ttf", 50)
        self.testo = font.render("play", (0.4), (255, 111, 0))
        self.testo_rect = self.testo.get_rect(center=(size[0] // 2, size[1] // 2))
    
    def draw(self):
        self.image.fill(self.colore_sfondo)  
        pygame.draw.rect(self.image, self.colore_bordo, self.image.get_rect(), 5) 
        self.image.blit(self.testo, self.testo_rect)
        self.screen.blit(self.image, self.rect)

def schermatainiziale():
    schermo.fill ((0,0,0))
    immagine = pygame.image.load('inizialecampominato.jpeg')
    immagine = pygame.transform.scale(immagine, (larghezza_schermo, altezza_schermo))
    schermo.blit(immagine, (0,0))
    bottone = Bottone(schermo, (x_start, y_start), (larghezza_start, altezza_start))
    bottone.draw()
    

tavolo = Tavolo(schermo, (0, 75), (larghezza_schermo, altezza_schermo-75))
barra = Barra(schermo, (0,0), (larghezza_schermo,  75))

cliccato = False

tavolo.piazza_mine()

for i, riga in enumerate(tavolo.celle):
    for j, cella in enumerate(riga):
        if tavolo.celle[i][j].valore != 'B':
            tavolo.celle[i][j].valore=tavolo.contamine(cella)
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    start_rect = pygame.Rect(x_start, y_start, larghezza_start, altezza_start)
                    if start_rect.collidepoint(pos):
                        cliccato = True
                    if cliccato:
                        if tavolo.rect.collidepoint(pos):
                            tavolo.cambia_colore(pos)
                            tavolo.stampa_numero(pos)
                            tavolo.bomba(pos)
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    if cliccato:
                        if tavolo.rect.collidepoint(pos):
                            tavolo.bandiera(pos)


        
       
    


    if cliccato:
        schermo.fill((8, 92, 11))
        tavolo.draw()
        barra.draw()

    else:
        schermatainiziale()
    
    
    pygame.display.flip()
    clock.tick(fps)  

