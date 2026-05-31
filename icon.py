import pygame

class Icon:
    def __init__(self, src):
        self.src = src
    
    def render_icon(self):
        myimage = pygame.image.load(self.src)
        imagerect = myimage.get_rect()
        return myimage, imagerect