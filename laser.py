from entity import *

class Laser(Entity):
    def __init__(self, surface, pos, groups, speed = 400):
        super().__init__(surface, groups, pos, "midbottom")
        self.speed = speed


    def update(self, delta):
        self.rect.centery -= self.speed * delta
        if self.rect.bottom < 0:
            self.kill()