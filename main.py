import pygame
from sys import exit

Width: int = 800
Heigth: int  = 800

pygame.init()
screen = pygame.display.set_mode((Width, Heigth))
pygame.display.set_caption("Computacao Grafica")


#Game Loop
while True:


    #Player Controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()