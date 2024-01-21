import pygame
class BtnEventHandler():
    def __init__():
        pass

    @staticmethod
    def eventHandler(button,btnEvent) -> str:
        mousePosition=None
                # if the mouse button was pressed
        if btnEvent.type == pygame.MOUSEBUTTONDOWN:
            # temp, need to generalize for all buttons
				#where was the mouse button pressed?
            mousePosition=btnEvent.pos
            	#collidepoint is a method of the rectangle class
				#if the mouse input collided with a drawn object then return buttonName
            if button.testButton.collidepoint(mousePosition):
					#return 'button {} was pressed'.format(self.btnName)
                print('button event handler name:',button.btnName)
                return button.btnName
            return None
    
    @staticmethod
    def locateEventButton(buttonDict,btnEvent):
        event=None
        for buttonName in buttonDict:
                #ask all the buttons if the mouse was pressed on their coordinate
            if BtnEventHandler.eventHandler(buttonDict[buttonName],btnEvent):
                #return appropriate button result
                event = BtnEventHandler.eventHandler(buttonDict[buttonName],btnEvent)
			
        return event
