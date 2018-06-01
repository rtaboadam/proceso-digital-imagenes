import os
import bs4
import shutil
from include.elements.imagen import Imagen
from include.filters.filter import Filter
from include.transforms.linear import LinearTransform
TEMPLATE = 'template.html'
ROOT = os.getcwd()
DOMINOS = [(x, y) for x in range(10) for y in range(10) if x >= y]


class Dominoes(Filter, LinearTransform):
    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            templatePath = os.path.join(ROOT, 'include', 'templates', TEMPLATE)
            outputPath = os.path.join(ROOT, 'output', 'dominoes.html')
            shutil.copyfile(templatePath, outputPath)
            font = message.font
            self.apply(message.image, outputPath, font)
        except Exception as e:
            raise e

    def apply(self, image, canvas, font):
        with open(canvas) as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt, "html.parser")
        print(soup)
        load = image.convert("L").load()
        W, H = image.size
        for x in range(W):
            row = ""
            for y in range(H):
                row += self.getDominoForPixel(load[x, y])
            new_p = soup.new_tag("p", style="font-family: %s" % font)
            new_p.string = str(row)
            soup.body.append(new_p)
        with open(canvas, "w") as outf:
            outf.write(str(soup.prettify()))

        result = Imagen()
        result.show = lambda: print("exito")
        result.setSuccessful(canvas)
        return result

    def getDominoForPixel(self, pixel):
        x, y = DOMINOS[pixel//len(DOMINOS)]
        return str(x) + str(y)
