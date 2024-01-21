from abc import ABC, abstractmethod

class AbsMap(ABC):
    def __init__(self,mapImage,mapName):
        self.mapImage=mapImage
        self.mapName=mapName

