#!/usr/bin/env python
"""
    Arbalet - ARduino-BAsed LEd Table
    Video pixeliser

    Renders a high-def video on Arbalet by reducing dramatically its resolution
    in real time.

    Copyright 2015 Yoan Mollard - Arbalet project - http://github.com/arbalet-project
    License: GPL version 3 http://www.gnu.org/licenses/gpl.html
"""
import cv2
from os.path import isfile
from arbalet.application import Application
from arbalet.colors import mul


class Pixeliser(Application):
    def __init__(self, input, display_original=False, **kwargs):
        Application.__init__(self, **kwargs)
        self.video_reader = None
        self.display_original = display_original
        self.input = [input] if isinstance(input, (str, unicode)) else input

    def play_file(self, f):
        if isfile(f):
            self.video_reader = cv2.VideoCapture(f)
            self.rate = self.video_reader.get(cv2.cv.CV_CAP_PROP_FPS)
            print(self.rate, 'fps')

            while True:
                r, image = self.video_reader.read()
                if r:
                    pix_image = cv2.resize(image, (self.height, self.width))
                    pix_image = cv2.transpose(pix_image)
                    self.update_model(pix_image)
                    if self.display_original:
                        cv2.imshow(f, image)
                    cv2.waitKey(80)
                else:
                    break
        else:
            raise IOError('No such file or directory: \'{}\''.format(f))

    def update_model(self, image):
        with self.model:
            for h in range(self.height):
                for w in range(self.width):
                    pixel = mul(image[h][w], 1/255.)
                    pixel = [pixel[2], pixel[1], pixel[0]] # OpenCV pixels in BGR order
                    self.model.set_pixel(h, w, pixel)

    def run(self):
        for f in self.input:
            self.play_file(f)
