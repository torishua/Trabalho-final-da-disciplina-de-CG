class Vector3:

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
    
    def getVector3(self):
        return self
    
    def getScalar(self):
        return 0
    
    def multiplyByScalar(scalar, v):
        v = v.getVector3()
        return Vector3(scalar*v.getI(), scalar*v.getJ(), scalar*v.getK())
    
    def add(u, v):
        v = v.getVector3()
        u = u.getVector3()
        return Vector3(u.getI() + v.getI(), u.getJ() + v.getJ(), u.getK() + v.getK())

    def subtract(u, v):
        v = v.getVector3()
        u = u.getVector3()
        return Vector3(u.getI() - v.getI(), u.getJ() - v.getJ(), u.getK() - v.getK())
    
    def magnitude(self):
        return Vector3.scalarProduct(self,self)**(1/2)
    
    def normalize(self):
        return Vector3.multiplyByScalar(1/self.magnitude(), self)

    def scalarProduct(u, v):
        return u.getI()*v.getI() + u.getJ()*v.getJ() + u.getK()*v.getK()
    
    def vectorialProduct(u, v):
        return Vector3(u.getJ()*v.getK() - u.getK()*v.getJ(), u.getK()*v.getI() - u.getI()*v.getK(), u.getI()*v.getJ() - u.getJ()*v.getI())
