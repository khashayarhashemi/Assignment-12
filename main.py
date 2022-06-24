from arcade import Window, set_background_color, color, key, run, load_texture, draw_text, start_render, draw_lrwh_rectangle_textured, check_for_collision
from random import randint
from time import time
from os import path
from Spacecraft_Class import Spacecraft
from Enemy_Class import Enemy

class Game(Window):
    def __new__(cls, *args, **kwargs) -> object:
        return super().__new__(cls)
    
    def __init__(self, fontSize: int=40) -> None:
        self.w = 800
        self.h = 600
        super().__init__(self.w, self.h, title="Star Wars")
        set_background_color(color.BLACK)
        self.fontSize = fontSize
        self.background_image = load_texture(':resources:images/backgrounds/stars.png')
        self.me = Spacecraft(self.w, self.h)
        self.enemy = Enemy(self.w, self.h)
        self.next_enemy_time = randint(2, 5)
        self.enemy_list = []
        self.game_start_time = time()
        self.start_time = time()
        self.health_image = load_texture('{path}/assets/heart.png'.format(path=path.dirname(__file__)))

    def on_draw(self) -> None:
        start_render()
        if self.me.health<=0:
            draw_text('GAME OVER', self.w // 2 - 200, self.h // 2, color.WHITE, self.fontSize // 2, width=400, align='center')
        else:
            draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
            self.me.draw()
            for i in range(len(self.me.laser_list)):
                self.me.laser_list[i].draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
            for i in range(self.me.health):
                draw_lrwh_rectangle_textured(10 + i * 35 ,10 ,30 ,30 ,self.health_image)
            draw_text('Score: %i'%self.me.score, self.w-130, 10, color.WHITE, self.fontSize // 2, width=200, align='left')
    
    def on_update(self, delta_time) -> None:
        self.end_time = time()
        if self.end_time - self.start_time > self.next_enemy_time:
            self.next_enemy_time = randint(2, 6)
            self.enemy_list.append(Enemy(self.w, self.h, 3+(self.end_time-self.game_start_time)//24))
            self.start_time = time()
        self.me.rotate()
        self.me.move()
        for i in range(len(self.me.laser_list)):
            self.me.laser_list[i].move()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()
        for enemy in self.enemy_list:
            for bullet in self.me.laser_list:
                if check_for_collision(bullet, enemy):
                    enemy.hit()
                    self.me.laser_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    self.me.score += 1
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.me.health -= 1
                self.enemy_list.remove(enemy)
        for bullet in self.me.laser_list:
            if bullet.center_y > self.height or bullet.center_x < 0 or bullet.center_x > self.width:
                self.me.laser_list.remove(bullet)
    
    def on_key_press(self, keyPressed, modifiers) -> None:
        if keyPressed == key.UP:
            self.me.change_y = 1
        elif keyPressed == key.DOWN:
            self.me.change_y = -1
        elif keyPressed == key.RIGHT:
            self.me.change_x = 1.5
        elif keyPressed == key.LEFT:
            self.me.change_x = -1.5
        elif keyPressed == key.C:
            self.me.change_angle = 1
        elif keyPressed == key.V:
            self.me.change_angle = -1
        elif keyPressed == key.SPACE:
            self.me.fire()
            self.me.laser_list[-1].lunch()
    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0
        self.me.change_x = 0
        self.me.change_y = 0

if __name__ == '__main__':
    Game()
    run()
