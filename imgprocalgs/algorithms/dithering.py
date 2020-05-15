""" Module including dithering algorithms """

import os

from PIL import Image as PillowImage
from imgprocalgs.algorithms.utilities import Image, get_greyscale


class FloydSteinberg:
    """
    Floyd Stainberg algorithm using for reducng grayscale image to black and white.
    Source: https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering
    """

    BLACK = "#000000"
    WHITE = "#FFFFFF"

    def __init__(self, image_path: str, destination_path: str, factor: int):
        self.min_factor = 0
        self.max_factor = int(get_greyscale(255, 255, 255))  # max greyscale vlaue for #FFFFFF

        if not self.min_factor < factor < self.max_factor:
            raise ValueError(f"Factor value should be from 0 to {self.max_factor}")

        self.image = Image(image_path)
        self.factor = factor

        self.destination_path = destination_path

        #  raw error table and output image
        self.width, self.height = self.image.get_size()
        self.greyscale_image = self.image2greyscale()
        # error size + 1 than input image because of lack of if statements
        self.error_table = [[0 for _ in range(self.height + 2)] for __ in range(self.width + 2)]

        self.output_image = PillowImage.new("RGB", (self.width, self.height), self.WHITE)
        self.output_pixels = self.output_image.load()

    def image2greyscale(self):
        greyscale_image = PillowImage.new("RGB", (self.width, self.height), self.WHITE)
        pixels = greyscale_image.load()

        for x in range(self.width):
            for y in range(self.height):
                grey_value = int(get_greyscale(*self.image.pixels[x, y]))
                pixels[x, y] = (grey_value, grey_value, grey_value)

        greyscale_image.save(os.path.join(self.destination_path, "output_greyscale.jpg"))
        return greyscale_image

    def process(self):
        input_pixels = self.greyscale_image.load()

        for x in range(self.width):
            for y in range(self.height):
                if self.factor > input_pixels[x, y][0] + self.error_table[x][y]:
                    self.output_pixels[x, y] = (0, 0, 0)
                    current_error = input_pixels[x, y][0] + self.error_table[x][y]
                else:
                    self.output_pixels[x, y] = (255, 255, 255)
                    current_error = input_pixels[x, y][0] + self.error_table[x][y] - 255

                # error propagation
                self._propagate_error(x, y, current_error)

        self.output_image.save(os.path.join(self.destination_path, "output_floyd_steinberg.jpg"))

    def _propagate_error(self, x, y, current_error):
        self.error_table[x + 1][y] += + 7 / 16 * current_error
        self.error_table[x + 1][y + 1] += 3 / 16 * current_error
        self.error_table[x][y + 1] += 5 / 16 * current_error
        self.error_table[x - 1][y + 1] += 1 / 16 * current_error


class JarvisJudiceNinke(FloydSteinberg):
    """
    Floyd staingerg extension
    https://en.wikipedia.org/wiki/Dither
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_table = [[0 for _ in range(self.height + 3)] for __ in range(self.width + 3)]

    def _propagate_error(self, x, y, current_error):
        self.error_table[x + 1][y] += 7 / 48 * current_error
        self.error_table[x + 2][y] += 5 / 48 * current_error

        self.error_table[x][y + 1] += 7 / 48 * current_error
        self.error_table[x + 1][y + 1] += 5 / 48 * current_error
        self.error_table[x + 2][y + 1] += 3 / 48 * current_error
        self.error_table[x - 1][y + 1] += 5 / 48 * current_error
        self.error_table[x - 2][y + 1] += 3 / 48 * current_error

        self.error_table[x][y + 2] += 5 / 48 * current_error
        self.error_table[x + 1][y + 2] += 3 / 48 * current_error
        self.error_table[x + 2][y + 2] += 1 / 48 * current_error
        self.error_table[x - 1][y + 2] += 3 / 48 * current_error
        self.error_table[x - 2][y + 2] += 1 / 48 * current_error
