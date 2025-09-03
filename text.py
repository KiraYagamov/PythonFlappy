import pygame
import config
from vector import Vector2
from scene_data import SceneData

pygame.font.init()

class Text:
    def __init__(self, screen, position: Vector2, font: str, text: str, font_size: int = 30):
        self.screen = screen
        self.position = position
        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        SceneData.game_objects_pool.append(self)
    
    def draw(self):
        text_surface = self.font.render(self.text, False, (0, 0, 0))
        self.screen.blit(text_surface, (self.position.x, self.position.y))
