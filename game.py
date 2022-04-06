import pyxel
SIZE = 200
class App:
    def __init__(self):
        pyxel.init(SIZE, SIZE, fps=10   )
        pyxel.load('my_resource.pyxres')
        
        self.x:int = 50
        self.y:int = 50
        self.u:int = 0
        self.v:int = 0
        self.width:int=16
        self.running:bool = False
        
        self.direction = 'right'
        
        pyxel.run(self.update, self.draw)
        
        
    def set_direction(self):
        if self.direction == "left":
            self.u = 0
        if self.direction == "right":
            self.u = 16
        if self.direction == "front":
            self.u = 32
        if self.direction == "back":
            self.u = 48

    def run(self):
        start_u = 14
        end_u = 112
        v = 32
        self.width = 14
        if self.running == False:
            self.v= v
            self.u = start_u
            self.running = True
        elif self.u >= end_u:
            self.u = start_u
        else:
            if self.direction == 'right':
                # self.x+=2
                self.u += 14
            else:
                self.x -= 1
                self.u -= 14
            
        
                
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
            self.run()


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y,1,self.u,self.v,self.width,32)
        # pyxel.rect(self.x, self.y, 20, 20, 11)

App()