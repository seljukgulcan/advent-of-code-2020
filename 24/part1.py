import re

filename = 'input.txt'


def parse_direction(line):
    pattern = r'nw|ne|e|se|sw|w'
    return re.findall(pattern, line)


with open(filename) as file:
    tile_dir_lst = [parse_direction(line.strip()) for line in file]


class Tile:
    def __init__(self):
        self.nw = None
        self.ne = None
        self.e = None
        self.se = None
        self.sw = None
        self.w = None
        self.is_white = True

    def flip(self):
        self.is_white = not self.is_white


grid_row_count = 100
grid_col_count = 100

G = []

for row in range(grid_row_count):

    G.append([])
    for col in range(grid_col_count):
        tile = Tile()

        if row != 0:
            if row % 2 == 0:
                tile.ne = G[row - 1][col]
                G[row - 1][col].sw = tile

                if col != 0:
                    tile.nw = G[row - 1][col - 1]
                    G[row - 1][col - 1].se = tile
            else:
                tile.nw = G[row - 1][col]
                G[row - 1][col].se = tile

                if col != grid_col_count - 1:
                    tile.ne = G[row - 1][col + 1]
                    G[row - 1][col + 1].sw = tile

        if col != 0:
            tile.w = G[row][col - 1]
            G[row][col - 1].e = tile

        G[row].append(tile)

origin_row = grid_row_count // 2
origin_col = grid_col_count // 2
origin = G[origin_row][origin_col]

for tile_dir in tile_dir_lst:

    tile = origin

    for d in tile_dir:
        if d == 'nw':
            tile = tile.nw
        elif d == 'ne':
            tile = tile.ne
        elif d == 'e':
            tile = tile.e
        elif d == 'se':
            tile = tile.se
        elif d == 'sw':
            tile = tile.sw
        elif d == 'w':
            tile = tile.w
        else:
            raise ValueError('Unexpected direction : {}'.format(d))

    tile.flip()

count = 0
for row in range(grid_row_count):
    for col in range(grid_col_count):
        tile = G[row][col]
        if not tile.is_white:
            count += 1

print(count)