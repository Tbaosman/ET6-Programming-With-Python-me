import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
    def test_positive(self):
        """"""
        self.assertEqual(mystery_1(2,5), 7)
    def test_combination(self):
        """"""
        self.assertEqual(mystery_1(-2,2), 0)
    def test_negative(self):
        """"""
        self.assertEqual(mystery_1(-2,-4), -6)
