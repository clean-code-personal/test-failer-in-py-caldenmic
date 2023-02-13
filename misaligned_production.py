COLOR_MAP = dict()
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def create_color_map():
    global COLOR_MAP, major_colors, minor_colors
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            COLOR_MAP[i * 5 + j + 1] = major + ' ' + minor
            # print(f'{i * 5 + j} | {COLOR_MAP[i * 5 + j]}')
    return COLOR_MAP
    
def get_pair_number(color_map, color_pair):
    pair_number = list(filter(lambda idx: color_map[idx] == color_pair, color_map))[0]
    return pair_number
    
def print_color_map():
    print(f"{'PAIR NUMBER': ^15}{'COLOR': <20}")
    for key, value in COLOR_MAP.items():
        print(f'{key: ^15}{value: <20}')
