from math import sin
from entity import *

class Invader(Entity):
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
        if self.rect.centery >= WINDOW_HEIGHT/2:
            self.direction.y = 0
            if (self.rect.centerx < WINDOW_WIDTH/2 and self.direction.x > 0)\
                or (self.rect.centerx > WINDOW_WIDTH/2 and self.direction.x < 0):
                self.direction.x *= -1
        else:
            dt = (pygame.time.get_ticks() - self.created_time)/1000
            self.direction.x = 10*sin(dt*3)
            self.direction.y = 1

        if self.direction:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * delta



        self.despawn_timer()
