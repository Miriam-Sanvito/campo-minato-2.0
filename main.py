import pygame, sys 
from pygame.locals import * 

larghezza_schermo = 700
altezza_schermo = 500
dimensioni_schermo = (larghezza_schermo, altezza_schermo)
schermo = pygame.display.set_mode(dimensioni_schermo)
# display = pygame.Surface((larghezza_schermo, altezza_schermo))
pygame.display.set_caption("campo minato")

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(fps)