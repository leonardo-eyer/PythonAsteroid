from random import randint

import pygame

from imageHandler import *
from player import *
from meteor import *
from invader import *
from settings import *

def collisions():
    global running

    if pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask):
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

def score():
    current_time = pygame.time.get_ticks() // 100
    text_surface = font.render(str(current_time), True, "#ffffff")
    text_rect = text_surface.get_frect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surface, text_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), text_rect.inflate(20,10).move(0, -7), 5, 10)


pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SCALED, vsync=True)
pygame.display.set_caption('Asteroid')
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
img = ImageHandler()
img.load("star")
img.load("laser")
img.load("player")
img.load("meteor")
img.load("invader")
font = pygame.font.Font(FONT, 40)


for i in range(20):
    Entity(
        img.surface["star"],
        all_sprites,
        (randint(50, WINDOW_WIDTH - 50), randint(50,WINDOW_HEIGHT - 50))
    )
player = Player(img.surface["player"], img.surface["laser"], [all_sprites, laser_sprites])

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)
# Meteor(img.surface["invader"], (300, -10), all_sprites)
while running:
    dt = clock.tick(75) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(img.surface["meteor"], (randint(0, WINDOW_WIDTH - 50), -10), (all_sprites, meteor_sprites))
            # Meteor(img.surface["invader"], (300, -10), all_sprites)

    all_sprites.update(dt)
    collisions()

    display_surface.fill("#3a2e3f")
    score()
    all_sprites.draw(display_surface)


    pygame.display.update()

pygame.quit()