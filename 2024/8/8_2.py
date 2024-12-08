import itertools
import time

outside= ' '

def get_harmonics_coodinates(x1, y1, x2, y2, width, height):
    coordinates = set()
    diff_x = x1 - x2
    diff_y = y1 - y2
    harmonic = 0
    while True:
        if 0 <= x2 - (harmonic * diff_x) < width and 0 <= y2 - (harmonic * diff_y) < width:
            coordinates.add((x2 - (harmonic * diff_x) , y2 - (harmonic * diff_y)))
            harmonic += 1
        else:
            break
    harmonic = 0    
    while True:
        if 0 <= x1 + (harmonic * diff_x) < width and 0 <= y1 + (harmonic * diff_y) < width:
            coordinates.add((x1 + (harmonic * diff_x) , y1 + (harmonic * diff_y)))
            harmonic += 1
        else:
            break
    
    return coordinates


class AntennaGrid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
            self.unique_frequencies = set(values)
            self.unique_frequencies.remove('.')  
            self.frequency_coordinates = {}
            for j in range(self.height):
                for i in range(self.width):    
                    if self.get(i,j) != '.':
                        frequency = self.get(i,j)
                        if frequency not in self.frequency_coordinates:
                            self.frequency_coordinates[frequency] = set()
                        self.frequency_coordinates[frequency].add((i,j))
        else:
            raise ValueError("This grid is not coherent")

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return outside
        
    def __repr__(self):
        rows = [
            self.values[i * self.width:(i + 1) * self.width]
            for i in range(self.height)
        ]
        return '\n'.join(' '.join(map(str, row)) for row in rows)

class AntiNodeGrid:
    def __init__(self, antenna_grid):
        self.width = antenna_grid.width
        self.height = antenna_grid.height
        self.values = ['.'] * (width * height)
        for frequency in antenna_grid.unique_frequencies:
            for coordinate_pair in itertools.combinations(antenna_grid.frequency_coordinates[frequency], 2):
                harmonics_coodinates = get_harmonics_coodinates(
                    coordinate_pair[0][0],
                    coordinate_pair[0][1],
                    coordinate_pair[1][0],
                    coordinate_pair[1][1],
                    self.width,
                    self.height)
                for hamonics_coordinate in harmonics_coodinates:
                    self.set(hamonics_coordinate[0],hamonics_coordinate[1],'#')

        self.anti_node_coordinates = set()
        for j in range(self.height):
            for i in range(self.width):    
                if self.get(i,j) == '#':
                    self.anti_node_coordinates.add((i,j))
                
    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.values[x + y * self.width] = value

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.values[x + y * self.width]
        else:
            return outside
        
    def __repr__(self):
        rows = [
            self.values[i * self.width:(i + 1) * self.width]
            for i in range(self.height)
        ]
        return '\n'.join(' '.join(map(str, row)) for row in rows)

with open("2024/8/input.txt", mode="r") as file:
    values = []
    width = 0
    height = 0
    for line in file:
        clean_line = line.strip('\n')
        values.extend(list(clean_line))
        height += 1
        width = max(width,len(clean_line))

part2_start_time = time.time()

antenna_grid = AntennaGrid(width, height, values)
anti_node_grid = AntiNodeGrid(antenna_grid)
print(f'Anti Nodes Count {len(anti_node_grid.anti_node_coordinates)}')

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")