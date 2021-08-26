#!/usr/bin/env python
"""
    Arbalet - ARduino-BAsed LEd Table
    Pong game

    Copyright 2021 Iñigo Diaz Iribarnegaray - http://github.com/Gogotron
    License: GPL version 3 http://www.gnu.org/licenses/gpl.html
"""
from arbalet.core import Application, Rate
from random import randrange
from math import ceil


class Pong(Application):
    BACKGROUND_COLOR = 'black'
    BALL_COLOR = 'lightgreen'
    PADDLE_COLOR = 'cyan'

    def __init__(self, parser):
        Application.__init__(self, parser)
        self.rate = 8
        self.rate_increase = self.args.speed
        try:
            self.paddle_size = self.bound(self.args.size, 1, self.width)
        except TypeError:
            self.paddle_size = ceil(self.width/4)

    def run(self):
        self.score = 0
        rate = Rate(self.rate)
        self.place_paddle()
        self.place_ball()
        while True:
            rate.sleep_dur = 1/self.rate

            self.move_paddle()
            ball_passed = self.move_ball()
            with self.model:
                self.model.set_all('black')
                self.draw_paddle()
                if not ball_passed:
                    self.draw_ball()
            rate.sleep()
            if ball_passed:
                break
        self.game_over()

    def place_ball(self):
        self.bpos = [randrange(self.width), 0]
        self.bspeed = [(-1)**randrange(2), 1]

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
            return True
        elif self.bpos[1] >= self.height-2:
            if self.ppos <= self.bpos[0] < self.ppos+self.paddle_size:
                self.bspeed[1] *= -1
                self.bpos[1] = self.height-2
                self.score += 1
                self.rate += self.rate_increase

    def draw_ball(self):
        self.model.set_pixel(self.bpos[1], self.bpos[0], self.BALL_COLOR)

    def place_paddle(self):
        self.ppos = (self.width-self.paddle_size) // 2

    def move_paddle(self):
        self.process_events()
        if self.command['left']:
            self.ppos -= 1
        if self.command['right']:
            self.ppos += 1
        self.ppos = self.bound(self.ppos, 0, self.width-self.paddle_size)

    def draw_paddle(self):
        for i in range(self.paddle_size):
            self.model.set_pixel(self.height-1, self.ppos+i, self.PADDLE_COLOR)

    def bound(self, x, m, M):
        return max(m, min(x, M))

    def game_over(self):
        self.model.flash()
        self.model.write(f"GAME OVER! Score: {self.score}", 'deeppink')
