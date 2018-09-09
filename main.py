from PIL import Image
from include.chainLink import ChainLink
from include.elements.message import Message
from include.filters.rgb_component import RGBComponent
from include.filters.greyscale import GreyScale
from include.filters.mosaic import Mosaic
from include.filters.blur import BoxBlur
from include.filters.blur import MotionBlur
from include.filters.blur import EdgeDetection
from include.filters.blur import GaussianBlurr3x3
from include.filters.blur import GaussianBlurr5x5
from include.filters.blur import Sharpen
from include.filters.oil import Oil
from include.filters.dominoes import Dominoes
from include.filters.htmlM import OneLetter


def main():
    solutions = []
    ChainLink(solutions, RGBComponent())
    ChainLink(solutions, GreyScale())
    ChainLink(solutions, Mosaic())
    ChainLink(solutions, BoxBlur())
    ChainLink(solutions, MotionBlur())
    ChainLink(solutions, EdgeDetection())
    ChainLink(solutions, GaussianBlurr3x3())
    ChainLink(solutions, GaussianBlurr5x5())
    ChainLink(solutions, Sharpen())
    ChainLink(solutions, Oil())
    ChainLink(solutions, Dominoes())
    ChainLink(solutions, OneLetter())

    message = Message()
    message.image = Image.open("var/emilia.jpg").copy()
    # message.name = "RGBComponent"
    # message.name = "Dominoes"
    message.name = "OneLetter"
    message.letter = "M"
    message.inGray = True
    # message.outputName = "e.html"
    message.type = "b"
    message.component = "r"
    message.square = 20, 10
    message.font = "BlackVegas"
    return solutions[0](message).succeeded


if __name__ == '__main__':
    imagen = main()
    if imagen.__class__ == Image.Image:
        imagen.show()
