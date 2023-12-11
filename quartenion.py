from vector3 import *
from point import Point

class Quartenion:
    
    def __init__(self, scalar, vector3: Vector3):
        self.scalar = scalar
        self.vector3 = vector3

    def getScalar(self):
        return self.scalar
    
    def getI(self):
        return self.vector3.getI()

    def getJ(self):
        return self.vector3.getJ()

    def getK(self):
        return self.vector3.getK()
    
    def getVector3(self):
        return self.vector3
    
    def multiplyByMatrix4D(m, q):
        s = q.getScalar()
        v = q.getVector3()
        x = v.getI()
        y = v.getJ()
        z = v.getK()
        arr = [x,y,z,s]
        newI = sum([arr[i]*m.getRow(0)[i] for i in range(4)])
        newJ = sum([arr[i]*m.getRow(1)[i] for i in range(4)])
        newK = sum([arr[i]*m.getRow(2)[i] for i in range(4)])
        newS = sum([arr[i]*m.getRow(3)[i] for i in range(4)])
        p = Quartenion(newS, Vector3(newI, newJ, newK))
        return Quartenion(newS, Vector3(newI, newJ, newK))
    
    def toPoint(self):
        return Point(self.getI(), self.getJ(), self.getK())

    def multiply(q, v):
        s1 = q.getScalar()
        s2 = v.getScalar()
        v1 = q.getVector3()
        v2 = v.getVector3()
        return Quartenion(s1*s2 - Vector3.scalarProduct(v1,v2), 
                          Vector3.add(
                            Vector3.add(
                              Vector3.multiplyByScalar(s1, v2),  Vector3.multiplyByScalar(s2, v1)),
                              Vector3.vectorialProduct(v1, v2)))
    
