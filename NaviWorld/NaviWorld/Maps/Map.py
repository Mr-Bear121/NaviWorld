import sys
sys.path.append('..')
from Abstractions import AbsMap
class Map(AbsMap):
    def __init__(self,mapImage,mapName):
        self.mapImage=mapImage
        self.mapName=mapName

    def createMap(self):
        return Map(self.mapImage,self.mapName)