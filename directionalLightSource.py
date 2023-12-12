from lightSource import LightSource
from point import Point
from vector3 import Vector3

class DirectionalLightSource(LightSource):
    def __init__(self, intensity, vector3, position = Point(0,0,0)):
        super().__init__(intensity, position)
        self.vector3 = vector3
    
    def getDistanceFrom(self, point):
        return 1
    
    def getVector3At(self, point):
        return Vector3.multiplyByScalar(-1,self.vector3)
