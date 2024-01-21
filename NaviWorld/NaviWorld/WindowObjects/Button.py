import pygame
import sys
sys.path.append('../')
from Events.ButtonEvent import BtnEventHandler
class Button():
	def __init__(self,btnName, image, pos, text_input, font, base_color, hovering_color,buttonAction=None, btnFunc=None):
		self.btnName=btnName
		#reference to a function
		self.btnAction=btnFunc
		self.imageNotNone=False
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.rect=None
		#note of reference of test button must be temp... fix later
		self.testButton=None
		if self.image is None:
			#self.image = self.text
			self.imageNotNone=False
		else:
			self.imageNotNone=True
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		#self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	
	'''def eventHandler(self,btnEvent):
			mousePosition=None
                # if the mouse button was pressed
			if btnEvent.type == pygame.MOUSEBUTTONDOWN:
            # temp, need to generalize for all buttons
				#where was the mouse button pressed?
				mousePosition=btnEvent.pos
            	#collidepoint is a method of the rectangle class
				#if the mouse input collided with a drawn object then return true
				if self.testButton.collidepoint(mousePosition):
					#return 'button {} was pressed'.format(self.btnName)
					return True
				return False
			#return 'no event'''
	
	def buttonAction(self,*args):
		#I want a generic way of attaching a function to my action and then allowing for any number of required arguements to pass into this function - 'done'
		if self.btnAction !=None:
			#to date... weirdest thing ive ever figured out.... but if *args works then *args works.
			return self.btnAction(*args)
		else:
			return 'no action'

	
	def display(self, screen):
		#if self.image is not None:
		if self.imageNotNone:
			screen.blit(self.image, self.rect)
		else:
			#need to change this so that color can be changed
			self.testButton = pygame.draw.rect(screen,(82,206,255),[self.x_pos-69,self.y_pos-22,140,40])
		#.blit draws an image or text. can draw a rectangle if you have a rectangle png
		screen.blit(self.text, self.text_rect)
	

	def checkForInput(self, position): 
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print('yes')
			return True
		
		return False
	
	

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	