from engine import GameController, config, SceneLoader

GameController.create_game(config.screen_size, "Flappy bird", lambda: SceneLoader.load_scene("MenuScene"))
