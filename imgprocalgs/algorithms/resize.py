"""
Own implementation of resize algorithms - just for practice.
Testing with Pillow
"""
import abc
import math

from PIL import Image


class ImageLoader:
    """
    CLass responsible for image loading
    """
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image: Image = Image.open(self.image_path)
        self.pixels = self.image.load()

    def get_size(self):
        """
        :return: x, y in pixels
        """
        return self.image.size[0], self.image.size[1]


class ImageResizer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process(self):
        pass

    def get_new_image(self, widht, height):
        return Image.new("RGB", (widht, height), "#000000")


class NearestNeigbhour(ImageResizer):
    """
    Nearest neighbour algorithm
    """

    def __init__(self, image_path: str, scale: float):
        self.image_loader: ImageLoader = ImageLoader(image_path)
        self.image_path = image_path
        self.scale = scale
        self.new_image = None

    def process(self):
        x_src, y_src = self.image_loader.image.size[0], self.image_loader.image.size[1]
        x_dest, y_dest = int(x_src * self.scale), int(y_src * self.scale)
        ratio_x, ratio_y = x_src / x_dest, y_src / y_dest

        self.new_image = Image.new("RGB", (x_dest, y_dest), "#000000")
        new_image_pixels = self.new_image.load()
        for x in range(x_dest - 1):
            for y in range(y_dest - 1):
                new_img_x, new_img_y = int(x * ratio_x), int(y * ratio_y)
                new_image_pixels[x, y] = self.image_loader.pixels[new_img_x, new_img_y]

        self.new_image.save("test_nearestneigh.jpg")


class BilinearInterpolation(ImageResizer):
    """
    Bilinear interpolation algorithm
    """
    def __init__(self, image_path: str, scale: float):
        super().__init__()
        self.image_loader: ImageLoader = ImageLoader(image_path)
        self.image_path = image_path
        self.pixels = self.image_loader.pixels
        self.scale = scale
        self.new_image = None

        self.neigh1 = None
        self.neigh2 = None
        self.neigh3 = None
        self.neigh4 = None

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

    def process(self):
        x_src, y_src = self.image_loader.get_size()
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
                # TODO: something is bad with x - y combination below in interpolation calc
                self.neigh1 = self.Neighbour(x1, y1, self.pixels[x1, y1])
                self.neigh2 = self.Neighbour(x2, y2, self.pixels[x2, y2])
                self.neigh3 = self.Neighbour(x1, y2, self.pixels[x1, y2])
                self.neigh4 = self.Neighbour(x2, y1, self.pixels[x2, y1])

                """ Bilinear Interpolation
                    source: https://en.wikipedia.org/wiki/Bilinear_interpolation
                 """
                red = (1 - dy) * (1 - dx) * self.neigh1.red + dx * self.neigh2.red + (1 - dx) * self.neigh3.red + dx * self.neigh3.red
                green = (1 - dy) * (1 - dx) * self.neigh1.green + dx * self.neigh2.green + (1 - dx) * self.neigh3.green + dx * self.neigh3.green
                blue = (1 - dy) * (1 - dx) * self.neigh1.blue + dx * self.neigh2.blue + (1 - dx) * self.neigh3.blue + dx * self.neigh3.blue
                dest_pixels[x, y] = (int(red), int(green), int(blue))

        self.new_image.save("test_bilinear.jpg")
