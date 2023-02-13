from misaligned_production import print_color_map
from misaligned_test_functions import TestMisaligned

print_color_map()
test_object = TestMisaligned()

test_object.test_pair_number("White Blue", 1)
test_object.test_major_color("Red Green")
test_object.test_minor_color("Red Green")
