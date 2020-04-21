from unittest import TestCase
import os
from imgprocalgs.algorithms import negative
from PIL import Image


class TestNegative(TestCase):
    TEST_IMAGE = "tests/data/test.jpg"
    TEST_DEST_IMAGE = "tests/data/test_negative.jpg"

    def setUp(self):
        self.image = Image.new("RGB", (100, 100), "#FFFFFF")
        self.image.save(self.TEST_IMAGE)

    def tearDown(self):
        os.remove(self.TEST_IMAGE)
        os.remove(self.TEST_DEST_IMAGE)

    def test_negative(self):
        """ Create (255, 255, 255) image and  check if all (0, 0, 0)"""
        negative.make_negative(self.TEST_IMAGE, self.TEST_DEST_IMAGE)

        pixels = Image.open(self.TEST_DEST_IMAGE).load()
        self.assertEqual(pixels[0, 0], (0, 0, 0))
