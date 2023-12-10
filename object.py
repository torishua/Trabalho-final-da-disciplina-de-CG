from vector3 import Vector3
from material import Material
from ray import Ray

class Object:
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def getPosition(self):
        return self.position

    def getMaterial(self):
        return self.material

    def setPosition(self, position):
        self.position = position

    def setMaterial(self, material):
        self.material = material

    def intersect(self, ray: Ray):
        return None

