from arcade import Sprite, play_sound, sound
from math import radians, sin, cos

class Laser(Sprite):
    def __new__(cls, *args, **kwargs) -> object:
        return super().__new__(cls)
    
    def __init__(self, angle, x, y) -> None:
        super().__init__(':resources:images/space_shooter/laserBlue01.png')
        self.speed = 5
        self.angle = angle + 90
        self.center_x = x
        self.center_y = y
    
    def lunch(self) -> None:
        play_sound(sound.Sound(':resources:sounds/laser4.wav'), 0.2, 0.0,False)

    def move(self) -> None:
        angle_rad = radians(self.angle - 90)
        self.center_x -= self.speed * sin(angle_rad)
        self.center_y += self.speed * cos(angle_rad)
