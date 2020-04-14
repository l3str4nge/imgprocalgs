from unittest import TestCase
from imgprocalgs.algorithms import negative


class TestNegative(TestCase):
    def test_negative(self):
        negative.make_negative("tests/data/desert.jpg")


