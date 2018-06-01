class LinearTransform:
    def linear_transform(self, image, func=lambda: (0, 0, 0),
                         before=lambda i, x: 0,
                         after=lambda i, x: 0):
        load = image.load()
        WIDTH, HEIGHT = image.size
        for x in range(WIDTH):
            before(image, x)
            for y in range(HEIGHT):
                load[x, y] = func(load[x, y])
            after(image, x)
        return image
