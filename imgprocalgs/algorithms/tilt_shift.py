from PIL import Image as PillowImage
import itertools
from math import sqrt, pi, e

from imgprocalgs.algorithms.utilities import Image


class TiltShift:
    def __init__(self, image_path: str, destination_path: str, min_blur: float, max_blur: float):
        self.image_path = image_path
        self.destination_path = destination_path
        self.input_image = Image(self.image_path)
        self.filter_size = 0

        self.min_factor = 0.003
        self.max_factor = 0.003

        self.min_blur = min_blur
        self.max_blur = max_blur

    @classmethod
    def _make_filter_factor(cls, blur: float, index: int):
        return (1 / sqrt(2 * pi * blur)) * pow(e, -(pow(index, 2)/2 * pow(blur, 2)))

    def _make_blur(self, distance: int, sharp_area_size: int):
        """
        :param distance: distance between point and sharp area
        :param sharp_area_size: sharp area size height/width
        :return: blur value
        """
        return self.min_blur + (self.max_blur - self.min_blur) * distance / sharp_area_size
