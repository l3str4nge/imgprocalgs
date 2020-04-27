import os
import itertools
from math import sqrt, pi, e
from imgprocalgs.algorithms.utilities import create_empty_image

from imgprocalgs.algorithms.utilities import Image


class TiltShift:
    def __init__(self, image_path: str, destination_path: str, min_blur: float, max_blur: float):
        self.image_path = image_path
        self.destination_path = destination_path
        self.input_image = Image(self.image_path)
        self.pixels = self.input_image.pixels
        self.filter_elements = []

        self.min_factor = 0.003
        self.max_factor = 0.003

        self.min_blur = min_blur
        self.max_blur = max_blur

    @classmethod
    def _make_filter_factor(cls, blur: float, index: int):
        return (1 / (sqrt(2 * pi) * blur)) * pow(e, -(pow(index, 2)/2 * pow(blur, 2)))

    def _make_blur(self, distance: int, sharp_area_size: int):
        """
        :param distance: distance between point and sharp area
        :param sharp_area_size: sharp area size height/width
        :return: blur value
        """
        return self.min_blur + (self.max_blur - self.min_blur) * distance / sharp_area_size

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
                blur = self._make_blur(1, 1)  # TODO: add logic, fixed value now
                self.generate_filter_elements(blur, 7)
                red = self.process_component(0, x, y)
                green = self.process_component(1, x, y)
                blue = self.process_component(2, x, y)
                output_pixels[x, y] = (red, green, blue)

        output.save(os.path.join(self.destination_path, 'output_tilt_shift.jpg'))

    def process_component(self, index, x, y):
        numerator = self.filter_elements[0] * self.pixels[x, y][index]
        denumerator = self.filter_elements[0]
        print(self.filter_elements)
        for i, value in enumerate(self.filter_elements[1:]):
            numerator += value * self.pixels[x - i, y][index] + value * self.pixels[x + 1, y][index]
            denumerator += 2 * value

        return int(numerator / denumerator)
