from object import Object
from material import Material
from point import Point
from vector3 import Vector3
import math
from transform import Transform

class Cone(Object):
    def __init__(self, materials: list[Material], mapFunction, world, radius, vertex, center, upDirection=Vector3(0, 1, 0)) -> None:
        self.vertex = vertex
        self.center = center
        position = Point.multiplyByScalar(1/2,Point.add(vertex, center))
        super().__init__(materials, mapFunction, world, position, upDirection)
        self.radius = radius
        self.height = Point.toVector(vertex, center).magnitude()
        self.partSeen = None

    def getNormal(self, point):
        if self.partSeen == None:
            return Vector3(0,0,0)
        elif self.partSeen == 'circle':
            return Vector3.multiplyByScalar(-1, self.upDirection).normalize()
        else:
            v1 = Point.toVector(0, point)
            v2 = Point.toVector(self.position, 0)
            v = Vector3.add(v1, v2)
            u = Vector3.vectorialProduct(v, self.upDirection)
            u1 = Transform.rotation(math.pi/2, self.upDirection, u).normalize()
            angle = math.atan(self.height/self.radius)
            n = Transform.rotation(angle, u, u1)
            return n
        
    def setPosition(self, position):
        return super().setPosition(position)
    
    def setUpDirection(self, upDirection):
        return super().setUpDirection(upDirection)
        

    def getIntersection(self, v, p0=Point(0, 0, 0)):
        n = Vector3.multiplyByScalar(-1, self.upDirection).normalize()
        u = Point.toVector(self.vertex, p0)
        angle = math.atan(self.height/self.radius)
        a = Vector3.scalarProduct(v, n)**2 - Vector3.scalarProduct(v,v)*math.cos(angle)**2
        b = Vector3.scalarProduct(u, v)*math.cos(angle)**2 - Vector3.scalarProduct(u, n)*Vector3.scalarProduct(v, n)
        c = Vector3.scalarProduct(u, n)**2 - Vector3.scalarProduct(u,u)*math.cos(angle)**2

        delta = b*b - a*c
        if delta < 0 or a==0:
            return None
        
        ti = (-b+math.sqrt(delta))/a
        tj = (-b-math.sqrt(delta))/a

        if ti <= 0 and tj <=0:
            return None
        if ti < tj:
            self.partSeen = 'cone'
            return ti
        else:
            self.partSeen = 'cone'
            return tj
    