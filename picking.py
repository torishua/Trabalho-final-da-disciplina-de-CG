from pixel import Pixel

class Picking:
    def __init__(self, camera, matrixOfPixels) -> None:
        self.camera = camera
        self.matrixOfPixels = matrixOfPixels

    def getPixel(self, x, y):
        return self.matrixOfPixels[y][x]

    def pickObjectByPixel(self, x, y):
        pixel = self.getPixel(x,y)
        return pixel.getObject()