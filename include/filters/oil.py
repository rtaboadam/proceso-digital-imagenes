from include.filters.filter import Filter
from include.elements.imagen import Imagen
from include.transforms.convolution import Convolution

import numpy as np


class Oil(Filter, Convolution):
    kernel = np.array([[0, 1, 1, 1, 0],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [0, 1, 1, 1, 0]])

    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            return self.apply(message.image)
        except Exception as e:
            print(e)
            return Imagen()

    def apply(self, image):
        im = self.convolve(self.aux_oil, image, self.kernel)
        result = Imagen()
        result.setSuccessful(im)
        return result

    def aux_oil(self, matrix, kernel):
        def intensity(r, g, b):
            return (r + g + b) // 3

        intensityCurr = {x: 0 for x in range(256)}
        averageR = {x: 0 for x in range(256)}
        averageG = {x: 0 for x in range(256)}
        averageB = {x: 0 for x in range(256)}
        x, y = kernel.shape
        for i in range(x):
            for j in range(y):
                r, g, b = matrix[i][j]
                current = intensity(r, g, b)
                intensityCurr[current] += 1
                averageR[current] += r
                averageG[current] += g
                averageB[current] += b

        maxIntensity = max(intensityCurr.keys(),
                           key=(lambda key: intensityCurr[key]))
        maxIntensityValue = intensityCurr[maxIntensity]
        r = averageR[maxIntensity] // maxIntensityValue
        g = averageG[maxIntensity] // maxIntensityValue
        b = averageB[maxIntensity] // maxIntensityValue
        return r, g, b
