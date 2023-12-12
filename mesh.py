from typing import Callable
from material import Material
from object import Object
from point import Point
from vector3 import Vector3
from transform import Transform
import math

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

    def setPosition(self, position):
        self.p1 = Point.add(Point.subtract(self.p1, self.position), position)
        self.p2 = Point.add(Point.subtract(self.p2, self.position), position)
        self.p3 = Point.add(Point.subtract(self.p3, self.position), position)
        self.position = position

    def setUpDirection(self, upDirection):
        angle = math.acos(Vector3.scalarProduct(self.upDirection.normalize(), upDirection.normalize()))
        u = Vector3.vectorialProduct(self.upDirection, upDirection).normalize()
        self.p1 = Transform.rotation(angle, u, self.p1)
        self.p2 = Transform.rotation(angle, u, self.p2)
        self.p3 = Transform.rotation(angle, u, self.p3)
        self.upDirection = upDirection


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
