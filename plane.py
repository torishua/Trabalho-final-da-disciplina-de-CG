from typing import Callable
from material import Material
from object import Object
from point import Point
from vector3 import Vector3

class Plane(Object):
    def __init__(self, materials: list[Material], mapFunction: Callable[[list[Material], Point], Material], world, p1, p2, p3, normalMapping = None, name='null object') -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.normalMapping = normalMapping
        position = Point.add(Point.add(p1, p2), p3)
        position = position.multiplyByScalar(1/3, position)
        v1 = Point.toVector(p1, p2)
        v2 = Point.toVector(p1, p3)
        upDirection = Vector3.vectorialProduct(v1, v2)
        super().__init__(materials, mapFunction, world, position, upDirection, name)
        super().__init__(materials, mapFunction, world, position, upDirection, name)
        

    def getNormal(self, point):
        if self.normalMapping == None:
            return self.upDirection
        
        normal = self.normalMapping(point, self.p1, self.p2, self.p3)
        return normal

    
    def getIntersection(self, v, p0=Point(0,0,0)):
        u = Point.toVector(p0, self.p1)
        a = Vector3.scalarProduct(u, self.upDirection)
        b = Vector3.scalarProduct(v, self.upDirection)
        ti = a/b
        if ti <= 0:
            return None
        return ti

    