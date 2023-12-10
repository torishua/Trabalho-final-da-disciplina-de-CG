class Pixel:
    def __init__(self, object, light, position):
        self.position = position
        self.object = object
        self.light = light

    def getLight(self):
        return self.light
    
    def getObject(self):
        return self.object
    
    def setLight(self, light):
        self.light = light

    def setObject(self, object):
        self.object = object

    def getPosition(self):
        return self.position

    