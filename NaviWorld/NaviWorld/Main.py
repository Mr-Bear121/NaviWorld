from WindowObjects.Button import Button
from Events import ButtonEvent
from Events import WindowEvent
from SqliteInterface import DataBase
from PIL import Image
import cv2
import io
import base64
import pygame
from pygame.locals import Color

def convertBG(img,imgName):
    print(type(img))
    noBG= Image.open("Test/"+imgName)
    return None

#need logic that says, 'when you resize the screen, resize the image'. - complete 
#goal, impliment a side bar that contains tokens that can be placed on the map. allow for editing of said tokens with notes that gets placed within a sqlite database
def appStart(screen):
    print('Main app Started')
    animationSize = 0
    bgImageRef = 'TestImages//New World.jpg'
    bgImage = pygame.image.load(bgImageRef)
    defaultLocation = (0,0)
    screenX,screenY = 0,0
    #at this point I should make 'bottomSideBar an object'
    bottomPosition=0
    screenX,screenY = (screen.get_size())
    screen.blit(pygame.transform.scale(bgImage,(screenX,screenY)), defaultLocation)
    bottomSideBar=pygame.draw.rect(screen,color=(82,206,255),rect=[0,screenY-50,screenX,50])
    astroBase = DataBase('sqliteData//tokensDB')
    astroBase.OpenDataBase()
    #modify this for new database
    astroData = astroBase.readBlobData(4)
    astroBase.writeTofile(astroData[1],astroData[0] + ".png","Test/")
    '''
    print(type(astroData))
    myStr = astroData[3].replace("(", "")
    myStr = myStr.replace(")", "")
    myStr = myStr.replace(",", " ")
    myList = myStr.split()

    mytuple=tuple(map(int,myList))
    '''
    #test this---->
    convertBG(astroData[1],astroData[0] + ".png")
    #keep this---->
    #myImage = bytesToFile(astroData[1],astroData[0])
    #<-----keep this
    myImage=pygame.image.load('Test/mapMarker_noBG.png').convert_alpha()

    screen.blit(myImage, (0,0))
    pygame.display.flip()

    while True:

        pygame.display.update()
        gameEvent = pygame.event.get()   
        for event in gameEvent:
            if WindowEvent.windowResize(event):
                screenX,screenY = resizeBackground(screen,bgImage,defaultLocation)
            if WindowEvent.imageHover(event,bottomSideBar):
                while animationSize != -10:
                    #cancel the animation if you are not moused over the element and reverse it
                    animationSize = increaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation) 
                    '''gameEvent = pygame.event.get()
                    if len(gameEvent) == 0:
                        pass
                    else:
                        print(gameEvent)
                        break'''

            else:
                while animationSize != 0:
                    animationSize = decreaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation)

                    

    return 'success'

def openimgBytes(image):
    print(type(image))
    decode = base64.b64decode(image)
    byteimage = io.BytesIO(decode)
    image = Image.open(byteimage)
    image = image.convert('RGB')
    return image

def bytesToFile(image,imageName):
    imagePath='testImages//'
    print(type(image))
    decode = base64.b64decode(image)
    byteimage = io.BytesIO(decode)
    image = Image.open(byteimage)
    image = image.convert('RGB')
    imagePath+=imageName + '.png'
    image.save(imagePath)
    return imagePath

def increaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation):
    animationSize-=1
    screen.fill((0,0,0))
    bgImage = pygame.image.load(bgImageRef)
    screen.blit(pygame.transform.scale(bgImage,(screenX,screenY)), defaultLocation)
    bottomSideBar=pygame.draw.rect(screen,color=(82,206,255),rect=[0,screenY-50 + animationSize,screenX,50 - animationSize])
    pygame.display.update()
    return animationSize

def decreaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation):
    animationSize+=1
    screen.fill((0,0,0))
    bgImage = pygame.image.load(bgImageRef)
    screen.blit(pygame.transform.scale(bgImage,(screenX,screenY)), defaultLocation)
    bottomSideBar=pygame.draw.rect(screen,color=(82,206,255),rect=[0,screenY-50 + animationSize,screenX,50 - animationSize])
    pygame.display.update()
    return animationSize

def resizeBackground(screen, bgImage,defaultLocation):
    screenX,screenY = screen.get_size()
    screen.blit(pygame.transform.scale(bgImage,screenX,screenY), defaultLocation)
    pygame.display.update()
    return screenX,screenY