from vector3 import Vector3
class Point:

    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def getI(self):
        return self.i
    
    def getJ(self):
        return self.j
    
    def getK(self):
        return self.k
    
    def getW(self):
        return 1
    
    def getVector3(self):
        return Vector3(self.getI(), self.getJ(), self.getK())
    
    def toVector(pi, pf):
        return Vector3(pf.getVector3().getI() - pi.getVector3().getI(), pf.getVector3().getJ() - pi.getVector3().getJ(), pf.getVector3().getK() - pi.getVector3().getK())