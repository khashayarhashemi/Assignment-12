from arcade import Sprite, play_sound, sound
from random import randint

class Enemy(Sprite):
    def __new__(cls, *args, **kwargs) -> object:
        return super().__new__(cls)
    
    def __init__(self, width, height, speed: int=3) -> None:
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png')
        self.speed = speed
        self.center_x = randint(0, width)
        self.center_y = height
        self.angle = 180
        self.width = 50
        self.height = 50
    
    def hit(self) -> None:
        play_sound(sound.Sound(':resources:sounds/explosion1.wav'), 1.0, 0.0,False)
    
    def move(self) -> None:
        self.center_y -= self.speed
