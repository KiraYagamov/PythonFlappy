class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def zero():
        return Vector2(0, 0)
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y