import pygame.time
from laser import *

class Player(Entity):
    def __init__(self, surface, laser_surface, groups):
        super().__init__(surface, groups)
        self.groups = groups
        self.laser_surface = laser_surface
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown_duration = 500

    def shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, delta):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * delta

        # recent_keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] and self.can_shoot:
            # shouldn't be creating entities
            Laser(self.laser_surface, self.rect.topleft, self.groups)
            Laser(self.laser_surface, self.rect.midtop, self.groups)
            Laser(self.laser_surface, self.rect.topright, self.groups)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

        self.shoot_timer()