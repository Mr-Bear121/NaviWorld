import traceback
import pygame
from pygame.locals import Color

if __name__ == '__main__':
    try:
        initialize =pygame.init()
        screen=pygame.display.set_mode((1280,970))
        myImage='Test/mapMarker_noBG.png'
        myImage=pygame.image.load(myImage).convert_alpha()
        myImage.set_colorkey(Color('white'))
        
        while True:
            screen.blit(myImage, (0,0))
            pygame.display.flip()
            pygame.display.update()
    except Exception as ex:
        print(f'an exception has occured:{ex}')
        traceback.print_exception(ex)