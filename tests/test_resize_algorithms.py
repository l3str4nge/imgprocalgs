from unittest import TestCase
from PIL import Image
from imgprocalgs.algorithms import resize
import os


class BaseTestResize(TestCase):
    OUTPUT_FILE = ""

    def tearDown(self):
        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)

    def open_image(self):
        return Image.open(self.OUTPUT_FILE)


class TestNearestNeighbour(BaseTestResize):
    def test_resize(self):
        self.OUTPUT_FILE = 'tests/data/desert_resized_nearest_neighbour.jpg'
        algos = resize.NearestNeigbhour('tests/data/desert.jpg', 2)
        algos.process(self.OUTPUT_FILE)

        img = self.open_image()
        self.assertEqual((2048, 1536), img.size)

    def test_resize_bird(self):
        self.OUTPUT_FILE = 'tests/data/bird_resized_nearest_neighbour.jpg'
        algos = resize.NearestNeigbhour('tests/data/bird.jpg', 4)
        algos.process(self.OUTPUT_FILE)

        img = self.open_image()
        self.assertEqual((896, 900), img.size)


class TestBilinearInterpolation(BaseTestResize):
    def test_resize_desert(self):
        self.OUTPUT_FILE = 'tests/data/desert_resized_bilinear.jpg'
        algos = resize.BilinearInterpolation('tests/data/desert.jpg', 2)
        algos.process(self.OUTPUT_FILE)

        img = self.open_image()
        self.assertEqual((2048, 1536), img.size)

    def test_resize_bird(self):
        self.OUTPUT_FILE = 'tests/data/bird_resized_bilinear.jpg'
        algos = resize.BilinearInterpolation('tests/data/bird.jpg', 4)
        algos.process(self.OUTPUT_FILE)

        img = self.open_image()
        self.assertEqual((896, 900), img.size)


class TestBicubicInterpolation(BaseTestResize):
    def test_coeficient(self):
        algo = resize.BicubicInterpolation('tests/data/bird.jpg', 4)
        cofs = algo.get_coefficients(10)
        self.assertEqual(-607.5, cofs[0])
        self.assertEqual(1026.0,  cofs[1])
        self.assertEqual(-1092.5, cofs[2])
        self.assertEqual(675.0, cofs[3])

    def test_resize_bird(self):
        self.OUTPUT_FILE = 'tests/data/bird_resized_bicubic.jpg'
        algos = resize.BicubicInterpolation('tests/data/bird.jpg', 2)
        algos.process(self.OUTPUT_FILE)

        img = self.open_image()
        self.assertEqual((448, 450), img.size)