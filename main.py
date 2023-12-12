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
from world import World
from object import Object
from sphere import Sphere
from reflexetion import Reflexetion
from picking import Picking

from sys import exit

Width: int = 500
Heigth: int  = 500

pygame.init()
screen = pygame.display.set_mode((Width, Heigth))
pygame.display.set_caption("Computacao Grafica")

matrixOfPixels = [[Pixel(None, Light(0,20,100), (i,j)) for i in range(Width)] for j in range(Heigth)]

world = World(Light(255,255,255))

material1 = Material(Reflexetion(1, 0, 0),Reflexetion(0.7, 0.4, 0), Reflexetion(0.7, 0.4, 0), 2)
material2 = Material(Reflexetion(0, 1, 0),Reflexetion(0.7, 0.4, 0), Reflexetion(0.7, 0.4, 0), 2)
material3 = Material(Reflexetion(1, 0, 1),Reflexetion(0.7, 0.4, 0), Reflexetion(0.7, 0.4, 0), 2)
sphere1 = Sphere([material1], lambda materials, point:  materials[0],  world, 10, Point(20,0,20))
sphere2 = Sphere([material2], lambda materials, point:  materials[0],  world, 10, Point(20,40,20))
sphere3 = Sphere([material3], lambda materials, point:  materials[0],  world, 10, Point(20,80,20))

world.addObject(sphere1)
world.addObject(sphere2)
world.addObject(sphere3)

camera = Camera(Point(0,10,0), Point(10,0,10), Point(10, 40, 10), 10, -80, 80, -80, 80)
world.world2Camera(camera)

picking = Picking(camera, matrixOfPixels)

for pixelRow in matrixOfPixels:
    for pixel in pixelRow:
        camera.castRay(pixel, Width, Heigth, world)
        screen.set_at(pixel.getPosition(), pixel.getLight().toColor())

#Game Loop
while True:

    #Player Controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            obj = picking.pickObjectByPixel(pos[0], pos[1])
            print(obj)

    pygame.display.update()