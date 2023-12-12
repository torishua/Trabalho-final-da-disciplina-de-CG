import math
from vector3 import Vector3
from point import Point

class Matrix4D:
    #X, Y são invertidos, M[y][x] acessa o elemento (x,y)
    def __init__(self, matrix):
        self.matrix = matrix

    def getRow(self, rowIndex):
        return self.matrix[rowIndex]
    
    def getCollum(self, collumnIndex):
        return [self.matrix[i][collumnIndex] for i in range(0,3)]
        
    def multiply(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0] + A[0][3]*B[3][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1] + A[0][3]*B[3][1],
             A[0][0]*B[0][2] + A[0][1]*B[1][2] + A[0][2]*B[2][2] + A[0][3]*B[3][2],
             A[0][0]*B[0][3] + A[0][1]*B[1][3] + A[0][2]*B[2][3] + A[0][3]*B[3][3]
            ],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0] + A[1][3]*B[3][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1] + A[1][3]*B[3][1],
             A[1][0]*B[0][2] + A[1][1]*B[1][2] + A[1][2]*B[2][2] + A[1][3]*B[3][2],
             A[1][0]*B[0][3] + A[1][1]*B[1][3] + A[1][2]*B[2][3] + A[1][3]*B[3][3]
            ],
            [A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0] + A[2][3]*B[3][0],
             A[2][0]*B[0][1] + A[2][1]*B[1][1] + A[2][2]*B[2][1] + A[2][3]*B[3][1],
             A[2][0]*B[0][2] + A[2][1]*B[1][2] + A[2][2]*B[2][2] + A[2][3]*B[3][2],
             A[2][0]*B[0][3] + A[2][1]*B[1][3] + A[2][2]*B[2][3] + A[2][3]*B[3][3]
            ],
            [A[3][0]*B[0][0] + A[3][1]*B[1][0] + A[3][2]*B[2][0] + A[3][3]*B[3][0],
             A[3][0]*B[0][1] + A[3][1]*B[1][1] + A[3][2]*B[2][1] + A[3][3]*B[3][1],
             A[3][0]*B[0][2] + A[3][1]*B[1][2] + A[3][2]*B[2][2] + A[3][3]*B[3][2],
             A[3][0]*B[0][3] + A[3][1]*B[1][3] + A[3][2]*B[2][3] + A[3][3]*B[3][3]
            ]
            ]
    
    def translation(tx, ty, tz):
        return Matrix4D([[1,0,0,tx], [0,1,0,ty], [0,0,1,tz], [0,0,0,1]])
    
    def scale(sx, sy, sz, xf, yf, zf):
        return Matrix4D([[sx,0,0,(1-sx)*xf],[0,sy,0,(1-sy)*yf],[0,0,sz,(1-sz)*zf],[0,0,0,1]])
    
    def rotationX(angle):
        return Matrix4D([[1,0,0,0],[0,math.cos(angle),-math.sin(angle),0],[0,math.sin(angle),math.cos(angle),0],[0,0,0,1]])
    
    def rotationY(angle):
        return Matrix4D([[math.cos(angle),0,math.sin(angle),0],[0,1,0,0],[-math.sin(angle),0,math.cos(angle),0],[0,0,0,1]])
    
    def rotationZ(angle):
        return Matrix4D([[math.cos(angle), -math.sin(angle),0,0],[math.sin(angle),math.cos(angle),0,0],[0,0,1,0],[0,0,0,1]])

    def world2Camera(c):
        kc = Point.toVector(c.getAtPoint(), c.getEyePoint()).normalize()
        ic = Vector3.vectorialProduct(c.getUpPoint(), Vector3(0,0,1)).normalize()
        jc = Vector3.vectorialProduct(kc, ic).normalize()
        row1 = [ic.getI(), ic.getJ(), ic.getK(), -Vector3.scalarProduct(ic,c.getEyePoint().getVector3())]
        row2 = [jc.getI(), jc.getJ(), jc.getK(), -Vector3.scalarProduct(jc,c.getEyePoint().getVector3())]
        row3 = [kc.getI(), kc.getJ(), kc.getK(), -Vector3.scalarProduct(kc,c.getEyePoint().getVector3())]
        row4 = [0,0,0,1]
        return Matrix4D([row1, row2, row3, row4])
    
    def pontualShadowProjectionY(point):
        return Matrix4D([[point.getJ(), -point.getI(), 0, 0], [0,0,0,0], [0, -point.getK(), point.getJ(),0], [0,-1,0,point.getJ()]])
    
    def directionalShadowProjectionY(vector3):
        return Matrix4D([[1, -vector3.getI()/vector3.getJ(), 0,0 ], [0,0,0,0], [0,-vector3.getK()/vector3.getJ(),1,0],[0,0,0,1]])
    

        

    
