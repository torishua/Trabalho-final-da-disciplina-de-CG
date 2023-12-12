from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math
from transform import Transform

class Cylinder(Object):
    def __init__(self, materials, mapFunction, world, radius, height, baseCenter, upDirection=Vector3(0, 1, 0)):
        position = Point.multiplyByScalar(1/2, Point.add(baseCenter), Vector3.multiplyByScalar(height,upDirection.normalize()))
        self.baseCenter = baseCenter
        super().__init__(materials, mapFunction, world, position, upDirection)
        self.radius = radius
        self.height = height
        self.partSeen= None

    def getNormal(self, point):
        if self.partSeen == None:
            return Vector3(0,0,0)
        elif self.partSeen == 'up':
            return self.upDirection.normalize()
        elif self.partSeen == 'down':
            return Vector3.multiplyByScalar(-1, self.upDirection).normalize()
        else:
            v1 = Point.toVector(0, point)
            v2 = Point.toVector(self.position, 0)
            v = Vector3.add(v1, v2)
            u = Vector3.vectorialProduct(v, self.upDirection)
            n = Transform.rotation(math.pi/2, self.upDirection, u).normalize()
            return n

    def getIntersection(self, v, p0=Point(0, 0, 0)):
        d1 = Point.toVector(self.baseCenter, p0)
        d2 = Vector3.multiplyByScalar(Vector3.scalarProduct(d1, self.upDirection), self.upDirection)
        d = Vector3.subtract(d1, d2)
        w = Vector3.subtract(v, Vector3.multiplyByScalar(Vector3.scalarProduct(v,self.upDirection), self.upDirection))

        a = Vector3.scalarProduct(w,w)
        b = Vector3.scalarProduct(d,w)
        c = Vector3.scalarProduct(d,d) - self.radius**2

        delta = b*b - a*c
        if delta < 0 or a==0:
            return None
        
        ti = (-b+math.sqrt(delta))/a
        tj = (-b-math.sqrt(delta))/a

        if ti <= 0 and tj <=0:
            return None
        if ti < tj:
            self.partSeen = 'cilinder'
            return ti
        else:
            self.partSeen = 'cilinder'
            return tj