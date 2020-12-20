filename = 'input.txt'

TILE_COUNT = 144
TILE_PIXEL_WIDTH = 10
IMAGE_DIMENSION = 12

class Tile:

    def __init__(self, no, image):
        self.no = no
        self.image = image

        self.border_info = []
        # 4 x 2 matrix, [i][j]
        # [0][:] -> top-bottom
        # [1][:] -> left-right
        # [2][:] -> top-bottom reversed
        # [3][:] -> left-right reversed
        self.border_set = set()

        edges = []
        edges.append(image[0][:])
        edges.append([row[-1] for row in image])
        edges.append(image[-1][:])
        edges.append([row[0] for row in image])

        reverse_edges = [edge[::-1] for edge in edges]

        for edge in (edges + reverse_edges):
            self.border_set.add(int(''.join(edge), 2))

    def __repr__(self):
        return 'Tile({})'.format(self.no)


tile_lst = []

with open(filename) as file:
    for i in range(TILE_COUNT):
        tile_no = int(file.readline().strip().split()[1][:-1])

        image = []
        for j in range(TILE_PIXEL_WIDTH):
            row = file.readline().strip()
            row = row.replace('#', '1')
            row = row.replace('.', '0')
            image.append(list(row))
        file.readline()

        tile = Tile(tile_no, image)
        tile_lst.append(tile)

no2tile = dict()
for tile in tile_lst:
    no2tile[tile.no] = tile

corner_lst = []

for tile in tile_lst:
    neighbor_count = 0
    for other in tile_lst:

        if tile is other:
            continue

        if tile.border_set & other.border_set:
            neighbor_count += 1

    if neighbor_count < 3:
        corner_lst.append(tile)

current_tile = corner_lst[0]
tile_lst.remove(current_tile)

merged = [[None for j in range(IMAGE_DIMENSION)] for i in range(IMAGE_DIMENSION)]
merged[0][0] = current_tile


current_tile = no2tile[1283]
print(corner_lst)

print(current_tile.no)
print()


row = 0
col = 1
for tile in tile_lst:
    if current_tile.border_set & tile.border_set:
        print(tile.no)
        merged[row][col] = tile
        row = 1
        col = 0

tile_lst.remove(merged[0][1])
tile_lst.remove(merged[1][0])


def find_only_neighbor(tile):
    retval = None
    for other in tile_lst:
        if tile.border_set & other.border_set:
            if retval is None:
                retval = other
            else:
                raise ValueError('More than two neighbors')

    if retval is None:
        raise ValueError('No neighbor found')

    return retval


def find_common_neighbor(tile1, tile2):
    retval = None
    for other in tile_lst:
        if tile1.border_set & other.border_set and tile2.border_set & other.border_set:
            if retval is None:
                retval = other
            else:
                raise ValueError('More than two common neighbors')
    if retval is None:
        raise ValueError('No neighbor found')

    return retval

row = 1
col = 1
tile = find_common_neighbor(merged[row - 1][col], merged[row][col - 1])
merged[row][col] = tile
tile_lst.remove(tile)

print('===')

# Finding the places each tile will go

for col in range(2, IMAGE_DIMENSION):
    row = 0
    tile = find_only_neighbor(merged[row][col - 1])
    merged[row][col] = tile
    tile_lst.remove(tile)

    row = 1
    tile = find_common_neighbor(merged[row - 1][col], merged[row][col - 1])
    merged[row][col] = tile
    tile_lst.remove(tile)

for row in range(2, IMAGE_DIMENSION):
    col = 0
    tile = find_only_neighbor(merged[row - 1][col])
    merged[row][col] = tile
    tile_lst.remove(tile)

    for col in range(1, IMAGE_DIMENSION):
        tile = find_common_neighbor(merged[row - 1][col], merged[row][col - 1])
        merged[row][col] = tile
        tile_lst.remove(tile)

print(tile_lst)

print(merged)

# Rotate and/or flip each tile to fit neighbors (fixing [0][0])

