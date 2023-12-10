from light import Light
from transform import Transform

class World:
    def __init__(self, ambienceLight = Light(0,0,0)) -> None:
        self.lightSources = []
        self.ambienceLight = ambienceLight
        self.objects = []

    def world2Camera(self, camera):
        for source in self.lightSources:
            source.setPosition(Transform.world2Camera(camera, source.getPosition()))

        for object in self.objects:
            object.setPosition(Transform.world2Camera(camera, object.getPosition()))
            object.setUpDirection(Transform.world2Camera(camera, object.getUpDirection()))

    def addLightSource(self, lightSource):
        self.lightSources.append(lightSource)

    def addObject(self, object):
        self.objects.append(object)

    def getLightSources(self):
        return self.lightSources
    
    def getObjects(self):
        return self.objects

    def getAmbienceLight(self):
        return self.ambienceLight