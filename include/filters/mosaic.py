from include.filters.filter import Filter
from include.transforms.cuadratic import CuadraticTransform
from include.elements.imagen import Imagen


class Mosaic(Filter, CuadraticTransform):
    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            result = self.apply(message.image, message.square)
            return result
        except Exception as e:
            print(e)
            return Imagen()

    def apply(self, image, square):
        im = self.cuadratic_transform(square, self.average, image)
        result = Imagen()
        result.setSuccessful(im)
        return result

    def average(self, load, rangeX, rangeY):
        x, dx = rangeX
        y, dy = rangeY
        total_pixeles = (dx - x) * (dy - y)
        r, g, b = 0, 0, 0
        for i in range(x, dx):
            for j in range(y, dy):
                try:
                    pr, pg, pb = load[i, j]
                    r += pr
                    g += pg
                    b += pb
                except Exception:
                    continue
        r = r // total_pixeles
        g = g // total_pixeles
        b = b // total_pixeles
        for i in range(x, dx):
            for j in range(y, dy):
                try:
                    load[i, j] = r, g, b
                except Exception:
                    continue
