class Tile:
    def __init__(self, tiledata):
        tiledata = tiledata.split('\n')
        self.id = int(tiledata[0][5:-1])
        self.tile = []
        for i in range(1, 11):
            self.tile.append(list(tiledata[i]))

    def rotate(self):
        self.tile = [list(row) for row in zip(*reversed(self.tile))]

    def flip(self):
        self.tile = [list(reversed(row)) for row in self.tile]

    def get_edge(self, direction):
        if direction == 'north':
            return self.tile[0]
        elif direction == 'south':
            return self.tile[9]
        elif direction == 'east':
            return [row[9] for row in self.tile]
        elif direction == 'west':
            return [row[0] for row in self.tile]
        else:
            raise ValueError('Invalid direction')


def add_search_locations(locations, coord):
    (x, y) = coord
    for search in [-1, 1]:
        if (x+search, y) not in locations:
            locations.append((x+search, y))
        if (x, y+search) not in locations:
            locations.append((x, y+search))


def match(tile, matchers):
    if matchers['north_tile'] is not None:
        tile_edge = tile.get_edge('north')
        match_edge = matchers['north_tile'].get_edge('south')
        if tile_edge != match_edge:
            return False
    if matchers['south_tile'] is not None:
        tile_edge = tile.get_edge('south')
        match_edge = matchers['south_tile'].get_edge('north')
        if tile_edge != match_edge:
            return False
    if matchers['west_tile'] is not None:
        tile_edge = tile.get_edge('west')
        match_edge = matchers['west_tile'].get_edge('east')
        if tile_edge != match_edge:
            return False
    if matchers['east_tile'] is not None:
        tile_edge = tile.get_edge('east')
        match_edge = matchers['east_tile'].get_edge('west')
        if tile_edge != match_edge:
            return False
    return True


def place_tile(coord, placed_tiles, unplaced_tiles):
    (x, y) = coord
    matchers = {
        'north_tile': placed_tiles.get((x, y+1), None),
        'south_tile': placed_tiles.get((x, y-1), None),
        'west_tile': placed_tiles.get((x+1, y), None),
        'east_tile': placed_tiles.get((x-1, y), None)
    }
    for tile in unplaced_tiles:
        for i in range(2):
            tile.flip()
            for i in range(4):
                tile.rotate()
                if match(tile, matchers):
                    placed_tiles[(coord)] = tile
                    unplaced_tiles.remove(tile)
                    return True
    return False


def multiply_corners(placed_tiles):
    min_x = 1
    min_y = 1
    max_x = -1
    max_y = -1
    for coord in placed_tiles.keys():
        (x, y) = coord
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        min_x = x if x < min_x else min_x
        min_y = y if y < min_y else min_y
    return (
        placed_tiles[(min_x, min_y)].id *
        placed_tiles[(min_x, max_y)].id *
        placed_tiles[(max_x, max_y)].id *
        placed_tiles[(max_x, min_y)].id
    )


with open('day20/input.data') as input:
    tiles = [tile for tile in input.read().split('\n\n')]

unplaced_tiles = [Tile(tiledata) for tiledata in tiles]
placed_tiles = {}
placed_tiles[(0, 0)] = unplaced_tiles[0]
unplaced_tiles.remove(unplaced_tiles[0])
search_locations = []
add_search_locations(search_locations, (0, 0))
print(search_locations)

while unplaced_tiles:
    search_at = search_locations.pop()
    if place_tile(search_at, placed_tiles, unplaced_tiles):
        add_search_locations(search_locations, search_at)

print(multiply_corners(placed_tiles))
