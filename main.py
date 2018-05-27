from PIL import Image
from include.chainLink import ChainLink
from include.elements.message import Message
from include.filters.rgb_component import RGBComponent
from include.filters.greyscale import GreyScale
from include.filters.mosaic import Mosaic


def main():
    solutions = []
    ChainLink(solutions, RGBComponent())
    ChainLink(solutions, GreyScale())
    ChainLink(solutions, Mosaic())

    message = Message()
    message.image = Image.open("var/emilia.jpg").copy()
    message.name = "Mosaic"
    message.type = "b"
    message.component = "r"
    message.square = 20, 10
    solutions[0](message).succeeded.show()


if __name__ == '__main__':
    main()
