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
x_start = 150
y_start = 300
larghezza_start = 200
altezza_start = 100

clock = pygame.time.Clock()
fps = 60


def schermatainiziale():
    schermo.fill ((0,0,0))
    rect = pygame.Rect(150, 300, 200, 100)
    pygame.draw.rect(schermo, (255, 255, 255), rect)  
    pygame.display.flip()
    

tavolo = Tavolo(schermo, (0, 75), (larghezza_schermo, altezza_schermo-75))
barra = Barra(schermo, (0,0), (larghezza_schermo,  75))

cliccato = False

tavolo.piazza_mine()
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

