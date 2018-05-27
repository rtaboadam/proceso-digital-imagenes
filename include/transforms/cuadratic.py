class CuadraticTransform:
    def cuadratic_transform(self, square, func, image):
        load = image.load()
        W, H = image.size
        dx, dy = square
        for x in range(0, W, dx):
            for y in range(0, H, dy):
                func(load, (x, x + dx), (y, y + dy))
        return image
