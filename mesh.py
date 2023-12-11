from typing import Callable
from material import Material
from object import Object
from point import Point
from vector3 import Vector3

class Mesh(Object):
    def __init__(self, materials: list[Material], mapFunction: Callable[[list[Material], Point], Material], world, p1, p2, p3, normalMapping = None, name = 'mesh') -> None:
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
        point = Point.add(p0, Vector3.multiplyByScalar(ti, v))
        A3 = Vector3.vectorialProduct(Point.toVector(point, self.p1), Point.toVector(point, self.p2))
        A1 = Vector3.vectorialProduct(Point.toVector(point, self.p2), Point.toVector(point, self.p3))
        A2 = Vector3.vectorialProduct(Point.toVector(point, self.p3), Point.toVector(point, self.p1))
        a3 = Vector3.scalarProduct(A3, self.upDirection)
        a2 = Vector3.scalarProduct(A2, self.upDirection)
        a1 = Vector3.scalarProduct(A1, self.upDirection)
        if a3 < 0 or a2 < 0 or a1 < 0:
            return None
        
        return ti
