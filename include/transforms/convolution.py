class Convolution:
    def convolve(self, image, kernel):
        temp = image.copy().load()
        load = image.load()
        W, H = image.size
        for i in range(W):
            for j in range(H):
                m = self.get_matrix_assoc(temp, (i, j), kernel.shape)
                load[i, j] = self.aux_convolve(m, kernel)
        return image

    def aux_convolve(self, matrix, kernel):
        r, g, b = 0, 0, 0
        x, y = kernel.shape
        for i in range(x):
            for j in range(y):
                pr, pg, pb = matrix[i][j]
                value_kernel = kernel[i, j]
                r += pr*value_kernel
                g += pg*value_kernel
                b += pb*value_kernel
        return int(r), int(g), int(b)

    def get_matrix_assoc(self, load, pos, shape):
        W, H = shape
        x, y = pos

        def f(l, x, y):
            try:
                return l[x, y]
            except Exception:
                return 0, 0, 0

        return [
            [f(load, i, j) for j in range(y - H//2, y + H//2 + 1)]
            for i in range(x - W//2, x + W//2 + 1)]

    def rgb2hex(self, r, g, b):
        return "0x{:02x}{:02x}{:02x}".format(r, g, b)


# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 x 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
