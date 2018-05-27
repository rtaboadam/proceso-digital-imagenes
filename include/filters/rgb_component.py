from include.filters.filter import Filter
from include.elements.imagen import Imagen
from include.transforms.linear import LinearTransform


class RGBComponent(Filter, LinearTransform):
    def __init__(self): pass

    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            component = message.component
            image = message.image
            result = self.apply(image, component)
            return result
        except Exception as e:
            print(e)
            return Imagen()

    def apply(self, image, component):
        im = self.linear_transform({
                    'r': lambda pixel: (pixel[0], 0, 0),
                    'g': lambda pixel: (0, pixel[1], 0),
                    'b': lambda pixel: (0, 0, pixel[2])
                    }[component], image)
        result = Imagen()
        result.setSuccessful(im)
        return result
