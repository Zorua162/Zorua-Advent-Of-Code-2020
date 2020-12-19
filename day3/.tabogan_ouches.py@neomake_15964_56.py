'''
Finding safe paths through the trees
'''


with open('./tree_layout.txt', 'r') as f:
    data = f.read().split('\n')


def walk_and_count(segment, start_pos, down_step, right_step):
    '''
    Walk down the slope in steps
    '''
    height_of_slope = len(segment) - start_pos[1]
    , y = start_pos
    tree_count = 0
    while y < height_of_slope:  
        if segment[y][x] == '#':
            tree_count += 1
        y += down_step
        x += right_step

#right 3 down 1
