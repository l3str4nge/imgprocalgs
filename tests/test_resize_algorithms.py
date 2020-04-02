from unittest import TestCase
from imgprocalgs.algorithms import resize


class TestNearestNeighbour(TestCase):
    def test_resize(self):
        algos = resize.NearestNeigbhour('data/desert.jpg', 2)
        algos.process()
