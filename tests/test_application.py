from unittest import TestCase
from imgprocalgs import application


class TestApplication(TestCase):
    def test_validate_algorithm_name(self):
        with self.assertRaises(Exception) as context:
            application.validate_algorithm_name("NOT_FOUND")

        self.assertTrue('Algorithm with name NOT_FOUND is not defined!' in str(context.exception))
        self.assertTrue(application.validate_algorithm_name('sepia'))
        self.assertTrue(application.validate_algorithm_name('negative'))
        self.assertTrue(application.validate_algorithm_name('nearest_neighbour'))
        self.assertTrue(application.validate_algorithm_name('bilinear_interpolation'))
        self.assertTrue(application.validate_algorithm_name('bicubic_interpolation'))
