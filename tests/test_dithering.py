import os
from unittest import TestCase
from imgprocalgs.algorithms.dithering import FloydSteinberg


class TestFloydSteinberg(TestCase):
    TEST_IMAGE = "tests/data/lena.jpg"

    def setUp(self):
        self.dest_path = 'tests/data/'

    def tearDown(self):
        pass
        # os.remove(os.path.join(self.dest_path, 'output_greyscale.jpg'))
        # os.remove(os.path.join(self.dest_path, 'output_floyd_steinberg.jpg'))

    def test_algorithm(self):
        fs = FloydSteinberg(self.TEST_IMAGE, self.dest_path, 100)
        fs.process()
