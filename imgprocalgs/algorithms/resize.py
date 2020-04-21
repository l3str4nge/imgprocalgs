"""
Own implementation of resize algorithms - just for practice.
Testing with Pillow
"""
import abc
import math
from PIL import Image as PillowImage
from imgprocalgs.algorithms.utilities import Image


class ImageResizer(metaclass=abc.ABCMeta):
    """ Base class of resizing algorithms """
    def __init__(self, image_path: str, scale: float):
        self.image = Image(image_path)
        self.scale = scale
        self.new_image = None

    @abc.abstractmethod
    def process(self, dest_path: str):
        pass

    def get_new_image(self, widht, height):
        return PillowImage.new("RGB", (widht, height), "#000000")


class NearestNeigbhour(ImageResizer):
    """
    Nearest neighbour algorithm
    """

    def process(self, dest_path: str):
        x_src, y_src = self.image.get_size()
        x_dest, y_dest = int(x_src * self.scale), int(y_src * self.scale)
        ratio_x, ratio_y = x_src / x_dest, y_src / y_dest

        self.new_image = PillowImage.new("RGB", (x_dest, y_dest), "#000000")
        new_image_pixels = self.new_image.load()
        for x in range(x_dest - 1):
            for y in range(y_dest - 1):
                new_img_x, new_img_y = int(x * ratio_x), int(y * ratio_y)
                new_image_pixels[x, y] = self.image.pixels[new_img_x, new_img_y]

        self.new_image.save(dest_path)


class Neighbour:
    """
    Nearest neighbour representation
    """
    def __init__(self, x, y, rgb):
        self.x = x
        self.y = y
        self.rgb = rgb

    @property
    def red(self):
        return self.rgb[0]

    @property
    def green(self):
        return self.rgb[1]

    @property
    def blue(self):
        return self.rgb[2]

    def __getitem__(self, item):
        return getattr(self, item)


class BilinearInterpolation(ImageResizer):
    """
    Bilinear interpolation algorithm
    """
    def __init__(self, image_path: str, scale: float):
        super().__init__(image_path, scale)
        self.neigh1 = None
        self.neigh2 = None
        self.neigh3 = None
        self.neigh4 = None

    def process(self, dest_path: str):
        x_src, y_src = self.image.get_size()
        x_dest, y_dest = int(x_src * self.scale), int(y_src * self.scale)
        ratio_x, ratio_y = x_src / x_dest, y_src / y_dest

        self.new_image = self.get_new_image(x_dest, y_dest)
        dest_pixels = self.new_image.load()

        for x in range(x_dest):
            for y in range(y_dest):
                x0 = float(x * ratio_x)
                y0 = float(y * ratio_y)

                x1, y1 = math.floor(x0), math.floor(y0)
                x2, y2 = math.ceil(x0), math.ceil(y0)

                if y2 == y_src: y2 = y0
                if x2 == x_src: x2 = x0

                dx, dy = x0 - x1, y0 - y1
                self.neigh1 = Neighbour(x1, y1, self.image.pixels[x1, y1])
                self.neigh2 = Neighbour(x2, y1, self.image.pixels[x2, y1])
                self.neigh3 = Neighbour(x1, y2, self.image.pixels[x1, y2])
                self.neigh4 = Neighbour(x2, y2, self.image.pixels[x2, y2])

                """ Bilinear Interpolation
                    source: https://en.wikipedia.org/wiki/Bilinear_interpolation
                 """
                red = (1 - dy) * (1 - dx) * self.neigh1.red + (1-dy) * dx * self.neigh2.red + (1 - dx) * dy * self.neigh3.red + dx * dy * self.neigh4.red
                green = (1 - dy) * (1 - dx) * self.neigh1.green + (1 - dy) * dx * self.neigh2.green + (1 - dx) * dy * self.neigh3.green + dx * dy * self.neigh4.green
                blue = (1 - dy) * (1 - dx) * self.neigh1.blue + (1 - dy) * dx * self.neigh2.blue + (1 - dx) * dy * self.neigh3.blue + dx * dy * self.neigh4.blue
                dest_pixels[x, y] = (int(red), int(green), int(blue))

        self.new_image.save(dest_path)


