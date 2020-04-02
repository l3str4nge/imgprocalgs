"""
Own implementation of resize algorithms - just for practice.
Testing with Pillow
"""


from PIL import Image


class NearestNeigbhour:
    """
    Nearest neighbour algorithm
    """

    def __init__(self, image_path: str, scale: float):
        self.image_path = image_path
        self.scale = scale
        self.image: Image = Image.open(self.image_path)
        self.pixels = self.image.load()
        self.new_image = None

    def process(self):
        xsrc, ysrc = self.image.size[1], self.image.size[0]
        print(xsrc, ysrc)
        xdest, ydest = int(xsrc * self.scale), int(ysrc * self.scale)
        ratio_x, ratio_y = xsrc / xdest, ysrc / ydest

        self.new_image = Image.new("RGB", (xdest, ydest), "#000000")
        new_image_pixels = self.new_image.load()
        for x in range(xdest - 1):
            for y in range(ydest - 1):
                try:
                    new_img_x, new_img_y = int(x * ratio_x), int(y * ratio_y)
                    new_image_pixels[x, y] = self.pixels[new_img_y, new_img_x]

                except Exception as e:
                    print("Catched")
        self.new_image.save("test.png")




