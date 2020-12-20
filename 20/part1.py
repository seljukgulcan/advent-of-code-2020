filename = 'input.txt'

TILE_COUNT = 144
TILE_PIXEL_WIDTH = 10


class Tile:

    def __init__(self, no, image):
        self.no = no
        self.image = image

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
        return str(self.no)


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

    corner_lst = []

    for tile in tile_lst:
        neighbor_count = 0
        for other in tile_lst:
            if tile.border_set & other.border_set:
                neighbor_count += 1

        if neighbor_count < 4:
            corner_lst.append(tile)

    answer = 1
    for tile in corner_lst:
        answer *= tile.no

    print(answer)
