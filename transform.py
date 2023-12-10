from matrix4D import *
from quartenion import *
import math

class Transform:
    def __init__():
        pass

    def translate(tx,ty,tz, q):
        return Quartenion.multiplyByMatrix4D(Matrix4D.translation(tx,ty,tz), q)
    
    def rotation(angle, u, v):
        u = u.normalize()
        qL = Quartenion(math.cos(angle/2), Vector3.multiplyByScalar(math.sin(angle/2), u))
        qR = Quartenion(math.cos(angle/2), Vector3.multiplyByScalar(math.sin(angle/2), u))
        v1 = Quartenion.multiply(qL,v)
        v2 = Quartenion.multiply(v1,qR)
        return v2
    
    def scale(sx,sy,sz, xf, yf, zf, q):
        return Quartenion.multiplyByMatrix4D(Matrix4D.scale(sx,sy,sz,xf,yf,zf), q)
    
    def rotationX(angle, v):
        return Quartenion.multiplyByMatrix4D(Matrix4D.rotationX(angle), v)
    
    def rotationY(angle, v):
        return Quartenion.multiplyByMatrix4D(Matrix4D.rotationY(angle), v)
    
    def rotationZ(angle, v):
        return Quartenion.multiplyByMatrix4D(Matrix4D.rotationZ(angle), v)
    
    def world2Camera(c: Camera, q):
        return Quartenion.multiplyByMatrix4D(Matrix4D.world2Camera(c), q)
    

