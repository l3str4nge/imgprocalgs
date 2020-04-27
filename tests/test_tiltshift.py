import os
from unittest import TestCase
from imgprocalgs.algorithms.tilt_shift import TiltShift


class TestTiltShift(TestCase):
    TEST_IMAGE = "tests/data/desert.jpg"
    DEST_PATH = "/tests/data"

    def test_make_filter_factor(self):
        self.assertEqual(0.24197072451914337, TiltShift._make_filter_factor(1, 1))
        self.assertEqual(9.463226016607707e-05, TiltShift._make_filter_factor(2, 2))

    def test_blur(self):
        ts = TiltShift(self.TEST_IMAGE, self.DEST_PATH, 1, 4)
        self.assertEqual(1.075, ts._make_blur(5, 200))
        self.assertEqual(2.8461538461538463, ts._make_blur(8, 13))






