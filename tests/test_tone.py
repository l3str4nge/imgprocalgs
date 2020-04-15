from unittest import TestCase
from imgprocalgs.algorithms import tone


class TestSepia(TestCase):
    TEST_IMAGE = "tests/data/desert.jpg"

    def test_sepia(self):
        """ Create (255, 255, 255) image and  check if all (0, 0, 0)"""
        tone.make_sepia(self.TEST_IMAGE, 30)







