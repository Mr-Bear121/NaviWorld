'''
might brand this app as northstar or astrolabe
'''
#import tkinter as tk
import pygame
#need to make a button object so i can dynamically create buttons
from WindowObjects.Button import Button
from Events.ButtonEvent import BtnEventHandler
import re
import pygame_menu
import traceback
import sys
import Main


def set_difficulty(value, difficulty):
    # Do the job here !
    pass
'''def displayElement(displayScreen,*kwargs):
    for element in kwargs:
        screen.blit(buttonText,menuButton)'''
def createMenuBtns():

    return{'Play':Button(btnName='Play',image=None,pos=(640, 250), 
                    text_input="PLAY", font=pygame.font.Font("Assets/font.ttf", 20),
                    base_color="#6cd9f5", hovering_color="White", btnFunc=Main.appStart),
    'Settings':Button(btnName='Settings',image=None,pos=(640, 350), 
                    text_input="Settings", font=pygame.font.Font("Assets/font.ttf", 20),
                    base_color="#6cd9f5", hovering_color="White"),
    'Exit':Button(btnName='Exit',image=None,pos=(640, 450), 
                    text_input="Exit", font=pygame.font.Font("Assets/font.ttf", 20),
                    base_color="#6cd9f5", hovering_color="White")}

def display(screen,element):
	#if self.image is not None:
	if element.image!=None:
		screen.blit(element.image, element.rect)
	else:
		element.testButton = pygame.draw.rect(screen,(8, 50, 189),[element.x_pos-69,element.y_pos-22,140,40])
	#.blit draws an image or text. can draw a rectangle if you have a rectangle png
	screen.blit(element.text, element.text_rect)

def startMenu():
    screenBtns={}
    mousePosition=None
    screen=pygame.display.set_mode((1280,970))
    screenBtns=createMenuBtns()
    screen.fill((0,0,0))
    #allows only a portion of the screen to be updated, instead of the entire area. If no argument is passed it updates the entire Surface area like pygame.
    for key in screenBtns:
            print(screenBtns[key])
            display(screen,screenBtns[key])
    pygame.display.set_caption('Astrolabe')
    pygame.display.update()
    #odd reaction, press button everything fine. press background, stuck in infinite loop. must correct later
    while True:
        event=None
        for btnEvent in pygame.event.get():
            #mousePosition = BtnEvent.buttonEvent(btnEvent)
            #ask all the buttons if the mouse was pressed on their coordinate
            event=BtnEventHandler.locateEventButton(screenBtns,btnEvent)
            #print(re.findall('button .* was pressed','button Play was pressed'))
            #if event == re.search('button .* was pressed',event):
            if  event != None:
                # if a button was pressed then perform action based on button name 'or button position'
                if event.lower() == "play":
                     #clear screen so that you can redraw images
                     screen.fill((0,0,0))
                     #need to seperate into a more managable form
                     #screen.blit(pygame.transform.scale(pygame.image.load('TestImages//New World.jpg'),(screen.get_size())), (0,0))
                     pygame.display.update() 
                     print(screenBtns['Play'].buttonAction(screen))                    
                elif event.lower() == 'settings':
                    pass
                elif event.lower() == 'exit':
                     pass
                    
                print("event name:",event)
                print(btnEvent)

        menuEvent=pygame.event.get()

    #return screen

if __name__ == '__main__':
    try:

        #returns a tuple of containing the number of successfull modules initialized
        Poweron = pygame.init()
        gameScreen=pygame.display.set_mode((600,400))
        screen=startMenu()
        #screen.mainloop()
    except Exception as ex:
        print(f'an exception has occured:{ex}')
        traceback.print_exception(ex)