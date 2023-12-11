from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math

class Cylinder(Object):
    def __init__(self, materials, mapFunction, world, radius, height, position=Point(0, 0, 0), upDirection=Vector3(0, 1, 0)):
        super().__init__(materials, mapFunction, world, position, upDirection)
        self.radius = radius
        self.height = height

    def getNormal(self, point):
        n = Vector3(point.getI() - self.position.getI(), 0, point.getK() - self.position.getK()).normalize()
        return n

    def getIntersection(self, v, p0=Point(0, 0, 0)):
        # abordagem simples de verificação de interseção com os discos empilhados ao longo do eixo y
        a = v.getI() ** 2 + v.getK() ** 2
        b = 2 * (v.getI() * (p0.getI() - self.position.getI()) + v.getK() * (p0.getK() - self.position.getK()))
        c = (p0.getI() - self.position.getI()) ** 2 + (p0.getK() - self.position.getK()) ** 2 - self.radius ** 2

        delta = b**2 - 4 * a * c

        if delta < 0:
            return None


        t1 = (-b + math.sqrt(delta)) / (2 * a)
        t2 = (-b - math.sqrt(delta)) / (2 * a)

        intersection1 = Point(p0.getI() + t1 * v.getI(), p0.getJ() + t1 * v.getJ(), p0.getK() + t1 * v.getK())
        intersection2 = Point(p0.getI() + t2 * v.getI(), p0.getJ() + t2 * v.getJ(), p0.getK() + t2 * v.getK())

        if self.position.getJ() <= intersection1.getJ() <= self.position.getJ() + self.height:
            return t1
        elif self.position.getJ() <= intersection2.getJ() <= self.position.getJ() + self.height:
            return t2
        else:
            return None
