from material import Material
from vector3 import Vector3
from point import Point
from world import World
from light import Light
from typing import Callable

class Object:
    def __init__(self, materials: list[Material], mapFunction: Callable[[list[Material], Point], Material], world, position = Point(0,0,0), upDirection = Vector3(0,1,0)) -> None:
        self.materiais = materials
        self.mapFunction = mapFunction
        self.world = world
        self.position = position
        self.upDirection = upDirection

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getUpDirection(self):
        return self.upDirection
    
    def setUpDirection(self, upDirection):
        self.upDirection = upDirection

    def setMapFunction(self, mapFunction):
        self.mapFunction = mapFunction
    
    def getIntersection(self, v, p0=Point(0,0,0)):
        '''Retorna o Ti do p0 + ti*v'''
        raise Exception("Method not implemented")
    
    def getNormal(self, point):
        raise Exception("Methode not implemented")
    
    def getIntersectionLight(self, v, ti, p0 = Point(0,0,0)):
        point = Point.add(p0, Vector3.multiplyByScalar(ti, v))
        material = self.mapFunction(self.materiais, Point.subtract(point, self.position))
        material.setNormal(self.getNormal(point))
        lightSources = self.world.getLightSources()
        ambienceLight = self.world.getAmbienceLight()
        lgt = Light.calculeTotalLight(material, point, v, lightSources, ambienceLight)
        return lgt
        
        
    

