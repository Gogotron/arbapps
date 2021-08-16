#!/usr/bin/env python
"""
    Arbalet - ARduino-BAsed LEd Table
    Langton's Ant

    Cellular automaton as described here:
    https://en.wikipedia.org/wiki/Langton%27s_ant

    Copyright 2021 Iñigo Diaz Iribarnegaray - http://github.com/Gogotron
    License: GPL version 3 http://www.gnu.org/licenses/gpl.html
"""
from arbalet.core import Application, Rate
from arbalet.colors import equal


class Langton(Application):
    def __init__(self):
        Application.__init__(self)
        self.x = self.width//2
        self.y = self.height//2
        self.dir = 0

    def run(self):
        self.model.set_all('black')

        rate = Rate(50)
        while True:
            self.step()
            rate.sleep()

    def step(self):
        if equal(self.model.get_pixel(self.y, self.x), 'white'):
            self.turn(1)
        else:
            self.turn(-1)
        self.flip_square()
        self.move_forward()

    def turn(self, turn_amount):
        self.dir += turn_amount
        self.dir %= 4

    def flip_square(self):
        if equal(self.model.get_pixel(self.y, self.x), 'white'):
            self.model.set_pixel(self.y, self.x, 'black')
        else:
            self.model.set_pixel(self.y, self.x, 'white')

    def move_forward(self):
        if self.dir == 0:
            self.x += 1
        elif self.dir == 1:
            self.y += 1
        elif self.dir == 2:
            self.x -= 1
        elif self.dir == 3:
            self.y -= 1
        self.x %= self.width
        self.y %= self.height
