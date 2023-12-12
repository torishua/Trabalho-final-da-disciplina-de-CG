from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math

class Sphere(Object):
    def __init__(self, materials: list[Material], mapFunction, world, radius, position=Point(0,0,0), upDirection=Vector3(0,1,0), name = 'sphere') -> None:
        super().__init__(materials, mapFunction, world, position, upDirection, name)
        self.radius = radius

    def getNormal(self, point):
        n = Vector3.subtract(point, self.position).normalize()
        return n

    def getIntersection(self, v, p0=Point(0,0,0)):
        a = Vector3.scalarProduct(v,v)
        b = Vector3.scalarProduct(Vector3.subtract(p0, self.position), v)
        c = Vector3.scalarProduct(Vector3.subtract(p0, self.position), Vector3.subtract(p0, self.position)) - self.radius**2
        delta = b*b - a*c
        if delta < 0:
            return None
        
        ti = (-b+math.sqrt(delta))/a
        tj = (-b-math.sqrt(delta))/a

        if ti <= 0 and tj <=0:
            return None
        if ti < tj:
            return ti
        else:
            return tj
    