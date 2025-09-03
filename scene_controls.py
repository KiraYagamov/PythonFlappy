import pygame
from gameobject import GameObject
from vector import Vector2
from scene_data import SceneData

class SceneControls:
    def move_objects(delta_time: float):
        for obj in SceneData.game_objects_pool:
            if isinstance(obj, GameObject) and obj.velocity != Vector2.zero():
                obj.move(delta_time)

    def render_scene():
        for obj in SceneData.game_objects_pool:
            obj.draw()
        pygame.display.flip()
