import pyxel


SIZE = 200  # window size


class Personage():
    def __init__(self):
        """
        self.x, self.y -- position in game window
        self.u, self.v -- position in editor window (alternatives for x and y in pyxel editor)
        self.width --  width of personage (used in self.draw())
        self.direction -- used to choose the right skin
        self.moving -- is personage moving (necessary for moving animation)
        """
        self.x: int = 50
        self.y: int = 50
        self.u: int = 0
        self.v: int = 0
        self.width: int = 16
        self.direction = 'right'
        self.moving: bool = False

    def set_direction(self):
        """
        changes u coordinate to select right skin in editor
        """
        if self.direction == "left":
            self.u = 0
        if self.direction == "right":
            self.u = 16
        if self.direction == "front":
            self.u = 32
        if self.direction == "back":
            self.u = 48

    def move(self):
        """
        personage move implementation
        variables:
            v - "y" coordinate of line with move animation frames in Editor
            start_u, end_u - horizontal limits of line with move animation frames in Editor
            width - width of personage while moving is diffrent to idling
        """
        v = 32
        start_u = 14
        end_u = 112
        self.width = 14
        if self.moving == False:
            self.v = v
            self.u = start_u
            self.moving = True
        elif self.u >= end_u:
            self.u = start_u
        else:
            # self.x+=2
            self.u += 14

    def update(self):
        # self.x = (self.x + 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_A):
            self.direction = 'left'
            self.set_direction()
        if pyxel.btn(pyxel.KEY_S):
            self.direction = 'front'
            self.set_direction()
        if pyxel.btn(pyxel.KEY_W):
            self.direction = 'back'
            self.set_direction()
        if pyxel.btn(pyxel.KEY_D):
            self.direction = 'right'
            self.set_direction()
        if pyxel.btn(pyxel.KEY_R):
            self.move()

    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.width, 32)


class App:
    def __init__(self):
        pyxel.init(SIZE, SIZE, fps=10)
        pyxel.load('my_resource.pyxres')

        self.personage = Personage()

        pyxel.move(self.update, self.draw)

    def update(self):
        self.personage.update()

    def draw(self):
        pyxel.cls(0)
        self.personage.draw()


App()
