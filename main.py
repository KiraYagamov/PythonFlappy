# Initialize libs
import pygame
from game_controller import GameController
from scene_loader import SceneLoader


# Initialize window
pygame.init()
GameController.current_screen = pygame.display.set_mode(
    (GameController.screen_size.x, GameController.screen_size.y),
    flags=pygame.SCALED,
    vsync=1
)

pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
SceneLoader.load_scene("MenuScene")


# Starting game cycle
while True:
    GameController.delta_time = clock.tick(GameController.current_scene.scene_data.FPS) / 1000.0 * GameController.current_scene.scene_data.time_scale
    GameController.current_scene.update()
