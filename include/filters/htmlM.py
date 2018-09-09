import os
import bs4
import shutil
from include.elements.imagen import Imagen
from include.filters.filter import Filter
from include.transforms.linear import LinearTransform
TEMPLATE = 'template.html'
ROOT = os.getcwd()


class OneLetter(Filter, LinearTransform):
    def __call__(self, message):
        try:
            self.check(message.name)
            print(self.__str__())
            templatePath = os.path.join(ROOT, 'include', 'templates', TEMPLATE)
            outputPath = os.path.join(ROOT, 'output',
                                      'eme.html' if not hasattr(message, 'outputName')
                                      else message.outputName)
            shutil.copyfile(templatePath, outputPath)
            return self.apply(message.image, outputPath, message.letter, message.inGray)
        except Exception as e:
            print(e)
            return Imagen()

    def apply(self, image, canvas, letter, isGray):
        with open(canvas) as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt, "html.parser")
        load = image.load() if not isGray else image.convert("L").load()
        W, H = image.size
        for y in range(H):
            row = soup.new_tag("p")
            for x in range(W):
                color = str((load[x, y], load[x, y], load[x, y])) if isGray else str(load[x, y])
                new_span = soup.new_tag("span",
                                        style="color:rgb%s" % color)
                new_span.string = letter
                row.append(new_span)
            soup.body.append(row)
        with open(canvas, "w") as outf:
            outf.write(str(soup))

        result = Imagen()
        result.show = lambda: print("exito")
        result.setSuccessful(True)
        return result
