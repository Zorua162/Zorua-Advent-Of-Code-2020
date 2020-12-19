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
    height_of_slope = len(segment) - start_pos[1] - 1
    length_of_segment = len(segment[0]) - start_pos[0]
    num_steps = height_of_slope/down_step
    length_of_slope = num_steps * right_step
    num_join_segments = ceil(length_of_slope/length_of_segment)
    slope = [[] for j in range(len(segment))]
    print(slope)
    for i, line in enumerate(segment):
        slope[i].append(line*(num_join_segments+1))
    slope = slope[:-1]
    slope = [i[0] for i in slope]
    print(len(slope[0]))

    x_coord, y_coord = start_pos
    tree_count = 0
    while y_coord < height_of_slope:
        print(f'Starting row {y_coord} position {x_coord}')
        row = slope[y_coord]
        print(row)
        position = row[x_coord]
        if position == '#':
            tree_count += 1
        y_coord += down_step
        x_coord += right_step
    print(f'Hit {tree_count} trees for Right {right_step}, Down ' +
          f'{down_step}')
    return tree_count
#right 1 down 1
r1d1 = walk_and_count(data, [0, 0], 1, 1)
#right 3 down 1
r3d1 = walk_and_count(data, [0, 0], 1, 3)
#right 5 down 1
r5d1 = walk_and_count(data, [0, 0], 1, 5)
#right 7 down 1
r7d1 = walk_and_count(data, [0, 0], 1, 7)
#right 1 down 2
r1d2 = walk_and_count(data, [0, 0], 2, 1)

ans = r1d1 * r3d1 * r5d1 * r7d1 * r1d2

print(f'The multiplication of all the trees hit is {ans}')
