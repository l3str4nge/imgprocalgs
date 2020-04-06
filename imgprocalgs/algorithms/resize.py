"""
Own implementation of resize algorithms - just for practice.
Testing with Pillow
"""
import abc

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

        self.new_image.save("test.png")


class BilinearInterpolation(ImageResizer):
    """
    Bilinear interpolation algorithm
    """
    def __init__(self, image_path: str, scale: float):
        super().__init__()
        self.image_loader: ImageLoader = ImageLoader(image_path)
        self.image_path = image_path
        self.scale = scale
        self.new_image = None

    def process(self):
        x_src, y_src = self.image_loader.get_size()
        x_dest, y_dest = int(x_src * self.scale), int(y_src * self.scale)
        ratio_x, ratio_y = x_src / x_dest, y_src / y_dest

        self.new_image = self.get_new_image(x_dest, y_dest)
        dest_pixels = self.new_image.load()

        for x in range(x_dest - 1):
            for y in range(y_dest - 1):
                neigh_1 = self.image_loader.pixels[x-1, y]
                neigh_2 = self.image_loader.pixels[x + 1, y]
                neigh_3 = self.image_loader.pixels[x, y + 1]
                neigh_4 = self.image_loader.pixels[x, y - 1]

                # TODO: how to handle edges?
                print(neigh_1, neigh_2, neigh_3, neigh_4)

        self.new_image.save("test.png")









