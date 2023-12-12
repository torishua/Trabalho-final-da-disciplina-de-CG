from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math

class Plane(Object):
    def __init__(self, materials: list[Material], mapFunction, world, normal, position=Point(0,0,0), upDirection=Vector3(0,1,0)) -> None:
        super().__init__(materials, mapFunction, world, position, upDirection)
        self.normal = normal

    def getNormal(self, point):
        return self.normal

    def getIntersection(self, v, p0=Point(0,0,0)):
        w = Vector3.subtract(p0 - self.position)
        numerador = Vector3.scalarProduct(w, self.normal)
        denominador = Vector3.scalarProduct(v, self.normal)

        if(denominador == 0):
            return math.inf
        
        t = -numerador/denominador

        if(t < 0):
            return math.inf
        
        return t