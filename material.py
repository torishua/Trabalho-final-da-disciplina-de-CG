from vector3 import Vector3

class Material:
    def __init__(self, ambienceReflexetion, diffuseReflexetion, specularReflexetion, specularM, color=None, image=None, textWidth=None, textHeight=None):
        self.ambienceReflexetion = ambienceReflexetion
        self.diffuseReflexetion = diffuseReflexetion
        self.specularReflexetion = specularReflexetion
        self.normal = Vector3(0,0,0)
        self.specularM = specularM
        self.color = color
        self.image = image
        self.textWidht = textWidth
        self.textHeight = textHeight
        #nem sei se isso da textura e cor da certokkkk

    def getAmbienceReflexetion(self):
        return self.ambienceReflexetion
    
    def getDiffuseReflexetion(self):
        return self.diffuseReflexetion
    
    def getSpecularReflexetion(self):
        return self.specularReflexetion
    
    def setNormal(self, normal):
        self.normal = normal
    
    def getNormal(self):
        return self.normal
    
    def getSpecularM(self):
        return self.specularM
    
    def getColor(self):
        return self.color
    
    def getImage(self):
        return self.image
    
    def gettextWidth(self):
        return self.textWidht
    
    def gettextHeight(self):
        return self.textHeight


    
    