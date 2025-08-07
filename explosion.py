import pygame
from entity import *

class Explosion(Entity):
    def __init__(self, frames, pos, groups):
        super().__init__(frames[0], groups, pos)
        self.frames = frames
        self.index = 0

    def update(self, delta):
        self.index += 25 *delta
        if self.index < len(self.frames):
            self.image = self.frames[int(self.index)]
        else:
            self.kill()