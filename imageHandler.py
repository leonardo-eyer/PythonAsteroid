import pygame
from settings import IMAGES

class ImageHandler:
    def __init__(self):
        self.surface = {}


    def load(self, type):
        if type not in self.surface:
            self.surface[type] = pygame.image.load(IMAGES[type]).convert_alpha()

