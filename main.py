from random import randint
from imageHandler import *
from player import *
from meteor import *
from invader import *
from settings import *


pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SCALED, vsync=True)
pygame.display.set_caption('Asteroid')
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
img = ImageHandler()
img.load("star")
img.load("laser")
img.load("player")
img.load("meteor")
img.load("invader")
for i in range(20):
    Entity(
        img.surface["star"],
        all_sprites,
        (randint(50, WINDOW_WIDTH - 50), randint(50,WINDOW_HEIGHT - 50))
    )
player = Player(img.surface["player"], img.surface["laser"], all_sprites)

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)
# Meteor(img.surface["invader"], (300, -10), all_sprites)
while running:
    dt = clock.tick(75) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(img.surface["meteor"], (randint(0, WINDOW_WIDTH - 50), -10), all_sprites)
            # Meteor(img.surface["invader"], (300, -10), all_sprites)

    all_sprites.update(dt)
    display_surface.fill("darkgray")
    all_sprites.draw(display_surface)


    pygame.display.update()

pygame.quit()