class BicubicInterpolation(ImageResizer):
    """
    Bicubic interpolation algorithm
    """
    A = -0.75

    def __init__(self, image_path: str, scale: float):
        super().__init__(image_path, scale)

        self.neighbours = []  # list for 4x4 neighbourhood
        self.x_coofs = None
        self.y_coofs = None

    def process(self, dest_path: str):
        """
        Implementing coefficients - inspired by openCV project
        const float A = -0.75f;
        """
        x_src, y_src = self.image.get_size()
        x_dest, y_dest = int(x_src * self.scale), int(y_src * self.scale)
        ratio_x, ratio_y = x_src / x_dest, y_src / y_dest

        self.new_image = self.get_new_image(x_dest, y_dest)
        dest_pixels = self.new_image.load()

        for x in range(x_dest):
            for y in range(y_dest):
                x0 = float(x * ratio_x)
                y0 = float(y * ratio_y)

                x1, y1 = math.floor(x0), math.floor(y0)
                x2, y2 = math.ceil(x0), math.ceil(y0)

                if y2 == y_src: y2 = y0
                if x2 == x_src: x2 = x0

                dx, dy = x0 - x1, y0 - y1
                self.x_coofs, self.y_coofs = self.get_coefficients(dx), self.get_coefficients(dy)

                # padding input image and select neighbours in 4x4 neighbourhood
                self.neighbours = []
                self.neighbours.append(Neighbour(x1, y1, self.image.pixels[x1, y1]))
                self.neighbours.append(Neighbour(x1, y1, self.image.pixels[x1, y1]))
                self.neighbours.append(Neighbour(x1, y1, self.image.pixels[x1, y1]))
                self.neighbours.append(Neighbour(x1, y1, self.image.pixels[x1, y1]))

                self.neighbours.append(Neighbour(x2, y1, self.image.pixels[x2, y1]))
                self.neighbours.append(Neighbour(x2, y1, self.image.pixels[x2, y1]))
                self.neighbours.append(Neighbour(x2, y1, self.image.pixels[x2, y1]))
                self.neighbours.append(Neighbour(x2, y1, self.image.pixels[x2, y1]))

                self.neighbours.append(Neighbour(x1, y2, self.image.pixels[x1, y2]))
                self.neighbours.append(Neighbour(x1, y2, self.image.pixels[x1, y2]))
                self.neighbours.append(Neighbour(x1, y2, self.image.pixels[x1, y2]))
                self.neighbours.append(Neighbour(x1, y2, self.image.pixels[x1, y2]))

                self.neighbours.append(Neighbour(x2, y2, self.image.pixels[x2, y2]))
                self.neighbours.append(Neighbour(x2, y2, self.image.pixels[x2, y2]))
                self.neighbours.append(Neighbour(x2, y2, self.image.pixels[x2, y2]))
                self.neighbours.append(Neighbour(x2, y2, self.image.pixels[x2, y2]))

                #  main interpolation
                red, green, blue = self._interpolate('red'), self._interpolate('green'), self._interpolate('blue')
                dest_pixels[x, y] = (int(red), int(green), int(blue))

        self.new_image.save(dest_path)

    def get_coefficients(self, x):
        first = ((self.A*(x + 1) - 5*self.A)*(x + 1) + 8*self.A)*(x + 1) - 4*self.A
        second = ((self.A + 2)*x - (self.A + 3))*x*x + 1
        third = ((self.A + 2)*(1 - x) - (self.A + 3))*(1 - x)*(1 - x) + 1
        fourth = 1.0 - first - second - third
        return first, second, third, fourth

    def _interpolate(self, key):
        a, b, c, d = self.x_coofs
        e, f, g, h = self.y_coofs

        xr1 = a * self.neighbours[0][key] + b * self.neighbours[4][key] + c * self.neighbours[8][key] + d * self.neighbours[12][key]
        xr2 = a * self.neighbours[1][key] + b * self.neighbours[5][key] + c * self.neighbours[9][key] + d * self.neighbours[13][key]
        xr3 = a * self.neighbours[2][key] + b * self.neighbours[6][key] + c * self.neighbours[10][key] + d * self.neighbours[14][key]
        xr4 = a * self.neighbours[3][key] + b * self.neighbours[7][key] + c * self.neighbours[11][key] + d * self.neighbours[15][key]
        return e * xr1 + f * xr2 + g * xr3 + h * xr4