def rotate90(im, width=TILE_PIXEL_WIDTH):
    retval = [['2' for j in range(width)] for i in range(width)]

    for i in range(width):
        for j in range(width):
            retval[j][width - i - 1] = im[i][j]

    return retval

def fliph(im, width=TILE_PIXEL_WIDTH):
    retval = [['2' for j in range(width)] for i in range(width)]

    for i in range(width):
        for j in range(width):
            retval[i][width - j - 1] = im[i][j]

    return retval

def flipv(im, width=TILE_PIXEL_WIDTH):
    retval = [['2' for j in range(width)] for i in range(width)]

    for i in range(width):
        for j in range(width):
            retval[width - i - 1][j] = im[i][j]

    return retval


row = 0
for col in range(1, IMAGE_DIMENSION):
    prev_tile = merged[row][col - 1]
    right_edge = [prev_tile.image[i][-1] for i in range(TILE_PIXEL_WIDTH)]
    tile = merged[row][col]

    for k in range(4):
        tile.image = rotate90(tile.image)
        left_edge = [tile.image[i][0] for i in range(TILE_PIXEL_WIDTH)]

        if left_edge == right_edge:
            break

        tile.image = flipv(tile.image)
        left_edge = [tile.image[i][0] for i in range(TILE_PIXEL_WIDTH)]

        if left_edge == right_edge:
            break

        tile.image = flipv(tile.image)
    else:
        raise ValueError('No fitting tile is found')

for col in range(IMAGE_DIMENSION):
    for row in range(1, IMAGE_DIMENSION):
        prev_tile = merged[row - 1][col]
        down_edge = [prev_tile.image[-1][j] for j in range(TILE_PIXEL_WIDTH)]
        tile = merged[row][col]

        for k in range(4):
            tile.image = rotate90(tile.image)
            up_edge = [tile.image[0][j] for j in range(TILE_PIXEL_WIDTH)]

            if up_edge == down_edge:
                break

            tile.image = fliph(tile.image)
            up_edge = [tile.image[0][j] for j in range(TILE_PIXEL_WIDTH)]

            if up_edge == down_edge:
                break

            tile.image = fliph(tile.image)
        else:
            raise ValueError('No fitting tile is found')

# Remove borders

for row in range(IMAGE_DIMENSION):
    for col in range(IMAGE_DIMENSION):
        tile = merged[row][col]

        border_removed_image = [tile.image[i][1:-1] for i in range(1, TILE_PIXEL_WIDTH - 1)]
        tile.image = border_removed_image


TILE_PIXEL_WIDTH = TILE_PIXEL_WIDTH - 2

bigimage = [[-1 for j in range(IMAGE_DIMENSION * TILE_PIXEL_WIDTH)] for i in range(IMAGE_DIMENSION * TILE_PIXEL_WIDTH)]

for row in range(IMAGE_DIMENSION):
    for i in range(TILE_PIXEL_WIDTH):
        for col in range(IMAGE_DIMENSION):
            tile = merged[row][col]
            for j in range(TILE_PIXEL_WIDTH):
                bigimage[row * TILE_PIXEL_WIDTH + i][col * TILE_PIXEL_WIDTH + j] = int(tile.image[i][j])

                """
                if tile.image[i][j] == '1':
                    print('#', end='')
                else:
                    print(' ', end='')
                """


# Find the pattern

pattern = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
           (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]

print(bigimage)
# 3x20 pattern

width = len(bigimage)


# bigimage = flipv(bigimage, width=width)

monster_count = 0

for i in range(4):

    bigimage = rotate90(bigimage, width=width)
    bigimage = flipv(bigimage, width=width)

    for row in range(0, width - 2):
        for col in range(0, width - 19):
            for drow, dcol in pattern:
                if bigimage[row + drow][col + dcol] == 0:
                    break
            else:
                monster_count += 1
                print(row + 1, col + 1, col + 1 + 18)

    bigimage = flipv(bigimage, width=width)

print(monster_count)

positive_count = 0
for row in bigimage:
    positive_count += sum(row)

print(positive_count)

answer = positive_count - monster_count * len(pattern)
print(answer)
