from vector3 import Vector3

class Material:
    def __init__(self, ambienceReflexetion, diffuseReflexetion, specularReflexetion, specularM):
        self.ambienceReflexetion = ambienceReflexetion
        self.diffuseReflexetion = diffuseReflexetion
        self.specularReflexetion = specularReflexetion
        self.normal = Vector3(0,0,0)
        self.specularM = specularM

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
    