from scene import Scene
import pygame
from gameobject import GameObject
from text import Text
from game_controller import GameController
from vector import Vector2
import sys
from random import randint
from scene_controls import SceneControls
from scene_loader import SceneLoader
import config

class GameScene(Scene):

    def __init__(self):
        super().__init__()

    def start(self):

        self.game_over = False
        self.points = 0

        # Initialize music
        pygame.mixer.music.load('music/music.mp3')
        pygame.mixer.music.play(-1)

        # Game objects
        self.backgrounds_images = ["sprites/Background.png", "sprites/NightBackground.png"]
        self.background = GameObject(GameController.current_screen, self, Vector2(0, 0), config.screen_size, [self.backgrounds_images[0]], False)
        self.player = GameObject(GameController.current_screen, self, Vector2(70, 150), Vector2(80, 60), ["sprites/Bird.png", "sprites/Bird2.png", "sprites/Bird3.png"])
        self.pipe_top = GameObject(GameController.current_screen, self, Vector2(1000, -200), Vector2(100, 500), ["sprites/Enemy.png"], False)
        self.pipe_bottom = GameObject(GameController.current_screen, self, Vector2(1000, 500), Vector2(100, 500), ["sprites/Enemy.png"], False)
        self.pipe_bottom.flip(False, True)
        self.points_text = Text(GameController.current_screen, self, Vector2(350, 0), 'Comic Sans MS', f"Points: {self.points}")

        # Start values of some game objects
        self.pipe_top.velocity.x = -5
        self.pipe_bottom.velocity.x = -5
        self.player.velocity.y = 5

        self.background_timer = 0
        self.background_switched = False

    def update(self):
        self.handle_events()

        self.check_enemy_position()
        self.check_collisions()
        self.check_player_fly_height()
        
        # Moving game objects (if they are enabled to move)
        SceneControls.move_objects(GameController.delta_time)
        # Drawing all of game objects
        SceneControls.render_scene()

        if not self.background_switched:
            self.background_timer += GameController.delta_time
            if self.background_timer > 17:
                self.background.set_sprite(self.backgrounds_images[1])
                GameController.current_scene.scene_data.time_scale *= 2
                self.pipe_top.velocity.x *= 1.5
                self.pipe_bottom.velocity.x *= 1.5
                self.background_timer = 0
                self.background_switched = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.player.velocity.y = 5
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.velocity.y = 5

    def check_enemy_position(self):
        if self.pipe_top.position.x < -self.pipe_top.size.x:
            self.pipe_top.position.x = 600
            self.pipe_bottom.position.x = 600
            y_move_delta = randint(-150, 150)
            self.pipe_top.position.y = -200 + y_move_delta
            self.pipe_bottom.position.y = 500 + y_move_delta
            self.points += 1
            self.points_text.text = f"Points: {self.points}"

    def check_collisions(self):
        collision_upper = self.player.mask.overlap(self.pipe_top.mask, self.player.offset(self.pipe_top.position))
        collision_bottom = self.player.mask.overlap(self.pipe_bottom.mask, self.player.offset(self.pipe_bottom.position))
        if collision_upper or collision_bottom:
            self.pipe_top.velocity.x = 0
            self.pipe_bottom.velocity.x = 0
            self.game_over = True

    def check_player_fly_height(self):
        if self.player.position.y < 0:
            self.player.position.y = 0
        if self.player.position.y > GameController.screen_size.y:
            SceneLoader.load_scene("MenuScene")
