from point import Point
from vector3 import Vector3
from material import Material
from lightSource import LightSource
from transform import Transform
import math

class Light:
    __a = 1
    __b = 1
    __c = 2

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def getRed(self):
        return self.red
    
    def getBlue(self):
        return self.blue
    
    def getGreen(self):
        return self.green
    
    def toColor(self):
        return (self.red, self.green, self.blue)
    
    def multiplyByScalar(scalar, lgt):
        return Light(scalar*lgt.getRed(), scalar*lgt.getGreen(), scalar*lgt.getBlue())
    
    def arrobaOperation(reflexetion, lgt):
        return Light(lgt.getRed()*reflexetion.getRed(), lgt.getGreen()*reflexetion.getGreen(), lgt.getBlue()*reflexetion.getBlue())
    
    def sum(lgt1, lgt2):
        return Light(lgt1.getRed() + lgt2.getRed(), lgt1.getGreen() + lgt2.getGreen(), lgt1.getBlue() + lgt2.getBlue())

    def ambienceLight(m, lgt):
        return Light.arrobaOperation(m.getAmbienceReflexetion(), lgt)

    def diffuseLight(m, p, lgtSource):
        q = lgtSource.getPosition()
        pq = Point.toVector(q, p)
        l = pq.normalize()
        d = pq.magnitude()
        n = m.getNormal()
        k = m.getDiffuseReflexetion()
        D = Light.__a + Light.__b*d + Light.__c*d**2
        Id = Light.multiplyByScalar(max(0,Vector3.scalarProduct(l, n)), lgtSource.getIntensity()) #(l.n)Ld
        Id = Light.multiplyByScalar(1/D, Id) #1/D*(l.n)Ld
        Id = Light.arrobaOperation(k, Id)
        return Id
    
    def specularLight(m, p, v, lgtSource):
        q = lgtSource.getPosition()
        pq = Point.toVector(q, p)
        l = pq.normalize()
        n = m.getNormal()
        planeVector = Vector3.vectorialProduct(l, n)
        angle = math.acos(Vector3.scalarProduct(l, n))
        r = Transform.rotation(2*angle, planeVector, l)
        d = pq.magnitude()
        D = Light.__a + Light.__b*d + Light.__c*d**2
        Id = Light.multiplyByScalar(max(0,Vector3.scalarProduct(l, n)), lgtSource.getIntensity())
        Is = Light.arrobaOperation(m.getSpecularReflexetion(), lgtSource.getIntensity())
        specCons = Vector3.scalarProduct(r, v)**m.getSpecularM()
        Is = Light.multiplyByScalar(1/D*specCons, Is)
        return Is
    
    def calculeTotalLight(m, p, v, sources, ambienceLgt):
        lgt = Light(0,0,0)
        for lgtSource in sources:
            lgtD = Light.diffuseLight(m, p, lgtSource)
            lgtS = Light.specularLight(m, p, v, lgtSource)
            lgt = Light.sum(lgt, lgtD)
            lgt = Light.sum(lgt, lgtS)
        ambienceLgt = Light.ambienceLight(m, ambienceLgt)
        lgt = Light.sum(lgt, ambienceLgt)
        lgt = Light(min(255, lgt.getRed()), min(255, lgt.getBlue()), min(255, lgt.getGreen()))
        return lgt



        
        
