import os
from unittest import TestCase
from imgprocalgs.algorithms import convolution
import numpy as np
from PIL import Image


class TestConvolution(TestCase):
    TEST_IMAGE = "tests/data/flower.jpg"

    def setUp(self):
        self.image = Image.open(self.TEST_IMAGE)
        self.image = self.image.convert('1')
        self.image = np.asarray(self.image)

    def test_convolution(self):
        filter_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        output = convolution.convolution(self.image, filter_kernel)
        self.assertTrue(output.size != 0)
