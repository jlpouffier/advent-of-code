import itertools
import time

outside= ' '

def rotate_coordinate(x, y, center_x, center_y):
    diff_x = x - center_x
    diff_y = y - center_y
    return center_x - diff_x, center_y - diff_y

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
                anti_node1_coordinates = rotate_coordinate(coordinate_pair[0][0],coordinate_pair[0][1], coordinate_pair[1][0],coordinate_pair[1][1])
                anti_node2_coordinates = rotate_coordinate(coordinate_pair[1][0],coordinate_pair[1][1], coordinate_pair[0][0],coordinate_pair[0][1])
                self.set(anti_node1_coordinates[0],anti_node1_coordinates[1],'#')
                self.set(anti_node2_coordinates[0],anti_node2_coordinates[1],'#')
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

part1_start_time = time.time()

antenna_grid = AntennaGrid(width, height, values)
anti_node_grid = AntiNodeGrid(antenna_grid)
print(f'Anti Nodes Count {len(anti_node_grid.anti_node_coordinates)}')

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")