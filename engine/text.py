import pygame
from engine.vector import Vector2

pygame.font.init()

class Text:
    def __init__(self, screen, scene, position: Vector2, font: str, text: str, font_size: int = 30, system_font=True):
        self.screen = screen
        self.position = position
        if system_font:
            self.font = pygame.font.SysFont(font, font_size)
        else:
            self.font = pygame.font.Font(font, font_size)
        self.text = text
        scene.scene_data.game_objects_pool.append(self)
    
    def draw(self):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.position.x, self.position.y))
