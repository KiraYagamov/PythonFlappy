from engine import Scene, GameController, Vector2, SceneControls, Button, GameObject, SceneLoader, config
import pygame
import sys

class MenuScene(Scene):
    def __init__(self):
        super().__init__()

    def start(self):

        pygame.mixer.music.load('music/menu_music.mp3')
        pygame.mixer.music.play(-1)

        self.background = GameObject(GameController.current_screen, self, Vector2(0, 0), config.screen_size, ["sprites/Background.png"], False)

        self.play_button = Button(
            GameController.current_screen,
            self, Vector2(GameController.screen_size.x // 2 - 100, GameController.screen_size.y // 2 - 100), 
            Vector2(200, 70), 36, 
            "Играть", 
            (129,227,140), (255, 255, 255),
            'Comic Sans MS'
        )

        def on_click_play():
            SceneLoader.load_scene("GameScene")

        self.play_button.set_onclick(on_click_play)

        self.exit_button = Button(
            GameController.current_screen,
            self, Vector2(GameController.screen_size.x // 2 - 100, GameController.screen_size.y // 2 - 20), 
            Vector2(200, 70), 36, 
            "Выйти", 
            (129,227,140), (255, 255, 255),
            'Comic Sans MS'
        )

        def on_click_exit():
            pygame.quit()
            sys.exit()
        
        self.exit_button.set_onclick(on_click_exit)

    def update(self):
        self.handle_events()
        SceneControls.render_scene()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                SceneControls.click_buttons(event.pos)

