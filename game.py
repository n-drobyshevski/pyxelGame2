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
        self.frames_info -- information corresponding a width, height of skin frame
                              and to the length of the row with frames of moving animation
        """
        self.x: int = 50
        self.y: int = 50
        self.u: int = 0
        self.v: int = 0
        self.width: int = 13
        self.height: int = 27
        self.direction = 'down'
        self.moving: bool = False

        self.frames_info = {'horizontal': {'end_u': 112, 'width': 14, 'width_moving': 14},
                              'vertical': {'end_u': 185, 'width': 12}}

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

    def move(self):
        """
        personage move implementation
        variables:
            start_u, end_u - horizontal limits of line with move animation frames in Editor
            width - width of personage while moving horizontally is diffrent to idling
        """
        start_u = 14
        end_u = 112
        if self.direction == 'right' or self.direction == 'left':
            self.width = self.frames_info['horizontal']['width_moving']
            end_u = self.frames_info['horizontal']['end_u']
        elif self.direction == 'up' or self.direction == 'down':
            end_u = self.frames_info['vertical']['end_u']

        # if not currently moving set first frame of animation as a current
        if self.moving == False:
            self.u = start_u
            self.moving = True
        # if current frame is last in animation the next one will return to first on the line
        elif self.u >= end_u:
            self.u = start_u
        # move personage forward, change skin
        else:
            # self.x+=2
            self.u += self.width # one pixel offset between frames

    def update(self):
        # self.x = (self.x + 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_A):
            self.direction = 'left'
        elif pyxel.btn(pyxel.KEY_S):
            self.direction = 'front'
            self.set_direction()
        elif pyxel.btn(pyxel.KEY_W):
            self.direction = 'back'
            self.set_direction()
        elif pyxel.btn(pyxel.KEY_D):
            self.direction = 'right'

        self.set_direction()
        # press r to run animation in selected direction !only development thing!
        if pyxel.btn(pyxel.KEY_R):
            self.moving = True
            self.move()
        if pyxel.btnr(pyxel.KEY_R):
            self.moving = False

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
