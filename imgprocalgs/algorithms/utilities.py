""" Module including utilities for main algorithms"""
from PIL import Image as PillowImage


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
