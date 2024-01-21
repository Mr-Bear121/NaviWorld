from WindowObjects.Button import Button
from Events import ButtonEvent
from Events import WindowEvent
from SqliteInterface import DataBase
from PIL import Image
import io
import base64
import pygame
from pygame.locals import Color

def convertBG(img,imgName):
    noBG= Image.open(img)
    noBG=img.convert("RGBA")
    data=noBG.getdata()
    newData=[]
    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save('Tokens/'+imgName)
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
    astroData = astroBase.readBlobData(3)
    #screen.blit(pygame.image.fromstring(astroData,(920,764),'RGBX'))
    #print(pygame.image.load(openimgBytes(astroData)))
    #token = pygame.image.load(openimgBytes(astroData))
    #screen.blit(token, (0,0))   
    myStr = astroData[3].replace("(", "")
    myStr = myStr.replace(")", "")
    myStr = myStr.replace(",", " ")
    myList = myStr.split()
    mytuple=tuple(map(int,myList))
    #test this---->
    convertBG(astroData[1],astroData[0])
    #keep this---->
    #myImage = bytesToFile(astroData[1],astroData[0])
    #<-----keep this
    #print(myImage)
    #print(myList[0],myList[1])
    #'''assuming that the database has all required data.... this should work... but it doesnt'''
    #myImage=pygame.image.load(myImage).convert_alpha()
    #myImage.set_colorkey(Color('white'))
    myImage=pygame.image.load('Test/mapMarker_noBG.png').convert_alpha()

    #myImage.get_rect(x=myList[0],y=myList[1])
    #token = pygame.image.fromstring(astroData[0], mytuple, astroData[1])
    screen.blit(myImage, (0,0))
    pygame.display.flip()

    while True:
        #screen.blit(dest=(0,screenX),area=bottomSideBar)
        #need to seperate into a more managable form - 'Complete'
        pygame.display.update()
        gameEvent = pygame.event.get()
        #print(gameEvent,'begin')     
        for event in gameEvent:
            if WindowEvent.windowResize(event):
                screenX,screenY = resizeBackground(screen,bgImage,defaultLocation)
            if WindowEvent.imageHover(event,bottomSideBar):
                #print(gameEvent,1)
                while animationSize != -10:
                    #turn this and the previous block into a function - 'Done'
                    #cancel the animation if you are not moused over the element and reverse it
                    animationSize = increaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation) 
                    '''gameEvent = pygame.event.get()
                    if len(gameEvent) == 0:
                        pass
                    else:
                        print(gameEvent)
                        break'''
                    #create tokens and populate the bar with them, store token data in a sqlite database

                    #for event in gameEvent:
                    #    if WindowEvent.imageHover(event,bottomSideBar) == False:
                    #        while animationSize != 0:
                    #            animationSize = decreaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation)
                     #           break
                    #        break
                #if WindowEvent.imageHover(event,bottomSideBar) == False:
                #    while animationSize != 0:
                #            animationSize = decreaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation)
                #            if WindowEvent.imageHover(event,bottomSideBar):
                #                animationSize = increaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation)
            else:
                while animationSize != 0:
                    animationSize = decreaseSize(screen,animationSize,bgImageRef,screenX,screenY,defaultLocation)

                    

    return 'success'

def openimgBytes(image):
    print(type(image))
    decode = base64.b64decode(image)
    byteimage = io.BytesIO(decode)
    #byteimage = byteimage.read()
    #print(byteimage)
    image = Image.open(byteimage)
    image = image.convert('RGB')
    #image.show()
    return image

def bytesToFile(image,imageName):
    imagePath='testImages//'
    print(type(image))
    decode = base64.b64decode(image)
    byteimage = io.BytesIO(decode)
    #byteimage = byteimage.read()
    #print(byteimage)
    image = Image.open(byteimage)
    image = image.convert('RGB')
    imagePath+=imageName + '.png'
    image.save(imagePath)
    #image.show()
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