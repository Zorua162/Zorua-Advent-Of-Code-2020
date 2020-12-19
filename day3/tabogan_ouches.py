'''
Finding safe paths through the trees
'''
from math import ceil


with open('./tree_layout.txt', 'r') as f:
    data = f.read().split('\n')


def walk_and_count(segment, start_pos, down_step, right_step):
    '''
    Walk down the slope in steps
    '''
    height_of_slope = len(segment) - start_pos[1]
    length_of_segment = len(segment[0]) - start_pos[0]
    num_steps = height_of_slope/down_step
    length_of_slope = num_steps * right_step
    num_join_segments = ceil(length_of_slope/length_of_segment)
    slope = [[] for j in range(len(segment))]
    print(slope)
    for i, line in enumerate(segment):
        slope[i].append(line*num_join_segments)

    x_coord, y_coord = start_pos
    tree_count = 0
    print(slope)
    while y_coord < height_of_slope:
        print(y_coord, x_coord)
        if slope[y_coord][x_coord] == '#':
            tree_count += 1
        y_coord += down_step
        x_coord += right_step print(tree_count)
    return tree_count

#right 3 down 1
walk_and_count(data, [0, 0], 1, 3)
