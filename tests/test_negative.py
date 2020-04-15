from unittest import TestCase
from imgprocalgs.algorithms import negative
from PIL import Image


class TestNegative(TestCase):
    TEST_IMAGE = "tests/data/test.jpg"

    def setUp(self):
        self.image = Image.new("RGB", (100, 100), "#FFFFFF")
        self.image.save(self.TEST_IMAGE)

    def test_negative(self):
        """ Create (255, 255, 255) image and  check if all (0, 0, 0)"""
        negative.make_negative(self.TEST_IMAGE)

        pixels = Image.open('negative.jpg').load()
        self.assertEqual(pixels[0, 0], (0, 0, 0))






