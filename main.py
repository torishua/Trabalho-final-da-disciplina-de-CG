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

from sys import exit

Width: int = 500
Heigth: int  = 500

pygame.init()
screen = pygame.display.set_mode((Width, Heigth))
pygame.display.set_caption("Computacao Grafica")

matrixOfPixels = [[Pixel(None, Light(0,0,50), (i,j)) for i in range(Width)] for j in range(Heigth)]

world = World(Light(255,0,255))

material1 = Material(Reflexetion(0.7, 0.7, 0),Reflexetion(0.7, 0.4, 0.3), Reflexetion(0.7, 0.4, 0.6), 2)
sphere = Sphere([material1], lambda materials, point:  materials[0],  world, 10)
#print(sphere.getPosition().getI())
world.addObject(sphere)

sphere.setPosition(Transform.translate(10, 80, 10, sphere.getPosition()).toPoint())
#print(sphere.getPosition().getJ())
camera = Camera(Point(0,0,-10), Point(10,0,10), Point(10,40, 10), 10, -40, 40, -40, 40)
world.world2Camera(camera)

#print(sphere.getPosition().getI())
#print(sphere.getPosition().getJ())
#print(sphere.getPosition().getK())

for pixelRow in matrixOfPixels:
    for pixel in pixelRow:
        #(x,y) = pixel.getPosition()
        #color = pixel.getLight().toColor()
        #pixel.setLight(Light((color[0]-10)%256, 0, (color[2]+10)%256))
        camera.castRay(pixel, Width, Heigth, world)
        screen.set_at(pixel.getPosition(), pixel.getLight().toColor())

#Game Loop
while True:

    #Player Controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()