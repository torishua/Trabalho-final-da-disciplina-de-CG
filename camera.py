from vector3 import Vector3
from pixel import Pixel
from point import Point
from object import Object
from light import Light

class Camera:
    def __init__(self, eyePoint, atPoint, upPoint, focalDistance, xmin, xmax, ymin, ymax):
        self.eyePoint = eyePoint
        self.atPoint = atPoint
        self.upPoint = upPoint
        self.focalDistance = focalDistance
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def getYmax(self):
        return self.ymax
    
    def getXmax(self):
        return self.xmax
    
    def getYmin(self):
        return self.ymin
    
    def getXmin(self):
        return self.xmin

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

    def castRay(self, pixel:Pixel, width, height, world):
        objects: list[Object] = world.getObjects()
        if(len(objects) == 0):
            return
        
        (x,y) = pixel.getPosition()
        stepY = (self.ymax - self.ymin)/height
        stepX = (self.xmax - self.xmin)/width
        p0 = Point(0,0,0)
        v = Vector3(self.xmin+stepX*(x+1/2), self.ymax - stepY*(y+1/2), -self.focalDistance).normalize()
        minTi = None
        i = 0
        for j in range(len(objects)):
            tj = objects[j].getIntersection(v, p0)
            if minTi == None:
                minTi = tj
                i=j
            elif tj != None and tj < minTi:
                minTi = tj
                i=j

        if minTi == None:
            #pixel.setLight(Light(255*(abs(self.xmin+stepX*(x+1/2))/self.xmax), 0, 255*(abs(self.ymax-stepY*(y+1/2))/self.ymax))
            return
        
        pixel.setObject(objects[i])
        pixel.setLight(objects[i].getIntersectionLight(v, minTi, p0))
        
        


        

    