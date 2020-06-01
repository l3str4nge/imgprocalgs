import os
from unittest import TestCase
from imgprocalgs.algorithms.dithering import FloydSteinberg, JarvisJudiceNinke


class TestFloydSteinberg(TestCase):
    TEST_IMAGE = "tests/data/lena.jpg"

    def setUp(self):
        self.dest_path = 'tests/data/'

    def tearDown(self):
        os.remove(os.path.join(self.dest_path, 'output_greyscale.jpg'))
        os.remove(os.path.join(self.dest_path, 'output_floyd_steinberg.jpg'))

    def test_algorithm(self):
        fs = FloydSteinberg(self.TEST_IMAGE, self.dest_path, 100)
        fs.process()


class TestJarvisJudiceNinke(TestCase):
    TEST_IMAGE = "tests/data/lena.jpg"

    def setUp(self):
        self.dest_path = 'tests/data/'

    def tearDown(self):
        os.remove(os.path.join(self.dest_path, 'output_greyscale.jpg'))
        os.remove(os.path.join(self.dest_path, 'output_fjarvis_judice_ninke.jpg'))

    def test_algorithm(self):
        fs = JarvisJudiceNinke(self.TEST_IMAGE, self.dest_path, 100)
        fs.process()