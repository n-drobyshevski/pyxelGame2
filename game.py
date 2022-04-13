import pyxel


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


class App:
    def __init__(self):
        pyxel.init(SIZE, SIZE, fps=12)
        pyxel.load('my_resource.pyxres')

        self.personage = Personage()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.personage.update()

    def draw(self):
        pyxel.cls(0)
        self.personage.draw()


App()
