from unittest import TestCase
from imgprocalgs.algorithms.tilt_shift import TiltShift


class TestTiltShift(TestCase):
    TEST_IMAGE = "tests/data/city.jpg"
    DEST_PATH = "tests/data"

    def test_make_filter_factor(self):
        self.assertEqual(0.7978845608028654, TiltShift._make_filter_factor(0.5, 0))
        self.assertEqual(0.12098536225957168, TiltShift._make_filter_factor(2, 2))

    def test_blur(self):
        ts = TiltShift(self.TEST_IMAGE, self.DEST_PATH, 1, 4)
        self.assertEqual(1.075, ts._make_blur(5, 200))
        self.assertEqual(2.8461538461538463, ts._make_blur(8, 13))

    def test_gt_min_factor(self):
        ts = TiltShift(self.TEST_IMAGE, self.DEST_PATH, 1, 4)

        ts.min_factor = 2
        self.assertTrue(ts.is_gt_min_factor(10))
        self.assertFalse(ts.is_gt_min_factor(1))

    def test_generate_filter(self):
        ts = TiltShift(self.TEST_IMAGE, self.DEST_PATH, 0.1, 6)

        ts.generate_filter_elements(blur=0.5, max_factor=700)
        self.assertEqual(2, len(ts.filter_elements))

    def test_process(self):
        ts = TiltShift(self.TEST_IMAGE, self.DEST_PATH, 0.1, 6, [300, 500])
        ts.process()
