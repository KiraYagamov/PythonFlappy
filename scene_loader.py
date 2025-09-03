from game_controller import GameController

class SceneLoader:

    def load_scene(scene_name: str):
        from menu_scene import MenuScene
        from game_scene import GameScene    
        match scene_name:
            case "MenuScene":
                GameController.current_scene = MenuScene()
            case "GameScene":
                GameController.current_scene = GameScene()
