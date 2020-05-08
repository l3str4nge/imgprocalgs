from unittest import TestCase
from imgprocalgs.algorithms import utilities


class TestUtilities(TestCase):
    TEST_IMAGE = "tests/data/desert.jpg"

    def test_rgb_to_hsv(self):
        hsv = utilities.rgb_to_hsv(255, 255, 255)
        self.assertEqual(0, hsv.h)
        self.assertEqual(0, hsv.s)
        self.assertEqual(1.0, hsv.v)

        hsv = utilities.rgb_to_hsv(204, 221, 221)
        self.assertEqual(180, hsv.h)
        self.assertEqual(0.0769230769230769, hsv.s)
        self.assertEqual(0.8666666666666667, hsv.v)

        hsv = utilities.rgb_to_hsv(171, 205, 234)
        self.assertEqual(207.6190476190476, hsv.h)
        self.assertEqual(0.2692307692307693, hsv.s)
        self.assertEqual(0.9176470588235294, hsv.v)

        hsv = utilities.rgb_to_hsv(230, 10, 20)
        self.assertEqual(357.27272727272725, hsv.h)
        self.assertEqual(0.9565217391304348, hsv.s)
        self.assertEqual(0.9019607843137255, hsv.v)

    def test_hsv_to_rgb(self):
        rgb = utilities.hsv_to_rgb(200, 0.1, 0.2)
        self.assertEqual(45, rgb.r)
        self.assertEqual(49, rgb.g)
        self.assertEqual(51, rgb.b)

        rgb = utilities.hsv_to_rgb(150, 0.5, 0.8)
        self.assertEqual(102, rgb.r)
        self.assertEqual(204, rgb.g)
        self.assertEqual(153, rgb.b)

    def test_greyscale(self):
        self.assertEqual(91.36, utilities.get_greyscale(100, 100, 100))
        self.assertEqual(0.0, utilities.get_greyscale(0, 0, 0))
        self.assertEqual(67.095, utilities.get_greyscale(255, 0, 113))
        self.assertEqual(232.968, utilities.get_greyscale(255, 255, 255))
        self.assertEqual(168.93599999999998, utilities.get_greyscale(165, 189, 201))
