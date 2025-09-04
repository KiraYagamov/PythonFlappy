import pygame
import engine.config as config

class GameController:
    current_scene = None
    current_screen = None
    screen_size = config.screen_size
    delta_time = 0
    open('record.txt', 'a').close()
    with open("record.txt", "r") as f:
        try:
            points_record = int(f.read())
        except:
            points_record = 0
    
    def create_game(screen_size, caption, onstart):
        pygame.init()
        GameController.screen_size = screen_size
        GameController.current_screen = pygame.display.set_mode(
            (GameController.screen_size.x, GameController.screen_size.y),
            flags=pygame.SCALED,
            vsync=1
        )

        pygame.display.set_caption(caption)
        clock = pygame.time.Clock()
        if onstart != None:
            onstart()

        # Starting game cycle
        while True:
            GameController.delta_time = clock.tick(GameController.current_scene.scene_data.FPS) / 1000.0 * GameController.current_scene.scene_data.time_scale
            GameController.current_scene.update()

