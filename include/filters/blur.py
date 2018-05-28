from include.filters.filter import Filter
from include.elements.imagen import Imagen
from include.transforms.convolution import Convolution

import numpy as np


class Blur(Filter, Convolution):
    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            return self.apply(message.image)
        except Exception as e:
            str(e)
            return Imagen()

    def apply(self, image):
        im = self.convolve(self.aux_convolve, image, self.kernel)
        result = Imagen()
        result.setSuccessful(im)
        return result


class EdgeDetection(Blur):
    kernel = np.array([[1, 0, -1],
                       [0, 0, 0],
                       [-1, 0, 1]])


class BoxBlur(Blur):
    kernel = (1/9)*np.array([[1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]])


class MotionBlur(Blur):
    kernel = (1/9)*np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1]])


class GaussianBlurr3x3(Blur):
    kernel = (1/16)*np.array([[1, 2, 1],
                              [2, 4, 2],
                              [1, 2, 1]])


class GaussianBlurr5x5(Blur):
    kernel = (1/256)*np.array([[1, 4, 6, 4, 1],
                               [4, 16, 24, 16, 4],
                               [6, 24, 36, 24, 6],
                               [4, 16, 24, 16, 4],
                               [1, 4, 6, 4, 1]])


class Sharpen(Blur):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
