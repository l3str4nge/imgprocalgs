import os
from unittest import TestCase
from imgprocalgs.algorithms import convolution
import numpy as np


class TestConvolution(TestCase):
    TEST_IMAGE = "tests/data/desert.jpg"

    def setUp(self):
        self.dest_path = 'tests/data/desert_sepia.jpg'

    def tearDown(self):
        os.remove(self.dest_path)

    def test_convolution(self):
        """ Create (255, 255, 255) image and  check if all (0, 0, 0)"""
        #tone.make_sepia(self.TEST_IMAGE, self.dest_path, 30)
