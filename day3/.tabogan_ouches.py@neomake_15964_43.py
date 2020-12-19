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
    x, y = start_pos
    while y < height_of_slope:  
        y



#right 3 down 1

