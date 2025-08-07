import pygame
from settings import ANIMATION
from os.path import join

class AnimationHandler:
    def __init__(self):
        self.surface = {}
        self.anim_sound = pygame.mixer.Sound(join("audio", "explosion.wav"))
        self.anim_sound.set_volume(0.1)


    def load(self, type):
        if type not in self.surface:
            self.surface[type] = [pygame.image.load(value).convert_alpha() for value in ANIMATION[type]]
            # self.surface[type] = [value for value in ANIMATION[type]]

