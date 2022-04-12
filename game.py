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

    def set_direction(self):
        """
        changes u coordinate to select right skin in editor
        coordinate v corresponds to direction

        """

        if self.direction == "left":
            # self.width = self.frames_info['horizontal']['width']
            self.v = 0
        elif self.direction == "right":
            # self.width = self.frames_info['horizontal']['width']
            self.v = 28
        elif self.direction == "front":
            # self.width = self.frames_info['vertical']['width']
            self.v = 56
        elif self.direction == "back":
            # self.width = self.frames_info['vertical']['width']
            self.v = 84

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.width, self.height)


class App:
    def __init__(self):
        pyxel.init(SIZE, SIZE, fps=10)
        pyxel.load('my_resource.pyxres')

        self.personage = Personage()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.personage.update()

    def draw(self):
        pyxel.cls(0)
        self.personage.draw()


App()
