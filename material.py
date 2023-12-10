class Material:
    def __init__(self, ambienceReflexetion, diffuseReflexetion, specularReflexetion, specularM, normal):
        self.ambienceReflexetion = ambienceReflexetion
        self.diffuseReflexetion = diffuseReflexetion
        self.specularReflexetion = specularReflexetion
        self.normal = normal
        self.specularM = specularM

    def getAmbienceReflexetion(self):
        return self.ambienceReflexetion
    
    def getDiffuseReflexetion(self):
        return self.diffuseReflexetion
    
    def getSpecularReflexetion(self):
        return self.specularReflexetion
    
    def getNormal(self):
        return self.normal
    
    def getSpecularM(self):
        return self.specularM
    