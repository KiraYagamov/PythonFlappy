import pygame
from engine.gameobject import GameObject
from engine.vector import Vector2
from engine.game_controller import GameController

class SceneControls:
    def move_objects(delta_time: float):
        for obj in GameController.current_scene.scene_data.game_objects_pool:
            if isinstance(obj, GameObject) and obj.velocity != Vector2.zero():
                obj.move(delta_time)

    def render_scene():
        for obj in GameController.current_scene.scene_data.game_objects_pool:
            obj.draw()
        pygame.display.flip()
    
    def click_buttons(pos):
        for b in GameController.current_scene.scene_data.buttons_pool:
            if b.button_rect.collidepoint(pos):
                if hasattr(b, "onclick"):
                    b.onclick()
