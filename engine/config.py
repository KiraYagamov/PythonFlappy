from engine.vector import Vector2
import json

gravity = 10
screen_size = Vector2(500, 800)
scenes = []

try:
    with open("./config.json", "r") as config_file:
        try:
            config_data = json.loads(config_file.read())
            gravity = config_data["gravity"]
            screen_size = Vector2(config_data["screen_size"][0], config_data["screen_size"][1])
            scenes = config_data["scenes"]
            print("Конфиг успешно загружен!")
        except:
            print("Некорректный конфиг! Применяю стандартные значения!")
            gravity = 10
            screen_size = Vector2(500, 800)
except:
    print("Файл конфига не найден! Применяю стандартные значения!")
    gravity = 10
    screen_size = Vector2(500, 800)
