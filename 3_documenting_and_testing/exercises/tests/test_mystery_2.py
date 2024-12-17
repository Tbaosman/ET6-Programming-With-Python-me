import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_2(''), None)
        
    def test_string(self):
        """"""
        self.assertEqual(mystery_2("tbaosman"), 8)
    
    '''def test_integers(self):
        """"""
        self.assertEqual(mystery_2(12345), 5)'''
        
    def test_combination(self):
        """"""
        None
