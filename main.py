import pygame
from camera import Camera
from light import Light
from lightSource import LightSource
from material import Material
from matrix4D import Matrix4D
from pixel import Pixel
from point import Point
from quartenion import Quartenion
from transform import Transform
from vector3 import Vector3

from sys import exit

Width: int = 500
Heigth: int  = 500

pygame.init()
screen = pygame.display.set_mode((Width, Heigth))
pygame.display.set_caption("Computacao Grafica")

matrixOfPixels = [[Pixel(None, Light(0,0,0), (i,j)) for i in range(Width)] for j in range(Heigth)]

#Game Loop
while True:

    for pixelRow in matrixOfPixels:
        for pixel in pixelRow:
            (x,y) = pixel.getPosition()
            color = pixel.getLight().toColor()
            pixel.setLight(Light((color[0]-10)%256, 0, (color[2]+10)%256))
            screen.set_at((x, y), color)



    #Player Controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()