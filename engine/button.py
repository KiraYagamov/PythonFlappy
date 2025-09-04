from engine.vector import Vector2
from engine.game_controller import GameController
import pygame

class Button:

    def __init__(self, screen, scene, position: Vector2, size: Vector2, font_size: int, text: str, button_color, text_color, font_style: str = None):
        self.position = position
        self.size = size
        self.screen = screen
        self.text_color = text_color
        self.button_color = button_color
        self.font_size = font_size

        self.button_rect = pygame.Rect(position.x, position.y, size.x, size.y)

        self.font = pygame.font.SysFont(font_style, self.font_size)
        self.text_surface = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.button_rect.center)

        scene.scene_data.game_objects_pool.append(self)
        scene.scene_data.buttons_pool.append(self)

    def draw(self):
        pygame.draw.rect(GameController.current_screen, self.button_color, self.button_rect)
        GameController.current_screen.blit(self.text_surface, self.text_rect)
    
    def set_onclick(self, onclick):
        self.onclick = onclick
