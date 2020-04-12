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


class TestBicubicInterpolation(TestCase):
    def test_coeficient(self):
        algo = resize.BicubicInterpolation('tests/data/bird.jpg', 4)
        cofs = algo.get_coefficients(10)
        self.assertEqual(-607.5, cofs[0])
        self.assertEqual(1026.0,  cofs[1])
        self.assertEqual(-1092.5, cofs[2])
        self.assertEqual(675.0, cofs[3])
