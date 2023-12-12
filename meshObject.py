from typing import Callable
from material import Material
from object import Object
from mesh import Mesh
from point import Point
from vector3 import Vector3
from transform import Transform
import math
from light import Light

class MeshObject(Object):
    def __init__(self, world, meshs: list[Mesh], position=..., upDirection=..., name='null object') -> None:
        self.meshs = meshs
        self.meshSeenIndex = -1
        super().__init__(None, None, world, position, upDirection, name)
    
    def getIntersection(self, v, p0=Point(0,0,0)):
        minTi = None
        i = -1
        for j in range(len(self.meshs)):
            tj = self.meshs[j].getIntersection()
            if minTi == None:
                minTi = tj
                i = j
            elif tj != None and tj < minTi:
                minTi = tj
                i = j

        if minTi == None or i<0:
            return None
        
        self.meshSeenIndex = self.meshs[i]
        return minTi

    
    def setPosition(self, position):
        for mesh in self.meshs:
            mesh.setPosition(position)
        self.position = position    

    def setUpDirection(self, upDirection):
        angle = math.acos(Vector3.scalarProduct(self.upDirection.normalize(), upDirection.normalize()))
        u = Vector3.vectorialProduct(self.upDirection, upDirection).normalize()
        for mesh in self.meshs:
            mesh.setUpDirection(Transform.rotation(angle, u, self.upDirection))
        self.upDirection = upDirection
    
    def getNormal(self, point):
        if self.meshSeenIndex < 0:
            return Vector3(0,0,0)
        
        normal = self.meshs[self.meshSeenIndex].getNormal()
    
    def getIntersectionLight(self, v, ti, p0 = Point(0,0,0)):
        point = Point.add(p0, Vector3.multiplyByScalar(ti, v))
        mesh = self.meshs[self.meshSeenIndex]
        material = mesh.mapFunction(mesh.materiais, Point.subtract(point, self.position))
        material.setNormal(mesh.getNormal(point))
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
    
        ambienceLight = self.world.getAmbienceLight()
        lgt = Light.calculeTotalLight(material, point, v, lightSources, ambienceLight)
        return lgt
    

    
        