from random import uniform, randint
from entity import *

class Meteor(Entity):
    def __init__(self, surface, pos, groups, speed = 400):
        super().__init__(surface, groups, pos, "midbottom")
        self.speed = speed
        self.created_time = pygame.time.get_ticks()
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.rotation_speed = randint(40,70)
        self.rotation = 0

    def despawn_timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.created_time >= 30000:
            self.kill()

    def update(self, delta):
        self.rotation += self.rotation_speed * delta
        self.image = pygame.transform.rotozoom(self.original_surface, self.rotation, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

        self.direction.y = 1
        if self.direction:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed * delta
        self.despawn_timer()
