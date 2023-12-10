from vector3 import Vector3

class Camera:
    def __init__(self, eyePoint, atPoint, upPoint, focalDistance, xmin, xmax, ymin, ymax, step):
        self.eyePoint = eyePoint
        self.atPoint = atPoint
        self.upPoint = upPoint
        self.focalDistance = focalDistance
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.step = step

    def getEyePoint(self):
        return self.eyePoint
    
    def getAtPoint(self):
        return self.atPoint
    
    def getUpPoint(self):
        return self.upPoint
    
    def getFocalDistance(self):
        return self.focalDistance
    
    def setEyePoint(self, eyePoint):
        self.eyePoint = eyePoint
    
    def setAtPoint(self, atPoint):
        self.atPoint = atPoint
    
    def setUpPoint(self, upPoint):
        self.upPoint = upPoint

    def setFocalDistance(self, focalDistance):
        self.focalDistance = focalDistance

    