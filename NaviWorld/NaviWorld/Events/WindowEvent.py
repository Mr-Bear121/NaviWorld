import pygame

def windowResize(event):
    event = event.type
    if event == pygame.VIDEORESIZE:
        return True
    else:
        return False
    
def imageHover(event,image):
    #imageSurface = image.get_rect()
    mousePos = pygame.mouse.get_pos()
    #if the mouse collides with the image then return true
    if image.collidepoint(mousePos):
        return True
    else:
        return False