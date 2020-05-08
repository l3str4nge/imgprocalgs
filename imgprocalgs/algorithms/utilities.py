""" Module including utilities for main algorithms"""
from PIL import Image as PillowImage
from collections import namedtuple

ImageData = namedtuple("ImgData", 'header image')
HSV = namedtuple("HSV", 'h s v')
RGB = namedtuple("RGB", 'r g b')


class Image:
    """ Wrapper for Image class for easier usage"""
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image: PillowImage = PillowImage.open(self.image_path)
        self.pixels = self.image.load()

    def get_size(self):
        """
        :return: x, y in pixels
        """
        return self.image.size[0], self.image.size[1]


def create_empty_image(width: int, height: int) -> PillowImage:
    return PillowImage.new("RGB", (width, height), "#000000")


def get_greyscale(red: int, green: int, blue: int) -> float:
    return 0.2126 * red + 0.587 * green + 0.114 * blue


def rgb_to_hsv(red: int, green: int, blue: int) -> namedtuple:
    _red = red / 255
    _green = green / 255
    _blue = blue / 255

    c_max = max(_red, _green, _blue)
    c_min = min(_red, _green, _blue)

    delta = c_max - c_min

    if delta > 0:
        if c_max == _red:
            h = 60 * (((_green - _blue) / delta) % 6)
        elif c_max == _green:
            h = 60 * (((_blue - _red) / delta) + 2)
        elif c_max == _blue:
            h = 60 * (((_red - _green) / delta) + 4)
        else:
            raise ValueError(f"c_max ({c_max} is not equal {_red}/{_green}/{_blue})")
    else:
        h = 0

    s = 0 if c_max == 0 else delta/c_max

    return HSV(h, s, c_max)


def hsv_to_rgb(h: float, s: float, v: float) -> namedtuple:
    c = v * s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        red, green, blue = c, x, 0
    elif 60 <= h < 120:
        red, green, blue = x, c, 0
    elif 120 <= h < 180:
        red, green, blue = 0, c, x
    elif 180 <= h < 240:
        red, green, blue = 0, x, c
    elif 240 <= h < 300:
        red, green, blue = x, 0, c
    elif 300 <= h < 360:
        red, green, blue = c, 0, x
    else:
        raise ValueError(f"h value: {h} is out of range (0, 360)")

    return RGB(
        int((red + m) * 255),
        int((green + m) * 255),
        int((blue + m) * 255)
    )
