#!/usr/bin/env python
"""
    Arbalet - ARduino-BAsed LEd Table
    Pong game

    Copyright 2021 Iñigo Diaz Iribarnegaray - http://github.com/Gogotron
    License: GPL version 3 http://www.gnu.org/licenses/gpl.html
"""
from arbalet.core import Application, Rate


class Pong(Application):
    def __init__(self):
        Application.__init__(self)

    def run(self):
        self.bpos = [0, 0]
        self.bspeed = [1, 1]
        self.ppos = 0
        rate = Rate(5)
        while True:
            self.move_paddle()
            self.move_ball()
            with self.model:
                self.model.set_all('black')
                self.draw_paddle()
                self.draw_ball()
            rate.sleep()

    def move_ball(self):
        self.bpos[0] += self.bspeed[0]
        if not 0 <= self.bpos[0] < self.width:
            self.bspeed[0] *= -1
            self.bpos[0] = self.bound(self.bpos[0], 0, self.width-1)

        self.bpos[1] += self.bspeed[1]
        if not 0 <= self.bpos[1]:
            self.bspeed[1] *= -1
            self.bpos[1] = max(0, self.bpos[1])
        if self.bpos[1] >= self.height:
            print('game over')
            self.bpos = [0, 0]
        elif self.bpos[1] >= self.height-2:
            if self.ppos <= self.bpos[0] < self.ppos+3:
                self.bspeed[1] *= -1
                self.bpos[1] = self.height-2

    def draw_ball(self):
        self.model.set_pixel(int(self.bpos[1]), int(self.bpos[0]), 'white')

    def move_paddle(self):
        self.process_events()
        if self.command['left']:
            self.ppos -= 1
        if self.command['right']:
            self.ppos += 1
        self.ppos = self.bound(self.ppos, 0, self.width-3)

    def draw_paddle(self):
        for i in range(3):
            self.model.set_pixel(14, int(self.ppos)+i, 'cyan')

    def bound(self, x, m, M):
        return max(m, min(x, M))
