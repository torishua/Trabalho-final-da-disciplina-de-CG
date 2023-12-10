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
        return Vector3(scalar*v.getI(), scalar*v.getJ(), scalar*v.getK())
    
    def add(u, v):
        return Vector3(u.getI() + v.getI(), u.getJ() + v.getJ(), u.getK() + v.getK())

    def subtract(u, v):
        return Vector3(u.getI() - v.getI(), u.getJ() - v.getJ(), u.getK() - v.getK())
    
    def magnitude(v):
        return Vector3.scalarProduct(v,v)**(1/2)
    
    def normalize(v):
        return Vector3.multiplyByScalar(Vector3.magnitude(v), v)

    def scalarProduct(u, v):
        return u.getI()*v.getI() + u.getJ()*v.getJ() + u.getK()*v.getK()
    
    def vectorialProduct(u, v):
        return Vector3(u.getJ()*v.getK() - u.getK()*v.getJ(), u.getK()*v.getI() - u.getI()*v.getK(), u.getI()*v.getJ() - u.getJ()*v.getI())


