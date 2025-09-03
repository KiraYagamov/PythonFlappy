class SceneData:
    game_over = False
    points = 0
    FPS = 60
    game_objects_pool = []
    time_scale = 1

    @classmethod
    def get_points(cls):
        return cls.points

    @classmethod
    def set_points(cls, new_value):
        cls.points = new_value
