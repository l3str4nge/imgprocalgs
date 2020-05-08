import os
from unittest import TestCase
from imgprocalgs.algorithms import color_accent


class TestSepia(TestCase):
    TEST_IMAGE = "tests/data/flower.jpg"

    def setUp(self):
        self.dest_path = 'tests/data/flower_accented.jpg'

    def tearDown(self):
        os.remove(self.dest_path)

    def test_sepia(self):
        color_accent.accent_color(self.TEST_IMAGE, self.dest_path, 60, 40)
