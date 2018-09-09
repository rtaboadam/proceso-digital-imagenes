from include.elements.imagen import Imagen
from include.filters.filter import Filter
from include.transforms.linear import LinearTransform


class Sepia(Filter, LinearTransform):
    def __call__(self, message):
        self.check(message.name)
        print(self.__str__())
        result = self.apply(message.image)
        return result

    def sepia(self, pixel):
        