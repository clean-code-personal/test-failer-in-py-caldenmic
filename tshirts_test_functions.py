import unittest
from prod import size

class TestTshirts(unittest.TestCase):
    
    def test_small_size(self, shirt_size):
        shirt_size = size(shirt_size)
        self.assertEqual(shirt_size, 'S')
    
    def test_medium_size(self, shirt_size):
        shirt_size = size(shirt_size)
        self.assertEqual(shirt_size, 'M')
    
    def test_large_size(self, shirt_size):
        shirt_size = size(shirt_size)
        self.assertEqual(shirt_size, 'L')
