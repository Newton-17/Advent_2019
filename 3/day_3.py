"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/2
"""


conflict_list = []

def calculate_array_demensions(path_list):
    path_list = [(x[0], int(x[1:])) for x in path_list]
    up = 0
    down = 0
    left = 0
    right = 0
    for direction, count in path_list:
        if direction == 'U':
            up += count
        elif direction == 'D':
            down += count
        elif direction == 'L':
            left += count
        elif direction == 'R':
            right += count
    print('{} - {} - {} - {}'.format(up, down, left, right))
    return (up, down, left, right, path_list)

def get_grid(p1, p2):
    
    u1, d1, l1, r1, pl1 = calculate_array_demensions(p1)
    u2, d2, l2, r2, pl2 = calculate_array_demensions(p2)

    size = 20000
    print('Creating Grid')
    grid = [] 
    for i in range(size):
        new_row = ['.'] * (size)
        grid.append(new_row) 
    print('Grid Created')
    center = int(size/2), int(size/2)
    return (grid, center, pl1, pl2)
        
def create_up_row(grid, index, count):
    while count != 0:
        index = (index[0] - 1, index[1])
        value = grid[index[0]][index[1]]
        if value != '.':
            grid[index[0]][index[1]] = 'x'
            conflict_list.append((index[0], index[1]))
        else:
            grid[index[0]][index[1]] = '|'
        count -= 1
    return index

def create_down_row(grid, index, count):
    while count != 0:
        index = (index[0] + 1, index[1])
        value = grid[index[0]][index[1]]
        if value != '.':
            grid[index[0]][index[1]] = 'x'
            conflict_list.append((index[0], index[1]))
        else:
            grid[index[0]][index[1]] = '|'
        count -= 1
    return index

def create_left_column(grid, index, count):
    while count != 0:
        index = (index[0], index[1] - 1)
        value = grid[index[0]][index[1]]
        if value != '.':
            grid[index[0]][index[1]] = 'x'
            conflict_list.append((index[0], index[1]))
        else:
            grid[index[0]][index[1]] = '-'
        count -= 1
    return index

def create_right_column(grid, index, count):
    while count != 0:
        index = (index[0], index[1] + 1)
        value = grid[index[0]][index[1]]
        if value != '.':
            grid[index[0]][index[1]] = 'x'
            conflict_list.append((index[0], index[1]))
        else:
            grid[index[0]][index[1]] = '-'
        count -= 1
    return index

def get_closest_conflict(index):
    lowest = 9223372036854775807
    print('Start Index: {}'.format(index))
    for conflict in conflict_list:
        print('Conflict Point: {}'.format(conflict))
        distance = abs(index[0] - conflict[0]) + abs(index[1] - conflict[1])
        if distance < lowest:
            lowest = distance
    print(lowest)


def print_grid(grid):
    print('Printing out Grid....\n\n')
    for row in grid:
        print(''.join(row))

    print('\nGrid Printed Out')

if __name__ == '__main__':
    print('Starting Day 3 of Advent Calendar')
    with open('3/day_3_input.txt', 'r') as f:
        l1 = f.readline().rstrip("\n\r")
        p1 = [x for x in l1.split(',')]

        l2 = f.readline().rstrip("\n\r")
        p2 = [x for x in l2.split(',')]

        grid, s_index, pl1, pl2 = get_grid(p1, p2)

        start = 'X'
        intersection = 'int'
        p1_marker = '1'
        p2_marker = '2'

        c_index = (s_index[0], s_index[1])

        # Initial Marker to start
        grid[c_index[0]][c_index[1]] = start
        for i in len(pl1):

        for direction, count in pl1:
            if direction == 'U':
                c_index = create_up_row(grid, c_index, count)
            elif direction == 'D':
                c_index = create_down_row(grid, c_index, count)
            elif direction == 'L':
                c_index = create_left_column(grid, c_index, count)
            elif direction == 'R':
                c_index = create_right_column(grid, c_index, count)

        
        c_index = (s_index[0], s_index[1])
        for direction, count in pl2:
            if direction == 'U':
                c_index = create_up_row(grid, c_index, count)
            elif direction == 'D':
                c_index = create_down_row(grid, c_index, count)
            elif direction == 'L':
                c_index = create_left_column(grid, c_index, count)
            elif direction == 'R':
                c_index = create_right_column(grid, c_index, count)
        
        c_index = (s_index[0], s_index[1])
        get_closest_conflict(c_index)
        #print_grid(grid)





        
        