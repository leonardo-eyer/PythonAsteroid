import pygame
from settings import ANIMATION

class AnimationHandler:
    def __init__(self):
        self.surface = {}


    def load(self, type):
        if type not in self.surface:
            self.surface[type] = [pygame.image.load(value).convert_alpha() for value in ANIMATION[type]]
            # self.surface[type] = [value for value in ANIMATION[type]]

