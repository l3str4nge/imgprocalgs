import argparse
import os
import itertools
from math import sqrt, pi, exp
from typing import List

from imgprocalgs.algorithms.utilities import create_empty_image

from imgprocalgs.algorithms.utilities import Image


class TiltShift:
    """ Tilt-shift technique """
    def __init__(self,
                 image_path: str,
                 destination_path: str,
                 min_blur: float,
                 max_blur: float,
                 sharpen_area_size: List=None):

        self.image_path = image_path
        self.destination_path = destination_path
        self.input_image = Image(self.image_path)
        self.pixels = self.input_image.pixels

        if not sharpen_area_size:
            image_height = self.input_image.get_size()[1]
            sharpen_area_size = [image_height // 3, image_height * 2 // 3]

        self.sharpen_min_h, self.sharpen_max_h = sharpen_area_size[0], sharpen_area_size[1]
        self.sharpen_size = self.sharpen_max_h - self.sharpen_min_h
        self.sharpen_center = self.sharpen_min_h + self.sharpen_size // 2

        self.filter_elements = []

        self.min_factor = 0.003
        self.max_factor = 0.003

        self.min_blur = min_blur
        self.max_blur = max_blur

    @classmethod
    def _make_filter_factor(cls, blur: float, index: int):
        return (1 / (sqrt(2 * pi) * blur)) * exp(-pow(index, 2)/(2 * pow(blur, 2)))

    def _make_blur(self, distance: int, sharp_area_size: int):
        """
        :param distance: distance between point and sharp area
        :param sharp_area_size: sharp area size height/width
        :return: blur value
        """
        return abs(self.min_blur + (self.max_blur - self.min_blur) * distance / sharp_area_size)

    def generate_filter_elements(self, blur: float, max_factor: int):
        self.filter_elements = list(itertools.takewhile(
            self.is_gt_min_factor,
            [self._make_filter_factor(blur, i) for i in range(max_factor)]
        ))

    def is_gt_min_factor(self, value: float):
        return value >= self.min_factor

    def process(self):
        width, height = self.input_image.get_size()
        output = create_empty_image(width, height)
        output_pixels = output.load()

        for x in range(width):
            for y in range(height):

                if self.sharpen_min_h < y < self.sharpen_max_h:
                    output_pixels[x, y] = self.pixels[x, y]
                    continue

                blur = self._make_blur(self.sharpen_center - y, self.sharpen_size)
                self.generate_filter_elements(blur, 7)
                red = self.process_horizontal(0, x, y, width - 1)
                green = self.process_horizontal(1, x, y, width - 1)
                blue = self.process_horizontal(2, x, y, width - 1)
                output_pixels[x, y] = (red, green, blue)

        for x in range(width):
            for y in range(height):
                if self.sharpen_min_h < y < self.sharpen_max_h:
                    output_pixels[x, y] = self.pixels[x, y]
                    continue

                blur = self._make_blur(self.sharpen_center - y, self.sharpen_size)
                self.generate_filter_elements(blur, 7)
                red = self.process_vertical(0, x, y, height - 1)
                green = self.process_vertical(1, x, y, height - 1)
                blue = self.process_vertical(2, x, y, height - 1)
                output_pixels[x, y] = (red, green, blue)

        output.save(os.path.join(self.destination_path, 'output_tilt_shift.jpg'))

    def process_horizontal(self, index, x, y, max_value):
        num = self.filter_elements[0] * self.pixels[x, y][index]
        denum = self.filter_elements[0]

        for i, value in enumerate(self.filter_elements[1:]):
            num += value * self.pixels[abs(x - i), y][index] + value * self.pixels[min(x + 1, max_value), y][index]
            denum += 2 * value

        return int(num / denum)

    def process_vertical(self, index, x, y, max_index):
        num = self.filter_elements[0] * self.pixels[x, y][index]
        denum = self.filter_elements[0]

        for i, value in enumerate(self.filter_elements[1:]):
            num += value * self.pixels[x, abs(y - i)][index] + value * self.pixels[x, min(y + i, max_index)][index]
            denum += 2 * value

        return int(num / denum)


def parse_args():
    parser = argparse.ArgumentParser(description='Tilt-shift effect')
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.", default='data/')
    parser.add_argument("--min_blur", type=float, help="Min blur factor")
    parser.add_argument("--max_blur", type=float, help="Max blur factor")
    parser.add_argument("--sharpen_area_size", type=int, nargs='+', default=[0, 0], help="Sharpen area size")
    return parser.parse_args()


def main():
    args = parse_args()
    TiltShift(
        args.src,
        args.dest,
        args.min_blur,
        args.max_blur,
        args.sharpen_area_size
    ).process()
