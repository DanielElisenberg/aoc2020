from collections import deque
from copy import deepcopy
import numpy as np

def examine_slope(map, angle):
    map = deepcopy(map)
    trees_encountered = 0

    for y in range(len(map)):
        map[y].rotate(y*-angle)
        if map[y][0] == '#':
            trees_encountered += 1
    return trees_encountered


with open('day03/input.data') as input:
    map = [deque(line) for line in input.read().splitlines()]

trees_encountered = examine_slope(map, 3)
print(f'first solution: {trees_encountered}')

trees_encountered = np.product(
    [examine_slope(m, a) for (m, a) in 
    [(map, 1),(map, 3),(map, 5),(map, 7), (map[::2], 1)]]
)
print(f'second solution: {trees_encountered}')
