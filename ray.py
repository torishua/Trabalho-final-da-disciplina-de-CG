from vector3 import Vector3

class Ray:
    def __init__(self, origin, direction, t=float('inf')):
        self.origin = origin
        self.direction = direction
        self.t = t

    def getOrigin(self):
        return self.origin

    def getDirection(self):
        return self.direction

    def getT(self):
        return self.t

    def setOrigin(self, origin):
        self.origin = origin

    def setDirection(self, direction):
        self.direction = direction

    def setT(self, t):
        self.t = t
