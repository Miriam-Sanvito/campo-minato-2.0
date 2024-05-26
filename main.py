import pygame, sys 
from cella import Cella
from pygame.locals import *
from random import randint

larghezza_schermo = 500
altezza_schermo = 500
dimensioni_schermo = (larghezza_schermo, altezza_schermo)
schermo = pygame.display.set_mode(dimensioni_schermo)
pygame.display.set_caption("campo minato")
pygame.init()
pygame.font.init()

colore = ()
valore = "!"
numero_colonne = 10
numero_righe = 10
altezza_cella = (altezza_schermo/numero_righe)
larghezza_cella = (larghezza_schermo/numero_colonne)

clock = pygame.time.Clock()
fps = 60

celle = []
for riga in range(2, numero_righe):
    riga_celle = []
    for colonna in range(numero_colonne):
        cella = Cella(colonna * larghezza_cella, riga * altezza_cella, larghezza_cella, altezza_cella, riga, colonna, colore, valore)
        riga_celle.append(cella)
    celle.append(riga_celle)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN :
            for riga in celle:
                for cella in riga:
                    if cella.rect.collidepoint(pos):
                        if event.button == 1:  
                            cella.cambia_colore(schermo)
                        elif event.button == 3: 
                            cella.bandiera()
                
        
    # pos = pygame.mouse.get_pos()
    # for riga in celle:
    #     for cella in riga:
    #         if cella.rect.collidepoint(pos):
    #             cella.sbiadisci(schermo)
    #         else:
    #             cella.draw(schermo)
                
    
    for riga in celle:
        for cella in riga:
            cella.draw(schermo)
            cella.stampa_numero(schermo)
            
    pygame.display.flip()
    clock.tick(fps)  