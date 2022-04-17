from ctypes import DllGetClassObject
import pyxel
import random


SIZE = 200  # window size


class Personage():
    def __init__(self):
        """
        self.x, self.y -- position in game window
        self.u, self.v -- position in editor window (alternatives for x and y in pyxel editor)
        self.width --  width of personage (used in self.draw())
        self.direction -- used to choose the right skin
        """
        self.x: int = 50
        self.y: int = 50
        self.u: int = 0
        self.v: int = 0
        self.width: int = 13
        self.height: int = 27
        self.direction = 'down'
        self.moving = False
        self.skins_data = {'up': {'v': 88, 'animation_start_u': 15, 'animation_end_u': 180},
                           'right': {'v': 29, 'animation_start_u': 15, 'animation_end_u': 185},
                           'down': {'v': 58, 'animation_start_u': 15, 'animation_end_u': 165},
                           'left': {'v': 0,  'animation_start_u': 15, 'animation_end_u': 186}}

    def set_direction(self, direction: str) -> None:
        """
        Changes v coordinate to select right skin in editor

        """
        self.direction = direction
        self.v = self.skins_data[self.direction]['v']

    def moving_animation(self) -> None:
        """
        Each time called changes skin
        ? must be called from update() while moving
        """
        if not(self.moving):
            self.moving = True
            self.u = self.skins_data[self.direction]['animation_start_u']
        elif self.u >= self.skins_data[self.direction]['animation_end_u']:
            self.u = self.skins_data[self.direction]['animation_start_u']
        else:
            # 2 is offset between two separate frames in pyxel editor
            self.u = self.u + self.width+2
            self.x +=1

    def update(self):
        # ! just to verify result, will be delited
        if pyxel.btn(pyxel.KEY_R):
            self.set_direction('right')
            self.moving_animation()
        pass

    def draw(self):
        # ? last arg: "7" because white is background color
        # ! third arg: "1" because personage frames are stored in 1 image bank, (right bottom corner of pyxel image editor)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.width, self.height, 7)
        pass


class Enemy:
    def __init__(self, x, y):
        self.spawn_x = x
        self.spawn_y = y
        self.x = self.spawn_x
        self.y = self.spawn_y
        self.u = 0
        self.v = 0
        self.count = 0
        self.width = 13
        self.height = 30
        self.step = 1
        self.directions = ['right', 'down', 'left', 'up']
        self.direction = self.directions[0]

    def draw(self):
        # pyxel.blt(self.x, self.y, 3, self.u, self.v, self.width, self.height)
        pyxel.rect(self.x, self.y, 8, 8, 7)

    def change_direction(self):
        print('change_direction')
        if self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'down':
            self.direction = 'left'

    def move(self,inverted=False):
        if inverted: self.step = self.step*(-1)
        if self.direction == 'right':
            self.x += self.step

        elif self.direction == 'left':
            self.x -= self.step
        elif self.direction == 'up':
            self.y -= self.step
        elif self.direction == 'down':
            self.y += self.step
        if inverted: self.step = self.step*(-1)

    def update(self):
        # ! rename delta
        delta = 17
        print('update')
        print(self.x, ' ', self.y,' ',)
        is_in_x_diapason = self.x+self.step > self.spawn_x-delta and self.x-self.step < self.spawn_x+delta
        is_in_y_diapason =  self.y+self.step >self.spawn_y-delta and self.y-self.step < self.spawn_y+delta
        if pyxel.btn(pyxel.KEY_3):
            pass
        if is_in_x_diapason and is_in_y_diapason:
            print(self.spawn_x-delta, ' ', self.spawn_x+delta)
            self.move()
        else:
            self.move(True)
            self.change_direction()


class App:
    def __init__(self):
        pyxel.init(SIZE, SIZE, fps=12)
        pyxel.mouse(True)
        pyxel.load('my_resource.pyxres')
        global personage, enemy
        personage = Personage()
        enemy = Enemy(32, 32)

        pyxel.run(self.update, self.draw)

    def update(self):
        personage.update()
        enemy.update()

    def draw(self):
        pyxel.cls(0)
        enemy.draw()
        # personage.draw()


App()
