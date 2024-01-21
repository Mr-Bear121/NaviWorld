from abc import ABC, abstractmethod

class TokenABC(ABC):
    def __init__(self,tokenImage,tokenName):
        self.tokenImage=tokenImage
        self.tokenName=tokenName