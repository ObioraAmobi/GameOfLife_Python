def next(cells):
    return survivors(cells) + come_to_life(cells)

def neighbours_of(x, y):
    return [
        (x-1,y-1), (x,y-1), (x+1,y-1),
        (x-1,y),            (x+1,y),
        (x-1,y+1), (x,y+1), (x+1,y+1)
    ]


def living_neighbours(cells, (x, y)):
    potential_neighbours = neighbours_of(x, y)
    return set(potential_neighbours).intersection(cells)


def number_of_living_neighbours(cells, cell):
    return len(living_neighbours(cells, cell))


def cell_survives(cells, cell):
    neighbours = number_of_living_neighbours(cells, cell)
    return neighbours == 2 or neighbours == 3

def survivors(cells):
    return [cell for cell in cells if cell_survives(cells, cell)]

def come_to_life(cells):
    return []