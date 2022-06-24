from arcade import Sprite
from Laser_Class import Laser

class Spacecraft(Sprite):
    def __new__(cls, *args, **kwargs) -> object:
        return super().__new__(cls)
    
    def __init__(self, width, height):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.width = 48
        self.height = 48
        self.center_x = width // 2
        self.center_y = 48
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.change_angle = 0
        self.laser_list = []
        self.speed = 4
        self.score = 0
        self.health = 3

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def fire(self):
        lasers =[
            Laser(self.angle, self.center_x + 20, self.center_y),
            Laser(self.angle, self.center_x - 20, self.center_y)
        ]
        self.laser_list.extend(lasers)
