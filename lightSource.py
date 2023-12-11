class LightSource:
    def __init__(self, intensity, position):
        self.intensity = intensity
        self.position = position

    def getIntensity(self):
        return self.intensity
    
    def getPosition(self):
        return self.position
    
    def setIntensity(self, intensity):
        self.intensity = intensity

    def setPosition(self, position):
        self.position = position

        
