import pygame
import config
from vector import Vector2
from scene_data import SceneData

class GameObject:
    def __init__(self, screen, position: Vector2, size: Vector2, sprites_paths: str, has_gravity=True):
        self.position = position
        self.size = size
        self.sprites = []
        for sprite_path in sprites_paths:
            self.sprites.append(pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (size.x, size.y)))
        self.current_sprite = 0
        self.sprite_time = 0
        self.screen = screen
        self.velocity = Vector2(0, 0)
        self.has_gravity = has_gravity
        self.mask = pygame.mask.from_surface(self.sprites[0])
        SceneData.game_objects_pool.append(self)

    def draw(self):
        self.screen.blit(self.sprites[self.current_sprite], (self.position.x, self.position.y))
        self.sprite_time += 0.1
        if self.sprite_time > 1:
            self.next_sprite()
            self.sprite_time = 0
        
    def move(self, delta_time):
        if self.has_gravity:
            self.velocity.y -= config.gravity * delta_time
        self.position.y  -= self.velocity.y
        self.position.x += self.velocity.x

    def flip(self, flipX, flipY):
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.flip(self.sprites[i].convert_alpha(), flipX, flipY)
        self.mask = pygame.mask.from_surface(self.sprites[0])
    
    def offset(self, other):
        return int(other.x - self.position.x), int(other.y - self.position.y)
    
    def next_sprite(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
    
    def set_sprite(self, sprite_path):
        self.sprites = [pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (self.size.x, self.size.y))]
