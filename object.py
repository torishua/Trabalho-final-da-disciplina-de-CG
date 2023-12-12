from material import Material
from vector3 import Vector3
from point import Point
from world import World
from light import Light
from typing import Callable

class Object:
    def __init__(self, materials: list[Material], mapFunction: Callable[[list[Material], Point], Material], world, position = Point(0,0,0), upDirection = Vector3(0,1,0), name = 'null object') -> None:
        self.materiais = materials
        self.mapFunction = mapFunction
        self.world = world
        self.position = position
        self.upDirection = upDirection
        self.name = name

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getUpDirection(self):
        return self.upDirection
    
    def setMaterialList(self, materials):
        self.materiais = materials

    def getMaterialList(self):
        return self.materiais
    
    def setUpDirection(self, upDirection):
        self.upDirection = upDirection

    def setMapFunction(self, mapFunction):
        self.mapFunction = mapFunction
    
    def getIntersection(self, v, p0=Point(0,0,0)):
        '''Retorna o Ti do p0 + ti*v'''
        raise Exception("Method not implemented")
    
    def getNormal(self, point):
        raise Exception("Method not implemented")
    
    def getIntersectionLight(self, v, ti, p0 = Point(0,0,0)):
        point = Point.add(p0, Vector3.multiplyByScalar(ti, v))
        material = self.mapFunction(self.materiais, Point.subtract(point, self.position))
        material.setNormal(self.getNormal(point))
        lightSources = self.world.getLightSources()
        objects = self.world.getObjects()
        usableSources = []
        for source in lightSources:
            shadowed = False
            ushadow = source.getVector3At(point).normalize()
            for object in objects:
                if object != self:
                    ti = object.getIntersection(ushadow, point)
                    if ti != None:
                        shadowed = True
                        break
            if not shadowed:
                usableSources.append(source)


        ambienceLight = self.world.getAmbienceLight()
        lgt = Light.calculeTotalLight(material, point, v, usableSources, ambienceLight)
        return lgt
    

        
    def __str__(self) -> str:
        return self.name
        
    

