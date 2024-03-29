import pygame as pg
from pygame.sprite import Sprite


from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.hitpoints = 100
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
        if self.vel.y <= 0:
            hits = pg.sprite.spritecollide(self, self.game.all_mobs, False)
            if hits:
                self.hitpoints -= 2
                if self.rect.bottom >= hits[0].rect.top - 10:
                    self.rect.top = hits[0].rect.bottom
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = self.image = pg.image.load(os.path.join(img_folder, 'StFrancisPic.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        # self.pos = vec(WIDTH/2, HEIGHT/2)
        self.speed = 0
        if self.kind == "moving vertically" or "moving horizontally":
            self.speed = 5
    def update(self):
        if self.kind == "moving horizontally":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        if self.kind == "moving vertically":
            self.rect.y += self.speed
            if self.rect.y + self.rect.h > HEIGHT or self.rect.y < 0:
                self.speed = -self.speed

    def update(self):
        pass
# class Mob(Sprite):
#     def __init__(self, x, y, w, h, kind):
#         Sprite.__init__(self)
#         self.game = game_folder
#         self.image = pg.image.oad(os.path.join(img_folder, 'StFrancisPic.png')).convert()
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.kind = kind
#         self.pos = vec(WIDTH/2, HEIGHT/2)
        
    #     self.game = game
    #     self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
    #     self.image.set_colorkey(BLACK)
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (0, 0)
    #     self.pos = vec(WIDTH/2, HEIGHT/2)
    #     self.vel = vec(0,0)
    #     self.acc = vec(0,0)
    #     self.hitpoints = 100
    # def controls(self):
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_a]:
    #         self.acc.x = -5
    #     if keys[pg.K_d]:
    #         self.acc.x = 5
    #     if keys[pg.K_SPACE]:
    #         self.jump()
    # def jump(self):
    #     hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
    #     if hits:
    #         print("i can jump")
    #         self.vel.y = -PLAYER_JUMP
    # def update(self):
    #     # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
    #     self.acc = vec(0,PLAYER_GRAV)
    #     self.controls()
    #     # if friction - apply here
    #     self.acc.x += self.vel.x * -PLAYER_FRIC
    #     # self.acc.y += self.vel.y * -0.3
    #     # equations of motion
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #     self.rect.midbottom = self.pos