import unittest
from misaligned_production import create_color_map, get_pair_number, major_colors, minor_colors

color_map = create_color_map()

class TestMisaligned(unittest.TestCase):
    def test_pair_number(self, pair_color, expected_pair_number):
        pair_number = get_pair_number(color_map, pair_color)
        self.assertEqual(pair_number, expected_pair_number)
        
    def test_major_color(self, pair_color):
        major_color = pair_color.split(' ')[0]
        self.assertTrue(major_color in major_colors)
        
    def test_minor_color(self, pair_color):
        minor_color = pair_color.split(' ')[1]
        self.assertTrue(minor_color in minor_colors)
