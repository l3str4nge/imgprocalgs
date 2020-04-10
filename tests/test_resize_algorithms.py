from unittest import TestCase
from imgprocalgs.algorithms import resize

#TODO: more tests
class TestNearestNeighbour(TestCase):
    def test_resize(self):
        algos = resize.NearestNeigbhour('tests/data/desert.jpg', 2)
        algos.process()

    def test_resize_bird(self):
        algos = resize.NearestNeigbhour('tests/data/bird.jpg', 4)
        algos.process()


class TestBilinearInterpolation(TestCase):
    def test_resize(self):
        algos = resize.BilinearInterpolation('tests/data/desert.jpg', 2)
        algos.process()

    def test_resize_bird(self):
        algos = resize.BilinearInterpolation('tests/data/bird.jpg', 4)
        algos.process()
