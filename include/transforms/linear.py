class LinearTransform:
    def linear_transform(self, func, image):
        load = image.load()
        WIDTH = image.size[0]
        HEIGHT = image.size[1]
        for x in range(WIDTH):
            for y in range(HEIGHT):
                load[x, y] = func(load[x, y])
        return image
