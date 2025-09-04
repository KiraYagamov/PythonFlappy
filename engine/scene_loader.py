from engine.game_controller import GameController
import engine.config as config
import importlib

class SceneLoader:

    scenes = config.scenes

    def load_scene(scene_name: str):
        for scene in SceneLoader.scenes:
            if scene["class_name"] == scene_name:
                scene_module = importlib.import_module(scene["file_name"])
                GameController.current_scene = scene_module.__getattribute__(scene_name)()