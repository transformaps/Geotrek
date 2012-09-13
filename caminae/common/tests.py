from django.test import TestCase

from .utils import almostequal


class UtilsTest(TestCase):
    def test_almostequal(self):
        self.assertTrue(almostequal(0.001, 0.002))
        self.assertFalse(almostequal(0.001, 0.002, precision=3))
        self.assertFalse(almostequal(1, 2, precision=0))
        self.assertFalse(almostequal(-1, 1))
        self.assertFalse(almostequal(1, -1))