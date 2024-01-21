import sys

sys.path.append('..')
from Abstractions.TokenAbc import TokenABC
class Token:

    def __init__(self,tokenImage,tokenName) -> None:
        self.tokenImage=tokenImage
        self.tokenName=tokenName
