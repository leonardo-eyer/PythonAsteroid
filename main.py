import pygame
from random import randint
from imageHandler import *
from player import *
from settings import *

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid')
running = True
clock = pygame.time.Clock()

laser_surf = pygame.image.load("images/laser.png").convert_alpha()
meteor_surf = pygame.image.load("images/meteor.png").convert_alpha()

all_sprites = pygame.sprite.Group()
img = ImageHandler()
img.load("star")
img.load("player")
for i in range(20):
    Entity(
        img.surface["star"],
        all_sprites,
        (randint(50, WINDOW_WIDTH - 50), randint(50,WINDOW_HEIGHT - 50))
    )
player = Player(img.surface["player"], all_sprites)

while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)
    display_surface.fill("darkgray")
    all_sprites.draw(display_surface)
    pygame.display.update()

pygame.quit()