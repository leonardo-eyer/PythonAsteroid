import pygame
from random import uniform
from math import sin, pi

from pygame import Vector2

from entity import *

class Meteor(Entity):
    def __init__(self, surface, pos, groups, speed = 400):
        super().__init__(surface, groups, pos, "midbottom")
        self.speed = speed
        self.created_time = pygame.time.get_ticks()
        self.direction = pygame.Vector2(0,1)

    def despawn_timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.created_time >= 30000:
            self.kill()

    def update(self, delta):
        dt = (pygame.time.get_ticks() - self.created_time)/1000
        self.direction.x = 10*sin(dt*3)
        direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += direction * self.speed * delta
        self.despawn_timer()
