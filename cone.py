from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math

class Cone(Object):
    def __init__(self, materials: list[Material], mapFunction, world, radius, height, position=Point(0, 0, 0), upDirection=Vector3(0, 1, 0)) -> None:
        super().__init__(materials, mapFunction, world, position, upDirection)
        self.radius = radius
        self.height = height

    def getNormal(self, point):
        # normal para um cone é a direção do ponto para o vértice ?? 
        n = Vector3.subtract(point, self.position).normalize()
        return n

    def getIntersection(self, v, p0=Point(0, 0, 0)):
        a = v.scalarProduct(v) - (v.getJ()**2) * (self.radius / self.height)**2
        b = 2 * ((p0.subtract(self.position)).scalarProduct(v) - (v.getJ()**2) * ((p0.getJ() - self.position.getJ()) * (self.radius / self.height)**2))
        c = (p0.subtract(self.position)).scalarProduct(p0.subtract(self.position)) - ((p0.getJ() - self.position.getJ()) * (self.radius / self.height))**2

        delta = b**2 - 4 * a * c

        if delta < 0:
            return None

        t1 = (-b + math.sqrt(delta)) / (2 * a)
        t2 = (-b - math.sqrt(delta)) / (2 * a)

        # a interseção está dentro da altura do cone ??
        if self.position.getJ() <= p0.getJ() + t1 * v.getJ() <= self.position.getJ() + self.height:
            return t1
        elif self.position.getJ() <= p0.getJ() + t2 * v.getJ() <= self.position.getJ() + self.height:
            return t2
        else:
            return None
