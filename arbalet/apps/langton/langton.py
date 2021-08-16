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
from arbalet.colors import equal, name_to_rgb


class Langton(Application):
    def __init__(self, parser):
        Application.__init__(self, parser)
        self.x = self.width//2
        self.y = self.height//2
        self.dir = 0

        self.rate = self.args.rate
        self.fade_dur = min(1/self.rate, self.args.fade_dur)

    def run(self):
        self.model.set_all('black')

        rate = Rate(self.rate)
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
            current, next = 'white', 'black'
        else:
            current, next = 'black', 'white'
        self.fade(self.y, self.x, current, next)

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

    def fade(self, y, x, start, end):
        if isinstance(start, str):
            start = name_to_rgb(start)
        if isinstance(end, str):
            end = name_to_rgb(end)
        steps = 300
        duration = self.fade_dur
        if duration != 0:
            rate = Rate(steps/duration)
            for i in range(1, steps+1):
                col = (start*(steps-i) + end*i)/steps
                self.model.set_pixel(y, x, col)
                rate.sleep()
        else:
            self.model.set_pixel(y, x, end)
