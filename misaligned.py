def print_color_map():
    COLOR_MAP = dict()
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            COLOR_MAP[i * 5 + j] = major + ' ' + minor
            # print(f'{i * 5 + j} | {COLOR_MAP[i * 5 + j]}')
    return COLOR_MAP
    
def get_pair_number(color_map, color_pair):
    pair_number = list(filter(lambda idx: color_map[idx] == color_pair, color_map))[0]
    return pair_number

color_map = print_color_map()
pair_number = get_pair_number(color_map, 'White Blue')
assert(pair_number == 1)
print("All is well (maybe!)\n")
