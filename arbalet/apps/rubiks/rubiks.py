from arbalet.core import Application, Rate
from .cube import Cube
from random import choice


class Rubiks(Application):
    def __init__(self):
        Application.__init__(self)
        assert self.width >= 12 and self.height >= 9
        self.cube = Cube()

    def run(self):
        rate = Rate(1)
        with self.model:
            self.cube.draw(self.model)
        rate.sleep()
        while True:
            move = choice((
                self.cube.U,
                self.cube.D,
                self.cube.R,
                self.cube.L,
                self.cube.F,
                self.cube.B,
                self.cube.Up,
                self.cube.Dp,
                self.cube.Rp,
                self.cube.Lp,
                self.cube.Fp,
                self.cube.Bp,
            ))
            move()
            with self.model:
                self.cube.draw(self.model)
            rate.sleep()
