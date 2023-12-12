from point import Point

class LightSource:
    __a = 1
    __b = 1
    __c = 2

    def __init__(self, intensity, position):
        self.intensity = intensity
        self.position = position

    def getDistanceFrom(self, point):
        d = Point.toVector(self.position, point).magnitude()
        D = LightSource.__a + LightSource.__b*d + LightSource.__c*d**2
        return D

    def getIntensity(self):
        return self.intensity
    
    def getPosition(self):
        return self.position
    
    def setIntensity(self, intensity):
        self.intensity = intensity

    def setPosition(self, position):
        self.position = position

    def getVector3At(self, point):
        return Point.toVector(point, self.position)

        
