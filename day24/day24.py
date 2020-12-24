walk = {
    'nw': (-0.5, 1),
    'ne': (0.5, 1),
    'e': (1, 0),
    'w': (-1, 0),
    'sw': (-0.5, -1),
    'se': (0.5, -1)
}


with open('day24/input.data') as input:
    lines = input.read().split('\n')

tile_map = {}
for line in lines:
    (x, y)= (0, 0)
    i = 0
    while i < len(line):
        if line[i] in ['n', 's']:
            command = line[i:i+2]
            i += 2
        else:
            command = line[i]
            i += 1
        (walk_x, walk_y) = walk[command]
        x += walk_x
        y += walk_y
    if (x, y) in tile_map.keys():
        tile_map[(x,y)] = 'white' if tile_map[(x, y)] == 'black' else 'black'
    else:
        tile_map[(x, y)] = 'black'
black_tiles_count = len([1 for val in tile_map.values() if val == 'black'])
print(f'first solution: {black_tiles_count}')
