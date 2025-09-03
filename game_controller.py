import config


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
    def __init__(self):
        pass
