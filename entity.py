import pygame
from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, surface, groups, pos = WINDOW_CENTER):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300