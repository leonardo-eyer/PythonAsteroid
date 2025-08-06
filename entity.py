import pygame
from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, surface, groups, pos = WINDOW_CENTER, orientation = "center"):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(**{orientation:pos})
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300

        # def rot_center(image, rect, angle):
        #     """rotate an image while keeping its center"""
        #     rot_image = pygame.transform.rotate(image, angle)
        #     rot_rect = rot_image.get_rect(center=rect.center)
        #     return rot_image, rot_rect