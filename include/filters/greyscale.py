from include.filters.filter import Filter
from include.elements.imagen import Imagen
from include.transforms.linear import LinearTransform


class GreyScale(Filter, LinearTransform):
    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            type_ = message.type
            image = message.image
            result = self.apply(image, type_)
            return result
        except Exception as e:
            str(e)
            return Imagen()

    def apply(self, image, type):
        img = self.linear_transform({
            'avg': self.grey_avg,
            'r': self.grey_rgb(0),
            'g': self.grey_rgb(1),
            'b': self.grey_rgb(2)
            }[type], image)
        result = Imagen()
        result.setSuccessful(img)
        return result

    def grey_rgb(self, x):
        return lambda pixel: (pixel[x], pixel[x], pixel[x])

    def grey_avg(self, pixel):
        x = (pixel[0] + pixel[1] + pixel[2])//3
        return x, x, x
