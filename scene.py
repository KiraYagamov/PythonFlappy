from scene_data import SceneData
import pygame

class Scene:

    def __init__(self):
        self.scene_data = SceneData()
        pygame.mixer.music.stop()
        self.start()

    def start(self):
        pass

    def update(self):
        pass
