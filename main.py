# Initialize libs
import pygame
import sys
from random import randint
from gameobject import GameObject
from vector import Vector2
from text import Text
from scene_data import SceneData
from scene_controls import SceneControls

# Initialize window
pygame.init()
screen_size = Vector2(500, 800)
screen = pygame.display.set_mode((screen_size.x, screen_size.y), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()

# Initialize music
pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.play(-1)

# Game objects
backgrounds_images = ["sprites/Background.png", "sprites/NightBackground.png"]
background = GameObject(screen, Vector2(0, 0), screen_size, [backgrounds_images[0]], False)
player = GameObject(screen, Vector2(70, 150), Vector2(80, 60), ["sprites/Bird.png", "sprites/Bird2.png", "sprites/Bird3.png"])
pipe_top = GameObject(screen, Vector2(1000, -200), Vector2(100, 500), ["sprites/Enemy.png"], False)
pipe_bottom = GameObject(screen, Vector2(1000, 500), Vector2(100, 500), ["sprites/Enemy.png"], False)
pipe_bottom.flip(False, True)
points_text = Text(screen, Vector2(350, 0), 'Comic Sans MS', f"Points: {SceneData.points}")

# Start values of some game objects
pipe_top.velocity.x = -5
pipe_bottom.velocity.x = -5
player.velocity.y = 5

background_timer = 0
background_switched = False

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not SceneData.game_over:
                player.velocity.y = 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.velocity.y = 5

def check_enemy_position():
    if pipe_top.position.x < -pipe_top.size.x:
        pipe_top.position.x = 600
        pipe_bottom.position.x = 600
        y_move_delta = randint(-150, 150)
        pipe_top.position.y = -200 + y_move_delta
        pipe_bottom.position.y = 500 + y_move_delta
        SceneData.set_points(SceneData.get_points() + 1)
        points_text.text = f"Points: {SceneData.points}"

def check_collisions():
    collision_upper = player.mask.overlap(pipe_top.mask, player.offset(pipe_top.position))
    collision_bottom = player.mask.overlap(pipe_bottom.mask, player.offset(pipe_bottom.position))
    if collision_upper or collision_bottom:
        pipe_top.velocity.x = 0
        pipe_bottom.velocity.x = 0
        SceneData.game_over = True

def check_player_fly_height():
    if player.position.y < 0:
        player.position.y = 0
    if player.position.y > screen_size.y:
        pygame.quit()
        sys.exit()

# Starting game cycle
while True:
    delta_time = clock.tick(SceneData.FPS) / 1000.0 * SceneData.time_scale
    # Event handlers
    handle_events()

    check_enemy_position()
    check_collisions()
    check_player_fly_height()
    
    # Moving game objects (if they are enabled to move)
    SceneControls.move_objects(delta_time)
    # Drawing all of game objects
    SceneControls.render_scene()

    if not background_switched:
        background_timer += delta_time
        if background_timer > 17:
            background.set_sprite(backgrounds_images[1])
            SceneData.time_scale *= 2
            pipe_top.velocity.x *= 1.5
            pipe_bottom.velocity.x *= 1.5
            background_timer = 0
            background_switched = True
